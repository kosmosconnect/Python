# Python Week 8 – Capstone, Revision & Viva: teacher notes

## Week 8 cover

### Slide 1: Capstone, revision and mock viva

The final week. Classes: (22) the capstone project, a Library Management System that uses classes, files, exceptions, dictionaries and a menu; (23) exam revision: output questions, bubble sort, binary search and common mistakes; (24) a full mock viva and lab-exam tips. If the student preferred the ATM project, the same structure works: Account class, a Bank that holds accounts, save to CSV, menu.

## Class 22 — capstone: library management system

### Slide 2: Capstone project

This is the student's showcase program: something to show in the lab, to seniors, or in an internship interview. Plan it on paper first (15 minutes): what objects exist, what each one knows, what each one can do. Then build in four steps, running after each. It may take two sessions; that is fine. The full program is in code/class22_library.py.

### Slide 3: Two classes, one menu, one file

Draw a simple diagram: a Library box holding many Book boxes, the menu talking to the Library, and the Library reading and writing books.csv. Point out which week each part comes from: classes (7), dictionary of books by id (4), CSV (6), exceptions (7), menu loop (4), functions (5). Ask the student what else a real library needs (members, due dates, fines): those become extensions.

### Slide 4: The Book class

Keep the Book class small: it just holds data and prints itself. The bid (book id) is a short string like "B1"; using a string keeps the CSV simple. An empty string means the book is on the shelf. Test it alone: b = Book("B1", "Wings of Fire", "A. P. J. Abdul Kalam"); print(b).

### Slide 5: The Library class: issue and return

The methods do not print error messages themselves; they raise, and the menu decides what to show (Week 7). The method is called give_back because return is a Python keyword. Add list_all (loop and print each book) and search (title.lower() contains the word) yourself or from the code folder. Test: lib = Library(); lib.add(Book(...)); lib.issue("B1", "Ananya"); lib.issue("B1", "Subham") should raise.

### Slide 6: Saving and loading the books

Both are methods of Library, so they are indented inside the class in the real file. Mode "w" is right here because we write the complete, current list every time. Book(*row) is the unpacking star: Book(*["B1", "Wings", "Kalam", ""]) is the same as Book("B1", "Wings", "Kalam", ""). Run the program, issue a book, quit, run again: the book is still issued.

### Slide 7: The menu that ties it together

Walk through a full session: list, issue B2 to Ananya, try to issue B2 again (Already issued), return B2, type a wrong id (No book with that id), exit and restart to show the data was saved. The complete program in the code folder also has Add and Search choices and starts with three sample books (Wings of Fire, Godan and Python Basics) when no file exists.

### Slide 8: Your turn: extend the capstone

Answers for tasks 1 and 2 are built into code/class22_library.py (choices 4 and 5); tasks 3 and 4 are open-ended and are good for the student's own portfolio. Hints. Task 3: add an issued_on attribute set to str(date.today()), save it as a fifth CSV column, and compare (date.today() - date.fromisoformat(b.issued_on)).days > 14. Task 4: Account from Week 7 plus a Bank class with a dictionary of accounts by account number.

## Class 23 — exam revision: programs, outputs, sorting, searching, mistakes

### Slide 9: Exam revision

Revision class. Ask the student to bring a list of topics that still feel weak and spend extra time there. Many first-year exams have three kinds of questions: write a program, predict the output of given code, and explain a concept. This class covers all three, plus the two algorithms (bubble sort, binary search) that often appear in theory papers.

### Slide 10: Can you write these from memory?

Use this as a checklist: the student ticks each program they can write without looking, in under 5 minutes. Anything not ticked goes on a revision list. The code for every one is already in the week folders; the solutions folders have the practice versions. Suggest writing three programs a day on paper, the way the exam requires, then typing and running them to check.

### Slide 11: What does each line print?

Do this as a quiz: hide the answers (or read only the left column aloud). Explanations: 7 // 2 is 3 and 7 % 2 is 1; string repetition then joining; range(2, 9, 3) is 2, 5, 8 (stop excluded); slicing [1:4] takes indexes 1, 2, 3; a set removes the repeated 2; the empty string is False but any non-empty string, even "0", is True; / always gives a float. Make up five more of your own in the same style.

### Slide 12: Bubble sort: the classic sorting algorithm

Act it out with 5 cards or coins. Round 1 compares 64-25 (swap), 64-12 (swap), 64-22 (swap), 64-11 (swap): 64 is now last. Round 2 needs only 3 comparisons, and so on. The swap line is the tuple trick from Week 1. In real code you would use sort(), but exams love this algorithm. Viva: how many comparisons in the worst case? (About n squared over 2: it is a slow, O(n^2) algorithm.) Improvement: stop early if a whole round makes no swaps.

### Slide 13: Binary search: halve the list each time

Trace finding 25: low 0, high 4, mid 2 (22 is smaller, so low = 3); low 3, high 4, mid 3 (25 found, return 3). Linear search checks items one by one (up to n checks); binary search halves the range each time, so 1000 items need at most about 10 checks. Viva: why must the list be sorted? (Otherwise we cannot know which half to throw away.) A recursive version is also common in exams: same idea, calling itself on one half.

### Slide 14: Mistakes that cost marks

Ask the student to recall one bug of their own for each card from the past 8 weeks: real memories stick. Other frequent mistakes worth mentioning: wrong indentation (code accidentally inside or outside a loop), forgetting self in methods, using "w" instead of "a" and wiping a file, starting an accumulator at 0 for a product, and changing a list while looping over it.

### Slide 15: Your turn: revision practice

Answers are in solutions/class23_practice.py. Hints. Task 2: for i in range(n): find the index of the smallest item from i to the end, then swap it with nums[i]. Task 3: add a counter to each search loop; for the 5-item list, linear needs 5 checks and binary needs 3; for 1000 items it is 1000 against 10. The W3Schools exercises and quiz are good timed practice before the exam.

## Class 24 — mock viva, lab-exam tips and what next

### Slide 16: Mock viva

Run this class as a real viva: the student stands or sits across the table, you ask, they answer out loud in one or two sentences, then you show the card. Score each answer (clear, partly, not yet) and revise the weak ones together. Short, confident, correct answers with an example score best.

### Slide 17: Basics

Ask each question before revealing the card. Follow-up questions examiners like: "Is Python case-sensitive?" (Yes.) "What is a variable?" (A name that refers to a value.) "What does type() do?" "What is the difference between / and //?" "What are Python's key features?" (Simple syntax, interpreted, dynamically typed, huge library, cross-platform.)

### Slide 18: Functions and collections

Follow-ups: "Local vs global variable?" "What does return do if it is missing?" (Returns None.) "Difference between append and extend?" (append adds one item; extend adds each item of another list.) "What is a list comprehension?" "How is a set different from a list?" (No order, no duplicates.) Ask the student to give a one-line code example for each answer.

### Slide 19: Files, errors and OOP

Follow-ups: "What is __init__?" (The constructor, runs when an object is created.) "Name the four pillars of OOP." "What is inheritance? Give an example." (Student(Person).) "What does finally do?" "Why use with when opening files?" (Closes the file automatically.) "What is a module? Name three." (math, random, datetime.) End the mock viva with the student's own capstone: examiners often ask you to explain your project.

### Slide 20: In the lab exam

Most marks are lost by rushing, not by not knowing. Write the algorithm or flowchart if the exam asks for it: it often carries separate marks. Keep the output friendly: prompts like "Enter a number: " and results with labels. If stuck, write a simpler version that works, then improve it: a working partial program scores better than a broken complete one. Save often.

### Slide 21: Where to go after this course

Encourage the student to pick ONE direction for the next semester rather than everything at once. Data analysis with pandas is the most useful next step for most engineering branches. Suggest putting the capstone and mini-projects on GitHub as a first portfolio. Congratulate the student: 24 classes, 3 projects, and a solid base in programming.

## Course complete

### Slide 22: Course complete!

Final class wrap-up. Ask the student what they enjoyed most and what still feels hard, and give them a short plan for the weeks before the exam (two revision programs a day from the must-know list). Share the course folder and decks with the student (Share menu) so they can revise from them. Well done to both of you.
