# Python Week 4 – Collections & Mini-project 1: teacher notes

## Week 4 cover

### Slide 1: Collections and Mini-project 1

Week 4 finishes the data structures and ends with the first mini-project. Classes: (10) 2D lists and list comprehensions; (11) tuples, sets and dictionaries; (12) Mini-project 1, a student record manager that uses everything so far. Check the Week 3 homework first, especially the list practice: the mini-project depends on lists and loops being comfortable.

## Class 10 — 2D lists, matrices and list comprehensions

### Slide 2: Tables and shortcuts

Warm-up: write the largest-without-max program from memory. Then ask how to store marks of 3 students in 3 subjects: the answer is a table, which in Python is a list of lists. Matrix programs (addition, transpose, diagonal sum) are very common lab exercises, and the student meets matrices in Mathematics too.

### Slide 3: A table is a list of rows

Draw the 3 by 3 grid on paper with row numbers 0 to 2 down the side and column numbers 0 to 2 across the top. m[1] is the whole second row [4, 5, 6]; m[1][2] is the third item of that row, 6. Ask: how do you get 7? (m[2][0].) And the centre? (m[1][1].) Writing the list on three lines is optional, but it makes the table shape visible. Same as a 2D array in C, int m[3][3], but without declaring the size.

### Slide 4: Visiting every cell

Connect this to Week 2: nested loops again, but now they walk through stored data instead of printing stars. The index version is also important for exams: for i in range(len(m)): for j in range(len(m[i])): print(m[i][j]). Use the index version whenever you need the position, for example the diagonal: m[i][i] for i in range(3) gives 1, 5, 9. Ask the student to change the program to print column sums instead (harder: loop over j outside and i inside).

### Slide 5: Adding two matrices

Do the addition by hand first: add matching cells. Then trace i = 0: j = 0 gives 6, j = 1 gives 8, so row [6, 8] goes into C. Transpose (rows become columns) uses the same loops with T[j][i] = m[i][j], or row.append(m[j][i]) when building row i. Matrix multiplication is a three-loop program: show it only if the student's lab list includes it. Common bug: creating row = [] outside the outer loop, which glues all rows together.

### Slide 6: Building a list in one line

A list comprehension is just the append loop squeezed into one line. Write the long version first, then move the pieces: the expression (x * x) goes to the front, the for part follows. Both give the same list. Use comprehensions when they are easy to read; when the logic gets long, the normal loop is better. Viva: what is a list comprehension? (A short way to create a new list from a loop, optionally with a condition.)

### Slide 7: More one-line lists

Go through each row and say it in English: "n times 2 for each n in nums", "n for each n in nums, if n is more than 50". The if version is a filter. The input line in the tip is extremely useful in labs: the user types 10 20 30 on one line and gets the list [10, 20, 30]. Challenge: write the even numbers from 1 to 20 as a comprehension. ([x for x in range(1, 21) if x % 2 == 0].)

### Slide 8: Your turn: four programs

Answers are in solutions/class10_practice.py. Hints. Task 1: read each row with [int(x) for x in input().split()], then total += m[i][i]. Task 2: the result has 3 rows of 2: for j in range(3): row = [m[i][j] for i in range(2)]. Task 3: [x * x for x in range(1, 11) if x % 2 == 0] gives [4, 16, 36, 64, 100]. Task 4: for row in m: print(max(row)).

## Class 11 — tuples, sets and dictionaries

### Slide 9: Tuples, sets and dictionaries

Warm-up: make a list of 5 cities and sort it. Today's three containers: tuple (a list that cannot change), set (no repeats, no order) and dictionary (look things up by name instead of by position). Dictionaries are the most important of the three and are used directly in Friday's mini-project. They also show up in viva questions comparing the four containers.

### Slide 10: Tuples: lists that cannot change

Line 2 is unpacking: the two values in the tuple go into x and y in one step. The swap trick a, b = b, a from Week 1 was secretly using tuples. Run the commented line to show the error. Why use a tuple at all? It protects data that should never change, and it can be a dictionary key (a list cannot). Viva: difference between a list and a tuple? (A list is mutable with [ ], a tuple is immutable with ( ).) Show (5) versus (5,) with type(): the first is just the int 5.

### Slide 11: Sets: no repeats, no order

Connect to Mathematics: these are the same union, intersection and difference from set theory, so draw a Venn diagram. a - b is "in a but not in b", a ^ b is "in exactly one of them". Real use: students in both the cricket team and the coding club = cricket & coding. Sets have no index (a[0] is an error) because they have no order. An empty set is set(), not { } (that is an empty dictionary). Add items with a.add(9).

### Slide 12: Dictionaries: look things up by name

Analogy: a real dictionary or a phone book, where you look up a word (key) to get its meaning (value). Keys must be unique and are usually strings; values can be anything, even lists. Line 5 adds a new pair, line 6 changes an existing one. Show the KeyError from student["age"], then the safe way, student.get("age"), which gives None, or student.get("age", 0). Viva: can two keys be the same? (No, the second one overwrites the first.)

### Slide 13: Working with a dictionary

in checks the keys, not the values. .items() gives key-value pairs, unpacked into k and v like the tuple slide. Looping over d directly (for k in d) gives just the keys. Removing: d.pop("Puri") removes and returns the value; del d["Puri"] just removes. Since Python 3.7 a dictionary remembers the order you added the keys, which is why the loop prints Puri first.

### Slide 14: Counting letters with a dictionary

This counting pattern is one of the most useful in all of programming: votes, word counts, marks per grade. Trace banana: b new (1), a new (1), n new (1), a seen (2), n seen (2), a seen (3). Without get you need an if: if ch in freq: freq[ch] += 1 else: freq[ch] = 1. Show both; exams accept either. Ask: which letter is most common? Loop through freq.items() and keep the biggest, the same pattern as the largest number.

### Slide 15: Which container should I use?

This slide is pure viva preparation. Ask the student to classify: roll numbers of students who submitted homework (set, no repeats), the 7 days of the week (tuple, fixed), a shopping list (list), state capitals (dict: state to capital). Quick summary to memorise: list mutable ordered; tuple immutable ordered; set mutable unordered unique; dict mutable, key-value, unique keys.

### Slide 16: Your turn: four programs

Answers are in solutions/class11_practice.py. Hints. Task 1: book[name] = number in a loop; then if name in book. Task 2: convert both lists with set(), then & and ^. Task 3: the frequency program with line.split(). Task 4: loop over items(), keep the best, and divide sum(d.values()) by len(d).

## Class 12 — Mini-project 1: student record manager

### Slide 17: Mini-project 1

This class is a guided build. The student types the program, you guide. Plan on paper first (10 min), then build in four steps, running the program after each step. It uses input, if/elif, while True with break, lists, dictionaries, f-strings and loops: a full review of Weeks 1 to 4. Save the finished file: Week 5 rewrites it with functions.

### Slide 18: What our program will do

Ask the student to describe the program in their own words before showing code: what should the user see, what does the program remember, what are the choices. Decide the data structure together: why a dictionary and not a list? (Fast lookup by name for searching.) Why a list for the marks? (Several numbers, in a fixed subject order.) Subjects used here are Maths, Physics and Python; change them to the student's actual first-year subjects.

### Slide 19: The menu loop

Build and run this skeleton first, before any feature works. The placeholder print for choice 1 is replaced in the next step. This is how real programmers work: a running skeleton, then one feature at a time. Choices stay strings ("1" not 1), so typing letters cannot crash the program. Ask: what happens if we forget break? (The program never ends.) Add elif branches for 2, 3 and 4 with placeholders too.

### Slide 20: Adding and showing students

Put the add block (lines 2 to 6) inside the if choice == "1" branch, indented, and the show block (lines 8 and 9) inside elif choice == "2". The subject list makes the loop ask three questions with one input line. Test: add two students, then choose 2. Edge case to discuss: what if nobody has been added yet and the user picks 2? Add if not students: print("No students yet").

### Slide 21: Searching and finding the topper

Search uses in on the dictionary keys, which is why the names were stored in title case. The topper search starts with best_total = -1 so that any real total wins. Once both blocks work, the full program is in code/class12_records.py. Run through a full test: add three students, show, search for one that exists and one that does not, show the topper, exit.

### Slide 22: Your turn: grow the project

Answers are in solutions/class12_practice.py (each extension as a small separate piece). Hints. Task 1: compute avg, then the grade ladder. Task 2: if name in students: students.pop(name). Task 3: for i in range(3): total of m[i] over all students, divided by len(students). Task 4: for name, m in students.items(): if min(m) < 40: print(name). Encourage the student to invent a sixth feature of their own; this is good practice for the capstone in Week 8.

## Week 4 recap and what comes next

### Slide 23: What you can do now

Oral quiz: 1. How do you get the centre of a 3 by 3 matrix m? 2. Write a comprehension for the cubes of 1 to 5. 3. List versus tuple? 4. What does {1, 2} & {2, 3} give? 5. How do you avoid a KeyError? (get, or check with in.) 6. How do you loop over keys and values together? 7. Which container for unique roll numbers? Keep the mini-project file: next week it becomes neater with functions.
