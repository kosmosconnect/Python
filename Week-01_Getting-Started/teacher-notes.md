# Python Week 1 – Getting Started: teacher notes

## Welcome and the 8-week roadmap

### Slide 1: Getting started with Python

Welcome slide. Introduce yourself and the course: 8 weeks, 24 classes, about 1 hour each. Week 1 covers three classes: (1) what programming is and your first program, (2) variables, data types and input, (3) operators. Tell the student that every class ends with hands-on practice, so they should have a laptop (or at least a phone with Pydroid 3) ready from Class 1.

### Slide 2: Your 8-week Python roadmap

Spend about 5 minutes here. Show the whole journey so the student knows where each topic fits. Phase 1 builds logic (the base for every lab program). Phase 2 is about storing data. Phase 3 is about organising code and saving data to files. Phase 4 is object-oriented programming plus exam and viva preparation. Ask: "Have you coded before, in C, Scratch or a school computer class?" Adjust the pace to the answer. Point out the rhythm every class follows: learn the idea, see the code, try it yourself, recap.

## Class 1 — what programming is, setting up Python, first program

### Slide 3: Hello, Python!

Class 1 opener. Read the four goals aloud and tell the student: "By the end of this hour you will have written and run your first Python program." Suggested timing: concepts 20 min, setup 15 min, first program and rules 15 min, practice 10 min.

### Slide 4: What is a program?

Start with the recipe analogy before showing any code. Ask: "What happens if I swap steps 1 and 3?" (You cook dry noodles: the order matters.) "What if I just write 'make Maggi'?" (A computer would not understand: every step must be spelled out.) Key message: computers are fast but literal. A program is a recipe the computer follows exactly. Bugs come from unclear or wrong steps, not from the computer "thinking wrongly".

### Slide 5: Why learn Python first?

Many first-year students also meet C in their course, so this comparison helps. Point at the C version: header file, main function, semicolons, return value. All of that is needed just to print one line. Python needs one line. Do not teach C here; just show that Python lets you focus on the logic instead of the punctuation. Mention real-world use: Instagram's backend, Netflix's data tools and NASA's scientific scripts all use Python, and almost every AI/ML library is written for it.

### Slide 6: How Python runs your code

Viva favourite: "Is Python compiled or interpreted?" Simple answer for a first-year: Python is an interpreted language. The interpreter executes code line by line, so an error on line 5 means lines 1 to 4 already ran. (Advanced note, only if asked: Python first converts code to bytecode, then the Python Virtual Machine runs it.) Compare with C: a compiler translates the whole program first, then you run it. Analogy: compiler = translating a whole book before publishing; interpreter = a live translator at a press conference.

### Slide 7: Set up Python: pick one way

Do the installation live, together. The most common Windows problem: forgetting to tick "Add python.exe to PATH". If python --version says "not recognized", re-run the installer, choose Modify, and enable the PATH option (or try "py --version"). IDLE comes with Python and is perfect for beginners. VS Code with the Python extension is better for longer programs. If the laptop is not ready, use W3Schools Try it Yourself or Google Colab for today and install later. A phone is fine for practice but not for the full course.

### Slide 8: Hello, World!

Type this program live, line by line, and run it after each line so the student sees the effect. Ask the student to predict line 4 first: will it print "10 + 5" or 15? (15, because there are no quotes, so Python calculates.) Then ask: what would print("10 + 5") show? (The text 10 + 5.) Show one more trick verbally: print("Hi", end=" ") keeps the next print on the same line. Vocabulary to introduce: function (print), string (text in quotes), argument (what goes inside the brackets).

### Slide 9: Four golden rules of Python

Make errors on purpose, live, and read the messages together. This removes the fear of red text. Rule 1: Python is case-sensitive, so Print is an unknown name (NameError). Rule 2: a string must open and close with the same quote type (SyntaxError). Rule 3: spaces at the start of a line have meaning in Python; we will use them for if and loops next week. For now, never indent without a reason (IndentationError). Rule 4: comments start with # and are notes for humans. Viva question: "What is a comment and why do we use it?"

### Slide 10: Your turn: 10 minutes

Let the student work alone first; help only after 3 to 4 minutes. Answers. Task 1: three print() lines. Task 2: print("*"), print("* *"), print("* * *"). Bonus: print("*\n* *\n* * *") in one line using \n (new line). Task 3: Print must be lowercase print, and the closing quote is missing: print("Hello World"). Homework: read the four W3Schools pages and use the "Try it Yourself" button on each example.

## Class 2 — variables, data types, input and type casting

### Slide 11: Variables & data types

Quick warm-up (3 minutes): ask the student to write, from memory, a program that prints their name and 2 + 2. Then introduce today's problem: "How does a program remember things, like your marks, to use later?" That is what variables are for.

### Slide 12: A variable is a labelled box

Draw three boxes on paper or the whiteboard if possible. Key points: (1) A variable is a name that points to a value. (2) The = sign is assignment: the right side is worked out first, then stored in the name on the left. So age = age + 1 makes sense in Python even though it is "wrong" in maths. (3) Putting a new value in the box replaces the old one. Ask: after age = 19, what does print(age) show? (19, the 18 is gone.) Common mistake: writing 18 = age (the name must be on the left).

### Slide 13: Good names, bad names

The three rules to remember: (1) only letters, digits and underscore; (2) cannot start with a digit; (3) cannot be a keyword. Show the keyword list live: import keyword, then print(keyword.kwlist). There are about 35 keywords, such as if, else, for, while, class, def, True, False, None. Viva question: "Is Python case-sensitive?" Yes: Marks and marks are two different variables. Encourage snake_case (words joined with underscores); it is the Python style convention (PEP 8).

### Slide 14: Four basic types of data

Use real-life examples so the four types stick. Quick quiz: what type is each of these? 25 (int), 25.0 (float), "25" (str, because of the quotes), True (bool). Point out that True and False start with a capital letter; true without a capital is a NameError. You do not have to declare types in Python (unlike C's int x;). Python decides the type from the value. This is called dynamic typing, and it is a common viva question.

### Slide 15: Talking to the user with input()

Run greet.py live and let the student type the answers. Stress point 3: input() ALWAYS returns a string. This single fact causes most beginner bugs, which is exactly what the next slide is about. Tip: put a space at the end of the prompt ("Enter your name: ") so the typed text does not stick to the colon. Ask the student to change the program to also ask for their branch and print it.

### Slide 16: The input() trap, and the fix

Show the error first and let the student read it. "concatenate" means joining strings together: Python sees "18" + 1 and cannot join text with a number. Fix: wrap input() in int() for whole numbers or float() for decimals. Read int(input("Age: ")) from the inside out: input() runs first and gives "18", then int() turns it into 18. Extra demos: int("abc") gives ValueError; int("8.5") also gives ValueError (use float first). Viva question: "What is type casting?" Converting a value from one type to another.

### Slide 17: Your turn: 15 minutes

Answers. Task 1: name = input("Name: "); college = input("College: "); print("Welcome", name, "to", college + "!"). Task 2: a = int(input("First: ")); b = int(input("Second: ")); print("Sum =", a + b). If the student forgets int(), 5 and 3 give 53: a perfect teaching moment. Task 3: class 'float' (the / operator always gives a float), 55 (joining two strings), 10. Output-prediction questions like Task 3 are very common in university exams and quizzes, so do one or two every class.

## Class 3 — operators, BODMAS, f-strings and a full program

### Slide 18: Operators & expressions

Warm-up: ask the student to write a program that reads two numbers and prints their sum (last class's Task 2) in under 2 minutes. Today we turn Python into a calculator and learn how it decides whether something is True or False. That is the base for if/else next week.

### Slide 19: Python as a calculator

Open the Python shell (IDLE) and type each example; the shell prints the result instantly, so it works like a calculator. Spend most time on / versus //: 17 / 5 is 3.4 (true division, always a float), 17 // 5 is 3 (floor division: how many whole times 5 fits into 17). Note: in C, 17/5 gives 3, but in Python it gives 3.4. Also: ^ is NOT power in Python (it is bitwise XOR, so 2 ^ 10 gives 8). Exam trick question: what is -17 // 5? Answer -4, because floor always rounds down towards minus infinity.

### Slide 20: // and % in real life

This is the slide that makes // and % click. Act it out: 47 rasagolas, boxes of 6. Fill 7 boxes (42 rasagolas) and 5 are left. That is exactly 47 // 6 and 47 % 6. The % operator appears again and again in lab programs: even/odd, divisibility (n % 3 == 0), leap year, extracting the last digit of a number (n % 10), and digit-sum or reverse-number programs next week. Quick check: what is 1234 % 10? (4, the last digit.) And 1234 // 10? (123, the last digit removed.)

### Slide 21: Comparing and combining

Every comparison produces a bool (True or False): this is how programs make decisions, which is next week's topic. Walk through the example: attendance 80 is at least 75, so True. With and, both parts must be True, but marks 35 is below 40, so False. With or, one True part is enough, so True. The most common beginner bug: writing if x = 5 instead of if x == 5. One = stores, two == compare. Quick quiz: what is not (5 > 3)? (False.) What is 10 != 10? (False.)

### Slide 22: Python follows BODMAS too

Students already know BODMAS from school maths, so connect to it. Cover the answers on the right with your hand (or ask the student to look away) and let them predict each result first. 10 - 4 / 2 gives 8.0, not 8: the division happens first and / always makes a float. Golden advice: when in doubt, add brackets. They make code easier to read and remove any doubt. Exam trick (only if the student is quick): 2 ** 3 ** 2 is 512, because power is worked out right to left. Shortcuts: x += 1 is used constantly in loops next week.

### Slide 23: f-strings: fill in the blanks

Show the "old way" first: print(name, "scored", pct, "%") gives "Priyanka scored 87.4 %" with an extra space, and long decimals can look messy. Then show the f-string version. Analogy: an f-string is like a form with blanks ("Name: ____, Marks: ____") that Python fills in for you. Try variations live: {pct:.1f} gives 87.4, {pct:.0f} gives 87, and {marks + 10} works too, since any expression can go inside the braces. From now on, use f-strings for all output in lab programs; it looks professional.

### Slide 24: Program: simple interest calculator

This is a typical first lab program. Build it step by step with the student: first the three inputs, then the formula, then the output. Explain the IPO model: Input (read p, r, t), Process (si = p * r * t / 100), Output (print the results). Ask the student to label each line of the program as I, P or O. Why float() and not int()? Because the rate can be 7.5. Extension challenge: change it to compound interest: amount = p * (1 + r / 100) ** t. For 50000 at 7.5% for 2 years, the amount is Rs. 57781.25.

### Slide 25: Your turn: four lab-style programs

Do two tasks in class and give the other two as homework. Answers. Task 1: r = float(input("Radius: ")); print(f"Area = {3.14159 * r * r:.2f}"); print(f"Circumference = {2 * 3.14159 * r:.2f}"). Task 2: c = float(input()); f = c * 9 / 5 + 32. Task 3: also show the classic way with a third variable: temp = a; a = b; b = temp. Examiners often ask for both. Task 4: h = s // 3600; rest = s % 3600; m = rest // 60; sec = rest % 60. Ask the student to save all programs in a week-1 folder: they are the start of a lab record.

## Week 1 recap and what comes next

### Slide 26: What you can do now

Five-minute oral quiz to close the week (good viva practice): 1. Is Python compiled or interpreted? 2. What does input() always return? 3. What is the difference between / and //? 4. What does 17 % 5 give? 5. What is the difference between = and ==? 6. Name the four basic data types. 7. Is Python case-sensitive? Check the homework folder at the start of next week.
