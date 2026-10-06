# Python course teaching kit

Teaching kit for an 8-week, 24-class Python course for one B.Tech 1st-year student (ITER, SOA University, Bhubaneswar). The repo owner is the teacher. W3Schools Python is the reference textbook. Goal: slides that are easy for a beginner to understand, plus runnable code and notes for the teacher.

## Layout

- `README.md`: weekly plan and deck links. Update its Slides column when a deck is created or finished.
- `Week-NN_<Topic>/code/`: every program shown on that week's slides, runnable, named `classNN_<topic>.py`.
- `Week-NN_<Topic>/solutions/`: answers to the practice slides.
- `Week-NN_<Topic>/teacher-notes.md`: generated from the slides' `<aside>` notes with `python tools/make_notes.py N`. Do not hand-edit.
- `Week-NN_<Topic>/Week-NN-slides.pptx`: PowerPoint export of that week's online deck (the teacher exports it from Share › Export). Re-export after changing a deck.
- `deck-source/week-NN/project/`: source of that week's online Slides artifact (`deck.json` plus `slides/<id>.html`). This folder is the `root` when publishing to that week's artifact.

## Slide decks (claude.ai Slides artifacts)

| Week | Artifact | State |
|------|----------|-------|
| 1 | https://claude.ai/artifact/XPWS2SXfGJycbMLsRo4zR7 | complete, 26 slides |
| 2 | https://claude.ai/artifact/3D9WVoacF9Joc5nCBBHQvc | complete, 26 slides |
| 3 | https://claude.ai/artifact/4Nr3YYsXDky9QTbHxCo5CK | complete, 23 slides |
| 4 | https://claude.ai/artifact/BfEUvTiMxf5czDCZwSsj5p | complete, 23 slides |
| 5 | https://claude.ai/artifact/C4K3Jtwx6SnFdZaevQbbTe | complete, 23 slides |
| 6 | https://claude.ai/artifact/PAf5yhFnixkAumUkhSnbFd | complete, 22 slides |
| 7 | https://claude.ai/artifact/Sr5Lfg8H3dYLBC1LurWSfe | complete, 23 slides |
| 8 | https://claude.ai/artifact/4KZu1r4muw2SU1WLhirShB | complete, 22 slides |

To change a deck, edit files under `deck-source/week-NN/project/` and publish only the changed files to that week's URL with `root` = `deck-source/week-NN`. The teacher may edit slides in the browser; if a publish is refused, re-read the named file from the artifact and redo the edit on it.

## Style (keep every deck consistent)

- Fonts: Rubik (text) and JetBrains Mono (code), both from Google Fonts.
- Colours: navy `#1B2A41`, paper `#F7F5EF`, yellow `#F2B33D`, blue `#2A64A3`, body text `#4A5568`, practice tint `#E6EEF7`, callout `#FBEFD5`, orange `#B54708` for user-typed input and "No".
- Type scale: 120 cover, 96 class divider, 64 slide title, 36 lead and h3, 30 body and code, 24 labels and footer.
- Each class: yellow divider slide with goals, then concept and code slides (navy code panel plus output panel), then a tinted "Your turn" practice slide with W3Schools homework links. Each week ends with a navy recap slide.
- Code goes in a `<p>` in JetBrains Mono with `<br>` per line and `&#160;` for indentation; keywords and built-ins `#F2B33D`, strings `#9FD8A8`, comments `#8FA3B8`.
- Every slide has teacher notes in `<aside>`: what to say, common mistakes, answers, viva questions.
- Examples use local context: Bhubaneswar, Cuttack, Puri, rasagola, hostel Maggi; names like Ananya, Subham, Priyanka.

## Status and next steps

- All 8 weeks are complete: slides, `code/`, `solutions/` and `teacher-notes.md` for every class. Every program has been run and its output matches the slides.
- Mini-projects: Week 4 `class12_records.py` (rebuilt with functions in Week 5 `class14_records_functions.py`), Week 6 `class18_expenses.py`. Capstone: Week 8 `class22_library.py`.
- Weeks 2–8 slides were generated with a consistent set of layouts (code + output panel, card rows, two-column tables, practice, recap). When editing, keep the same markup patterns and the 24px minimum text size.
- Possible next steps: match topics to the student's official ITER lab list if the teacher shares it; add a printable question bank.
