"""Build a PowerPoint copy of one week's deck from deck-source/.

Use it when the online deck's own Share > Export is not available.

Usage:  python tools/build_pptx.py 1     (writes Week-01_*/Week-01-slides.pptx)
        python tools/build_pptx.py 2 out.pptx

Google Chrome (or Edge) lays the slides out exactly as the browser does, and
python-pptx turns every box, text and icon into editable PowerPoint shapes.
The fonts come from the fonts/ folder.
"""
import base64
import html
import io
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

ROOT = Path(__file__).resolve().parent.parent
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]
PX = 6350  # EMU per CSS pixel on a 1920 x 1080 slide (13.333 in wide)

FONT_FILES = [
    ("Rubik", "normal", "300 900", "Rubik[wght].ttf"),
    ("Rubik", "italic", "300 900", "Rubik-Italic[wght].ttf"),
    ("JetBrains Mono", "normal", "100 800", "JetBrainsMono[wght].ttf"),
    ("JetBrains Mono", "italic", "100 800", "JetBrainsMono-Italic[wght].ttf"),
]

# Line icons (24 x 24 grid, 2px stroke) for the x-icon names the slides use
ICONS = {
    "Book": '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/>',
    "Globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    "Tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "Wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "GraduationCap": '<path d="M21.42 10.92a1 1 0 0 0-.02-1.84L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.83l8.57 3.91a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "Code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "Settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    "CheckCircle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
    "Check": '<path d="M20 6 9 17l-5-5"/>',
    "Lightbulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    "Warning": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "Star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "Users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "Clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "Database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
    "Search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "Lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "Key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    "Play": '<polygon points="6 3 20 12 6 21 6 3"/>',
}

HARNESS_CSS = """
* { margin: 0; box-sizing: border-box; }
body { background: #808080; }
section { position: relative; width: 1920px; height: 1080px; overflow: hidden; }
h1 { font-size: 96px; font-weight: 600; line-height: 1.1; }
h2 { font-size: 64px; font-weight: 600; line-height: 1.15; }
h3 { font-size: 44px; font-weight: 600; line-height: 1.2; }
p { font-size: 32px; font-weight: 400; line-height: 1.4; }
ul, ol { padding-left: 1.3em; }
a { color: inherit; }
hr { border: none; height: 0; }
x-shape, x-icon, x-connector { display: block; }
aside { display: none; }
"""

MEASURE_JS = r"""
function col(c) {
  const m = /rgba?\(([^)]+)\)/.exec(c || "");
  if (!m) return null;
  const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number);
  const a = p.length > 3 ? p[3] : 1;
  if (a === 0) return null;
  return p.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, "0")).join("").toUpperCase();
}
function rel(el, base) {
  const r = el.getBoundingClientRect();
  return { x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height };
}
function px(v) { return parseFloat(v) || 0; }
function runs(el, upper) {
  const paras = [[]];
  (function walk(node) {
    for (const ch of node.childNodes) {
      if (ch.nodeType === 3) {
        const cs = getComputedStyle(ch.parentElement);
        let t = ch.nodeValue.replace(/[ \t\n\r\f]+/g, " ");
        if (upper) t = t.toUpperCase();
        const a = ch.parentElement.closest("a");
        paras[paras.length - 1].push({ text: t, color: col(cs.color), bold: +cs.fontWeight >= 600,
          italic: cs.fontStyle === "italic", href: a ? a.getAttribute("href") : null });
      } else if (ch.nodeType === 1) {
        if (ch.tagName === "BR") paras.push([]);
        else walk(ch);
      }
    }
  })(el);
  return paras.map(rs => {
    if (rs.length) { rs[0].text = rs[0].text.replace(/^ +/, ""); rs[rs.length - 1].text = rs[rs.length - 1].text.replace(/ +$/, ""); }
    const merged = [];
    for (const r of rs) {
      if (!r.text) continue;
      const last = merged[merged.length - 1];
      if (last && last.color === r.color && last.bold === r.bold && last.italic === r.italic && last.href === r.href) last.text += r.text;
      else merged.push(r);
    }
    return merged;
  });
}
function textItem(el, base, list) {
  const cs = getComputedStyle(el);
  const r = rel(el, base);
  const size = px(cs.fontSize);
  let lh = cs.lineHeight;
  lh = lh === "normal" ? size * 1.2 : (lh.endsWith("px") ? px(lh) : px(lh) * size);
  const left = px(cs.borderLeftWidth) + (list ? 0 : px(cs.paddingLeft));
  const top = px(cs.borderTopWidth) + px(cs.paddingTop);
  const right = px(cs.borderRightWidth) + px(cs.paddingRight);
  const bottom = px(cs.borderBottomWidth) + px(cs.paddingBottom);
  const upper = cs.textTransform === "uppercase";
  const item = { type: "text", tag: el.tagName.toLowerCase(), x: r.x + left, y: r.y + top, w: r.w - left - right, h: r.h - top - bottom,
    font: cs.fontFamily.split(",")[0].replace(/["']/g, "").trim(), size, lh,
    ls: cs.letterSpacing === "normal" ? 0 : px(cs.letterSpacing), align: cs.textAlign };
  if (list) {
    item.bullet = cs.listStyleType === "decimal" ? "decimal" : "disc";
    item.indent = px(cs.paddingLeft);
    item.paras = [...el.children].filter(li => li.tagName === "LI").map(li => runs(li, upper).flat());
  } else {
    item.paras = runs(el, upper);
  }
  return item;
}
function measure() {
  const slides = [];
  for (const sec of document.querySelectorAll("section")) {
    const base = sec.getBoundingClientRect();
    const items = [];
    let titled = false;
    (function walk(el) {
      for (const ch of el.children) {
        const tag = ch.tagName;
        if (tag === "ASIDE") continue;
        const cs = getComputedStyle(ch);
        if (cs.display === "none") continue;
        const r = rel(ch, base);
        if (["DIV", "P", "H1", "H2", "H3", "UL", "OL"].includes(tag)) {
          const fill = col(cs.backgroundColor);
          const bw = px(cs.borderTopWidth) || px(cs.borderLeftWidth);
          const bc = bw ? col(cs.borderTopColor) || col(cs.borderLeftColor) : null;
          if (fill || bc) items.push({ type: "box", ...r, fill, bw: bc ? bw : 0, bc, radius: px(cs.borderTopLeftRadius) });
        }
        if (tag === "X-SHAPE") { items.push({ type: "shape", kind: ch.getAttribute("kind"), ...r, fill: col(cs.backgroundColor) }); continue; }
        if (tag === "X-ICON") { items.push({ type: "icon", name: ch.getAttribute("name"), color: col(cs.color), ...r }); continue; }
        if (tag === "HR") { items.push({ type: "line", x1: r.x, y1: r.y, x2: r.x + r.w, y2: r.y, w: px(cs.borderTopWidth) || 1, color: col(cs.borderTopColor) }); continue; }
        if (tag === "X-CONNECTOR") {
          const host = ch.offsetParent && ch.offsetParent !== document.body ? rel(ch.offsetParent, base) : { x: 0, y: 0 };
          const n = k => px(ch.getAttribute(k));
          items.push({ type: "connector", x1: host.x + n("x1"), y1: host.y + n("y1"), x2: host.x + n("x2"), y2: host.y + n("y2"),
            route: ch.getAttribute("route") || "straight", head: ch.getAttribute("head") || "end",
            w: px(ch.style.borderWidth) || 2, color: col(cs.color) });
          continue;
        }
        if (["H1", "H2", "H3", "P"].includes(tag)) {
          const it = textItem(ch, base, false);
          if (!titled && (tag === "H1" || tag === "H2")) { it.title = true; titled = true; }
          items.push(it);
          continue;
        }
        if (tag === "UL" || tag === "OL") { items.push(textItem(ch, base, true)); continue; }
        walk(ch);
      }
    })(sec);
    const aside = sec.querySelector(":scope > aside");
    slides.push({ id: sec.id, bg: col(getComputedStyle(sec).backgroundColor) || "FFFFFF", items,
      notes: aside ? aside.textContent.trim() : "" });
  }
  const json = JSON.stringify(slides);
  document.getElementById("out").textContent = btoa(unescape(encodeURIComponent(json)));
}
document.fonts.ready.then(() => setTimeout(measure, 50));
"""


def browser():
    for b in BROWSERS:
        if Path(b).exists():
            return b
    sys.exit("Google Chrome or Microsoft Edge is needed to lay out the slides.")


def run_browser(args, tmp):
    cmd = [browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={tmp / 'profile'}"] + args
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)


def font_faces():
    rules = []
    for family, style, weight, name in FONT_FILES:
        data = base64.b64encode((ROOT / "fonts" / name).read_bytes()).decode()
        rules.append(f'@font-face {{ font-family: "{family}"; font-style: {style}; font-weight: {weight}; '
                     f'src: url(data:font/ttf;base64,{data}) format("truetype"); }}')
    return "\n".join(rules)


def measure(week, tmp):
    src = ROOT / "deck-source" / f"week-{week:02d}" / "project"
    deck = json.loads((src / "deck.json").read_text(encoding="utf-8"))
    sections = [(src / "slides" / f"{sid}.html").read_text(encoding="utf-8") for sid in deck["order"]
                if (src / "slides" / f"{sid}.html").exists()]
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_faces()}\n{HARNESS_CSS}</style></head>"
            f"<body>{''.join(sections)}<pre id='out'></pre><script>{MEASURE_JS}</script></body></html>")
    harness = tmp / "harness.html"
    harness.write_text(page, encoding="utf-8")
    result = run_browser(["--window-size=1920,1080", "--virtual-time-budget=20000", "--dump-dom", harness.as_uri()], tmp)
    found = re.search(r"<pre id=\"out\">([A-Za-z0-9+/=\s]+)</pre>", result.stdout)
    if not found or not found.group(1).strip():
        sys.exit("The browser did not finish laying out the slides.\n" + result.stderr[-2000:])
    return deck, json.loads(base64.b64decode(found.group(1)).decode("utf-8"))


def render_icons(slides, tmp):
    wanted = sorted({(i["name"], i["color"]) for s in slides for i in s["items"] if i["type"] == "icon"})
    if not wanted:
        return {}
    cell = 192
    cells = []
    for name, color in wanted:
        body = ICONS.get(name, '<circle cx="12" cy="12" r="9"/>')
        cells.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{cell}" height="{cell}" viewBox="0 0 24 24" fill="none" '
                     f'stroke="#{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')
    page = ("<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block;float:left}"
            f"</style></head><body>{''.join(cells)}</body></html>")
    (tmp / "icons.html").write_text(page, encoding="utf-8")
    shot = tmp / "icons.png"
    run_browser([f"--window-size={cell * len(wanted)},{cell}", "--default-background-color=00000000",
                 f"--screenshot={shot}", (tmp / "icons.html").as_uri()], tmp)
    sheet = Image.open(shot).convert("RGBA")
    icons = {}
    for k, key in enumerate(wanted):
        buf = io.BytesIO()
        sheet.crop((k * cell, 0, (k + 1) * cell, cell)).save(buf, "PNG")
        icons[key] = buf.getvalue()
    return icons


def emu(v):
    return Emu(int(round(v * PX)))


def set_fonts(rpr, family):
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rpr.find(qn(tag))
        if el is None:
            el = etree.SubElement(rpr, qn(tag))
        el.set("typeface", family)


def fill_text(tf, item):
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    body = tf._txBody.find(qn("a:bodyPr"))
    for old in body.findall(qn("a:normAutofit")) + body.findall(qn("a:spAutoFit")) + body.findall(qn("a:noAutofit")):
        body.remove(old)
    etree.SubElement(body, qn("a:normAutofit"))
    align = {"center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT, "justify": PP_ALIGN.JUSTIFY}.get(item["align"], PP_ALIGN.LEFT)
    paras = item["paras"] or [[]]
    for n, runs in enumerate(paras):
        p = tf.paragraphs[0] if n == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = Pt(item["lh"] * 0.5)
        ppr = p._p.get_or_add_pPr()
        if item.get("bullet"):
            hang = min(item["indent"], item["size"] * 0.9)
            ppr.set("marL", str(int(item["indent"] * PX)))
            ppr.set("indent", str(-int(hang * PX)))
            if item["bullet"] == "decimal":
                etree.SubElement(ppr, qn("a:buAutoNum")).set("type", "arabicPeriod")
            else:
                etree.SubElement(ppr, qn("a:buFont")).set("typeface", "Arial")
                etree.SubElement(ppr, qn("a:buChar")).set("char", "•")
        else:
            ppr.set("marL", "0")
            ppr.set("indent", "0")
            etree.SubElement(ppr, qn("a:buNone"))
        for r in runs:
            run = p.add_run()
            run.text = r["text"]
            f = run.font
            f.size = Pt(item["size"] * 0.5)
            f.bold = r["bold"]
            f.italic = r["italic"]
            if r["color"]:
                f.color.rgb = RGBColor.from_string(r["color"])
            rpr = run._r.get_or_add_rPr()
            set_fonts(rpr, item["font"])
            if item["ls"]:
                rpr.set("spc", str(int(round(item["ls"] * 50))))
            if r["href"]:
                run.hyperlink.address = r["href"]


def place_text(slide, item, title_shape):
    x, w = item["x"], item["w"]
    grow = w * 0.03  # PowerPoint wraps a little earlier than the browser
    if item["align"] == "center":
        x -= grow / 2
    elif item["align"] == "right":
        x -= grow
    w = min(w + grow, 1920 - max(x, 0))
    x = max(x, 0)
    if item.get("title") and title_shape is not None:
        shape = title_shape
        shape.left, shape.top, shape.width, shape.height = emu(x), emu(item["y"]), emu(w), emu(item["h"])
        tree = shape._element.getparent()
        tree.remove(shape._element)
        tree.append(shape._element)
    else:
        shape = slide.shapes.add_textbox(emu(x), emu(item["y"]), emu(w), emu(item["h"]))
    fill_text(shape.text_frame, item)
    return shape


def add_box(slide, item):
    inset = item["bw"] / 2
    x, y, w, h = item["x"] + inset, item["y"] + inset, item["w"] - 2 * inset, item["h"] - 2 * inset
    radius = min(item["radius"] / max(min(w, h), 1), 0.5)
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius > 0 else MSO_SHAPE.RECTANGLE,
                                   emu(x), emu(y), emu(w), emu(h))
    if radius > 0:
        shape.adjustments[0] = radius
    if item["fill"]:
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(item["fill"])
    else:
        shape.fill.background()
    if item["bc"]:
        shape.line.color.rgb = RGBColor.from_string(item["bc"])
        shape.line.width = emu(item["bw"])
    else:
        shape.line.fill.background()
    shape.shadow.inherit = False


def add_shape(slide, item):
    kind = {"arrow-right": MSO_SHAPE.RIGHT_ARROW, "arrow-left": MSO_SHAPE.LEFT_ARROW, "arrow-up": MSO_SHAPE.UP_ARROW,
            "arrow-down": MSO_SHAPE.DOWN_ARROW, "diamond": MSO_SHAPE.DIAMOND, "ellipse": MSO_SHAPE.OVAL,
            "rounded": MSO_SHAPE.ROUNDED_RECTANGLE}.get(item["kind"], MSO_SHAPE.RECTANGLE)
    shape = slide.shapes.add_shape(kind, emu(item["x"]), emu(item["y"]), emu(item["w"]), emu(item["h"]))
    if item["fill"]:
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(item["fill"])
    shape.line.fill.background()
    shape.shadow.inherit = False


def add_line(slide, x1, y1, x2, y2, width, color, arrow=False):
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, emu(x1), emu(y1), emu(x2), emu(y2))
    line.line.width = emu(width)
    if color:
        line.line.color.rgb = RGBColor.from_string(color)
    if arrow:
        ln = line.line._get_or_add_ln()
        etree.SubElement(ln, qn("a:tailEnd"), type="triangle", w="med", len="med")


def add_connector(slide, item):
    x1, y1, x2, y2 = item["x1"], item["y1"], item["x2"], item["y2"]
    if item["route"] == "vh":
        points = [(x1, y1), (x1, y2), (x2, y2)]
    elif item["route"] == "hv":
        points = [(x1, y1), (x2, y1), (x2, y2)]
    elif item["route"] == "elbow":
        mid = (x1 + x2) / 2
        points = [(x1, y1), (mid, y1), (mid, y2), (x2, y2)]
    else:
        points = [(x1, y1), (x2, y2)]
    segments = [(a, b) for a, b in zip(points, points[1:]) if a != b]
    for k, (a, b) in enumerate(segments):
        add_line(slide, *a, *b, item["w"], item["color"], arrow=item["head"] != "none" and k == len(segments) - 1)


def build(week, out):
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        deck, slides = measure(week, tmp)
        icons = render_icons(slides, tmp)

    prs = Presentation()
    prs.slide_width, prs.slide_height = emu(1920), emu(1080)
    layout = prs.slide_layouts[5]  # "Title Only", so every slide keeps a real title
    for s in slides:
        slide = prs.slides.add_slide(layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = RGBColor.from_string(s["bg"])
        title = slide.shapes.title
        used_title = False
        for item in s["items"]:
            kind = item["type"]
            if kind == "box":
                add_box(slide, item)
            elif kind == "shape":
                add_shape(slide, item)
            elif kind == "icon":
                pic = slide.shapes.add_picture(io.BytesIO(icons[(item["name"], item["color"])]),
                                               emu(item["x"]), emu(item["y"]), emu(item["w"]), emu(item["h"]))
                pic._element.nvPicPr.cNvPr.set("descr", item["name"])
            elif kind == "line":
                add_line(slide, item["x1"], item["y1"], item["x2"], item["y2"], item["w"], item["color"])
            elif kind == "connector":
                add_connector(slide, item)
            elif kind == "text":
                place_text(slide, item, title if item.get("title") else None)
                used_title = used_title or bool(item.get("title"))
        if not used_title:
            title._element.getparent().remove(title._element)
        if s["notes"]:
            slide.notes_slide.notes_text_frame.text = s["notes"]
    prs.core_properties.title = deck["title"]
    prs.save(out)
    print(f"Wrote {out} ({len(slides)} slides)")


if __name__ == "__main__":
    week = int(sys.argv[1])
    folder = next(ROOT.glob(f"Week-{week:02d}_*"))
    build(week, Path(sys.argv[2]) if len(sys.argv) > 2 else folder / f"Week-{week:02d}-slides.pptx")
