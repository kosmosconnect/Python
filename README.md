# Python Programming: 8-week course

One-to-one course for a B.Tech 1st-year student (ITER, SOA University, Bhubaneswar).
24 classes, 3 per week (squeeze into 2 per week by moving the practice slide to homework).
Reference textbook: [W3Schools Python Tutorial](https://www.w3schools.com/python/).

## Weekly plan and slide decks

| Week | Classes | Topics | Slides |
|------|---------|--------|--------|
| 1 | 1–3 | What a program is, setup, print, variables, data types, input, casting, operators, f-strings | [Week 1 deck](https://claude.ai/artifact/XPWS2SXfGJycbMLsRo4zR7) |
| 2 | 4–6 | if / elif / else, while and for loops, range, break/continue, nested loops and patterns | [Week 2 deck](https://claude.ai/artifact/3D9WVoacF9Joc5nCBBHQvc) |
| 3 | 7–9 | Strings, slicing, string methods, lists | [Week 3 deck](https://claude.ai/artifact/4Nr3YYsXDky9QTbHxCo5CK) |
| 4 | 10–12 | 2D lists, comprehensions, tuples, sets, dictionaries, Mini-project 1 | [Week 4 deck](https://claude.ai/artifact/BfEUvTiMxf5czDCZwSsj5p) |
| 5 | 13–15 | Functions, scope, lambda, recursion | [Week 5 deck](https://claude.ai/artifact/C4K3Jtwx6SnFdZaevQbbTe) |
| 6 | 16–18 | Modules, file handling, CSV, Mini-project 2 | [Week 6 deck](https://claude.ai/artifact/PAf5yhFnixkAumUkhSnbFd) |
| 7 | 19–21 | Exceptions, classes and objects, inheritance | [Week 7 deck](https://claude.ai/artifact/Sr5Lfg8H3dYLBC1LurWSfe) |
| 8 | 22–24 | Capstone project, exam revision, mock viva | [Week 8 deck](https://claude.ai/artifact/4KZu1r4muw2SU1WLhirShB) |

The decks open in the browser. Use **Present** to teach, and **Share › Export** to download a PDF or PowerPoint copy.
The links are private until you share them from the Share menu.

## What is in each week's folder

| Folder | Week |
|--------|------|
| `Week-01_Getting-Started/` | 1 |
| `Week-02_Decisions-and-Loops/` | 2 |
| `Week-03_Strings-and-Lists/` | 3 |
| `Week-04_Collections/` | 4 (Mini-project 1: `class12_records.py`) |
| `Week-05_Functions/` | 5 |
| `Week-06_Modules-and-Files/` | 6 (Mini-project 2: `class18_expenses.py`) |
| `Week-07_Exceptions-and-OOP/` | 7 |
| `Week-08_Capstone-and-Revision/` | 8 (Capstone: `class22_library.py`) |

Each one has:

```
code/              every program shown on the slides, ready to run live in class
solutions/         answers to the practice slides (keep until the student has tried)
teacher-notes.md   what to say on each slide, common mistakes, viva questions
Week-NN-slides.pptx   PowerPoint copy of that week's deck, for teaching offline
```

Run any program from its own folder, for example:

```
cd Week-01_Getting-Started/code
python class01_hello.py
```

Programs that read or write files (Weeks 6 and 8) create them in the folder you run them from.

## Other folders

- `fonts/` holds the two fonts the slides use, Rubik and JetBrains Mono (free, OFL licence). Install them on any laptop where you open the PowerPoint copies: select the four `.ttf` files, right-click, **Install**. Without them PowerPoint swaps in other fonts and code lines can lose their alignment.
- `deck-source/` holds the source files of the online slides. Do not edit them by hand; ask Claude to change a slide and it will update the online deck too.
- `tools/make_notes.py` rebuilds a week's `teacher-notes.md` from the slides: `python tools/make_notes.py 1`
- `tools/build_pptx.py` builds a week's PowerPoint copy from `deck-source/` when Share › Export is not available (it needs Chrome or Edge): `python tools/build_pptx.py 1`. The Week 1 copy was made this way.
