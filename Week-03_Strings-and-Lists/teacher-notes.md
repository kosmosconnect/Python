# Python Week 3 – Strings & Lists: teacher notes

## Week 3 cover

### Slide 1: Strings and lists

Week 3 moves from single values to collections. Classes: (7) strings, indexing and slicing; (8) string methods and text programs; (9) lists. Before starting, ask the student to write the pyramid or the prime program from memory: loops are used in every program this week. Check the Week 2 homework (diamond pattern, palindrome number).

## Class 7 — strings, indexing, slicing and looping

### Slide 2: Strings

Warm-up: ask "what type does input() return?" (str). So strings have been with us since Week 1: today we look inside them. Everything this week (names, roll numbers, sentences, passwords) is text processing, which is a big part of real programming and of lab exams (count vowels, reverse a string, palindrome word).

### Slide 3: A string is text in quotes

len() counts characters, including spaces: len("Hi there") is 8. Show the error from the warning live: TypeError: can only concatenate str (not "int") to str. Two fixes: str(18), or better an f-string: f"Age: {age}". Triple quotes make a multi-line string: useful for printing a menu. Viva: is "5" + "5" equal to 10? (No: "55".)

### Slide 4: Every character has a position

Draw the boxes on paper with both rows of numbers. Ask: what is word[5]? (N.) word[-6]? (P.) word[6]? (IndexError: there is no box 6.) Why start at 0? The index is "how many steps from the start", so the first character is 0 steps away. C arrays work the same way, so this helps in the C course too. Quick drill: last character of any string is s[-1] or s[len(s) - 1].

### Slide 5: Cutting out a piece: s[start:stop]

Write Cuttack with indexes 0 to 6 under it (C u t t a c k). s[0:3] takes boxes 0, 1, 2. A useful way to think: the slice length is stop - start. Slicing never gives an IndexError: s[0:100] just returns the whole string. The third number is the step, like in range: s[::2] gives every second character ("Ctak"). Exam question: reverse a string without a loop (s[::-1]). Ask the student to slice their own name: first 3 letters, last 3 letters.

### Slide 6: Visiting every character

This is the string version of the counting loop from Week 2. Trace "Konark": K no, o yes (1), n no, a yes (2), r no, k no. Show the index version too, which some teachers prefer: for i in range(len(word)): ch = word[i]. Both are correct; the first is the Python way. Variation: count consonants (letters that are not vowels, so check ch.isalpha() too, coming next class), or count spaces to count words.

### Slide 7: Strings cannot be changed in place

Run the commented line to show the error: TypeError: 'str' object does not support item assignment. Analogy: a string is like a printed exam paper; to fix a word you print a new copy. Viva favourite: "Are strings mutable in Python?" (No.) "Name a mutable type." (list.) The fix uses slicing from the last slide: everything from index 1 onwards. This is exactly what the .capitalize() method does, which we meet next class.

### Slide 8: Your turn: four programs

Answers are in solutions/class07_practice.py. Hints. Task 1: first[0] + "." + last[0] + ".". Task 2: start with rev = "" and do rev = ch + rev for each character (adding to the front). Task 3: a counting loop with if ch == "a". Task 4: the middle index is len(word) // 2; say "please enter an odd-length word" if len(word) % 2 == 0.

## Class 8 — string methods, split, search and text programs

### Slide 9: String methods

Warm-up: reverse a string with slicing and count vowels with a loop. Explain the word "method": a function that belongs to a value and is called with a dot, like name.upper(). Methods never change the original string (strings are immutable); they give back a new one, so you must store or print the result.

### Slide 10: Cleaning and changing text

Run each line in the shell so the student sees the result appear. Highlight the spaces: strip() removes spaces at both ends only, not in the middle. Real use: a user types " Yes " or "YES" and you want to treat both as "yes", so answer = input().strip().lower(). Also show capitalize() (only the first letter) and swapcase(). Common bug: calling the method and expecting s to change; remember strings are immutable.

### Slide 11: Breaking a sentence into words

split() is the bridge to lists (Class 9): the square brackets in the output are a list. Show "10,20,30".split(",") giving ['10', '20', '30'], strings, not numbers. Common lab use: read many numbers on one line with input().split(). Counting words is now one line: len(line.split()). join is the opposite of split and is called on the glue string, which looks odd at first: " ".join(words).

### Slide 12: Finding things inside text

in is the one to use most: it reads like English and works with lists too. find gives the index of the first match, which you can use with slicing: s[s.find("nath"):] gives "nath". find returns -1 when the text is missing (index() would crash instead). count is case-sensitive: "Jagannath".count("j") is 0. Fix with s.lower().count("j").

### Slide 13: Is it digits? Is it letters?

Test with "abc" (too short), "12345678" (only digits), "odishaabc" (only letters) and "odisha2026". Real use: check that a phone number or roll number has only digits before converting it with int(), so the program does not crash: if roll.isdigit(): roll = int(roll). isalnum() is True for letters and digits mixed. Note that isdigit() of "-5" is False, because of the minus sign.

### Slide 14: Does it read the same backwards?

Start by asking for palindrome examples: madam, level, racecar, and Malayalam (a language that is also a palindrome). Run it without .lower() first, so the student discovers that "Malayalam" fails: the M and m are different. For sentences like "Never odd or even", also remove spaces: word.replace(" ", ""). Exam variant: do it without slicing, using a loop that compares word[i] with word[-1 - i] for the first half.

### Slide 15: Your turn: four programs

Answers are in solutions/class08_practice.py. Hints. Task 1: name.strip().title(). Task 2: loop over line.split() and keep the longest so far (like finding the largest number). Task 3: email.count("@") == 1 and (email.endswith(".com") or email.endswith(".in")). Task 4: three counters and an if/elif with isalpha(), isdigit() and ch == " ".

## Class 9 — lists, list methods, totals, searching and sorting

### Slide 16: Lists

Warm-up question: "Store the marks of 60 students. Do you want 60 variables?" A list solves that. Lists use the same indexing and slicing as strings, so half of today is already known. The big difference: lists are mutable, they can change. Lists in Python are like arrays in C, but they can grow and can hold mixed types.

### Slide 17: A list keeps items in order

Draw the list as boxes with indexes, exactly like the PYTHON string. Line 5 is the key contrast with Class 7: marks[2] = 70 works, while name[0] = "P" failed. An empty list is [] and you can check membership with in: 92 in marks gives True. Viva: difference between a list and a string? (A list holds any items and is mutable; a string holds only characters and is immutable.)

### Slide 18: Adding and removing items

Contrast with strings: s.upper() gave a new string, but f.append() changes f itself and returns None. So f = f.append("x") is a classic bug that leaves f as None. Run each method live and print f after it. pop() also gives back the removed item: last = f.pop(). Also show del f[0] and f.clear(). Viva: difference between remove() and pop()? (remove deletes by value, pop by index and returns it.)

### Slide 19: Total and average of marks

This is the standard way to read n values into a list. Show the one-line alternative for strong students: marks = [int(x) for x in input().split()] reads all marks on one line (list comprehensions come next week). Ask: how do you find how many students scored above the average? (Loop again and count.) Built-ins sum, max, min and len work on any list of numbers. Also show for m in marks: print(m) to loop through items.

### Slide 20: Find the largest without max()

Trace with a table: big starts 34, sees 78 (bigger, big = 78), 12 (no), 91 (big = 91), 56 (no). Why start with nums[0] and not 0? Because if all numbers are negative, 0 would wrongly win. Same pattern finds the smallest (change > to <) and the position of the largest (also store the index). Linear search is the same loop: for each item, if item == target, print the index and break. Viva: what is linear search? (Checking items one by one.)

### Slide 21: Putting a list in order

sort() is a list method and changes the list; sorted() is a function, works on any collection (even a string) and leaves the original alone. Strings sort alphabetically: ["Puri", "Cuttack", "Angul"] becomes ["Angul", "Cuttack", "Puri"]. Capital letters come before small ones. Other useful ones: nums.reverse() and nums[::-1]. If the exam asks for a sorting algorithm (bubble sort), that comes in Week 8 revision; for now use the built-ins.

### Slide 22: Your turn: four programs

Answers are in solutions/class09_practice.py. Hints. Task 1: average first, then a counting loop. Task 2: sort and take [-2], but better without sorting: keep big and second, update both in one loop. Task 3: start with unique = [] and append only if item not in unique. Task 4: two empty lists and an if/else with n % 2 inside the loop.

## Week 3 recap and what comes next

### Slide 23: What you can do now

Oral quiz: 1. What is s[-1]? 2. What does "Puri"[1:3] give? ("ur".) 3. Are strings mutable? 4. Difference between find() and index()? 5. What does split() return? 6. Difference between append() and insert()? 7. Difference between sort() and sorted()? 8. How do you reverse a list in one line? Next week has the first mini-project, so the student should be comfortable with lists.
