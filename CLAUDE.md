# Python course teaching kit

Teaching kit for an 8-week, 24-class Python course for one B.Tech 1st-year student (ITER, SOA University, Bhubaneswar). The repo owner is the teacher. W3Schools Python is the reference textbook. Goal: slides that are easy for a beginner to understand, plus runnable code and notes for the teacher.

## Layout

- `README.md`: weekly plan and deck links. Update its Slides column when a deck is created or finished.
- `Week-NN_<Topic>/code/`: every program shown on that week's slides, runnable, named `classNN_<topic>.py`.
- `Week-NN_<Topic>/solutions/`: answers to the practice slides.
- `Week-NN_<Topic>/teacher-notes.md`: generated from the slides' `<aside>` notes with `python tools/make_notes.py N`. Do not hand-edit.
- `deck-source/week-NN/project/`: source of that week's online Slides artifact (`deck.json` plus `slides/<id>.html`). This folder is the `root` when publishing to that week's artifact.

## Slide decks (claude.ai Slides artifacts)

| Week | Artifact | State |
|------|----------|-------|
| 1 | https://claude.ai/artifact/XPWS2SXfGJycbMLsRo4zR7 | complete, 26 slides |
| 2 | https://claude.ai/artifact/3D9WVoacF9Joc5nCBBHQvc | in progress |

To change a deck, edit files under `deck-source/week-NN/project/` and publish only the changed files to that week's URL with `root` = `deck-source/week-NN`. The teacher may edit slides in the browser; if a publish is refused, re-read the named file from the artifact and redo the edit on it. Weeks 3–8 each get a new deck made from the Slides artifact type.

## Style (keep every deck consistent)

- Fonts: Rubik (text) and JetBrains Mono (code), both from Google Fonts.
- Colours: navy `#1B2A41`, paper `#F7F5EF`, yellow `#F2B33D`, blue `#2A64A3`, body text `#4A5568`, practice tint `#E6EEF7`, callout `#FBEFD5`, orange `#B54708` for user-typed input and "No".
- Type scale: 120 cover, 96 class divider, 64 slide title, 36 lead and h3, 30 body and code, 24 labels and footer.
- Each class: yellow divider slide with goals, then concept and code slides (navy code panel plus output panel), then a tinted "Your turn" practice slide with W3Schools homework links. Each week ends with a navy recap slide.
- Code goes in a `<p>` in JetBrains Mono with `<br>` per line and `&#160;` for indentation; keywords and built-ins `#F2B33D`, strings `#9FD8A8`, comments `#8FA3B8`.
- Every slide has teacher notes in `<aside>`: what to say, common mistakes, answers, viva questions.
- Examples use local context: Bhubaneswar, Cuttack, Puri, rasagola, hostel Maggi; names like Ananya, Subham, Priyanka.

## Status and next steps

- Week 1 (Classes 1–3): done, including its code, solutions and teacher notes.
- Week 2 (Classes 4–6): Class 4 slides done; Class 5 has `c5`, `c5-why`, `c5-while`, `c5-for`. Still to write: `c5-accum`, `c5-digits`, `c5-break`, `c5-try`, `c6` through `c6-try`, and `wrap` (their ids are already in `deck.json` `order`). Then the `Week-02_Decisions-and-Loops` folder (code, solutions, notes).
- Weeks 3–8: follow the topics in the README table.
