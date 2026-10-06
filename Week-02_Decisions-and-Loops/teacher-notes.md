# Python Week 2 – Decisions & Loops: teacher notes

## Week 2 cover

### Slide 1: Decisions and loops

Week 2 is the most important week for lab exams: almost every first-year lab question uses if/else and loops. Classes: (4) decisions with if, elif and else; (5) while and for loops; (6) nested loops, patterns, primes and Fibonacci. Before starting, check the Week 1 homework folder and ask two quick questions: what does 17 % 5 give, and what does input() return?

## Class 4 — if, else, elif and classic decision programs

### Slide 2: Making decisions

Warm-up (3 minutes): what do these print? 10 > 3 and 2 > 5 (False), not (4 == 4) (False), 15 % 2 == 1 (True). Comparisons give True or False, and today we use those True/False answers to make the program choose what to do.

### Slide 3: Programs that make decisions

Draw this flowchart on paper too: flowcharts are part of many first-year exams. The diamond is a decision box: it asks a yes/no question. Each arrow is a possible path, and only ONE path is taken each time. Ask the student to give two decisions from their own day and say them as "If ..., then ..., else ...". Then point out the condition is always a True/False expression, the same comparisons from Class 3.

### Slide 4: Your first if

This is where indentation finally matters. In C you use { } to group lines; in Python you use indentation (4 spaces, IDLE and VS Code add them automatically after the colon). Run the program twice, with 72 and with 25, so the student sees the indented line being skipped. Common errors to show: forgetting the colon (SyntaxError: expected ':'), and forgetting to indent (IndentationError: expected an indented block). Viva question: "How does Python know which lines belong to an if?" By the indentation.

### Slide 5: Two roads: if … else

Even/odd is the most common first lab program with if/else, so make sure the student can write it from memory. Point out that else has no condition of its own: it simply catches every case the if did not. else must line up exactly with its if (same indentation) and also ends with a colon. Ask: what does the voting program print for age 18? ("You can vote", because 18 >= 18 is True.) Edge case discussion: what about age -5? Programs should ideally check for invalid input; we will handle that properly with try/except in Week 7.

### Slide 6: Many roads: the grade calculator

elif means "else if". Trace the ladder for 82 together, then ask the student to trace 95, 60, 39 and 40. Ask why we do not need marks >= 75 and marks < 90 in the second line. (If we reach that line, marks is already less than 90.) Common bug: writing the ladder in the wrong order, starting with marks >= 40, so 95 would get a C. Order matters: biggest condition first. The grades here are just an example; adjust the cut-offs to whatever your university's grading uses.

### Slide 7: Largest of three numbers

A favourite lab-exam program. Test with three cases: largest first (50, 10, 20), largest in the middle (12, 45, 27) and largest last (5, 8, 99). Also test equal values (7, 7, 3): >= makes it work. Ask the student to write a second version with nested ifs (if a >= b: then if a >= c: ...) because examiners sometimes ask for "nested if" specifically. max(a, b, c) is the real-world one-liner, but in the lab write the logic unless allowed.

### Slide 8: Is it a leap year?

Explain the real-world reason first: a year is about 365.24 days, so we add a day every 4 years, but that over-corrects slightly, so century years skip it, except every 400 years. The elif ladder checks the rarest case (400) first, which is why the order works. Show the one-line version too, because textbooks use it: if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0. Test all four sample years with the student. Viva question: "Why is 1900 not a leap year but 2000 is?"

### Slide 9: Your turn: four decision programs

Answers are in solutions/class04_practice.py. Hints to give if the student is stuck. Task 1: if n > 0, elif n < 0, else. Task 2: check equilateral first (a == b == c), then isosceles (a == b or b == c or a == c), else scalene. Task 3: if units <= 100: bill = units * 5, else: bill = 100 * 5 + (units - 100) * 7. Task 4: op = input("Operator: "), then an elif ladder on op == "+" and so on; inside the "/" branch, check b == 0 before dividing.

## Class 5 — while and for loops, range, accumulators, digits, break and continue

### Slide 10: Loops

Warm-up: ask the student to print the numbers 1 to 5 using print(). Then ask: "Now print 1 to 1000." The groan is the motivation for loops. Today's programs (sum, factorial, reverse number, palindrome, Armstrong) are all standard lab and exam questions.

### Slide 11: Print 1 to 100: two ways

Analogy: a gym trainer says "do 20 push-ups", not "push-up, push-up, push-up..." twenty times. A loop is that single instruction. Each repetition is called an iteration. Examples to sort into while vs for: "keep asking for the password until it is correct" (while: unknown rounds); "print the 7 times table" (for: exactly 10 rounds); "keep reading digits until the number becomes 0" (while).

### Slide 12: The while loop has three parts

Trace the loop on paper with a table: count = 1, is 1 <= 5? yes, print 1, count becomes 2... until count = 6, when 6 <= 5 is False and the loop stops. That is 5 rounds. Then delete the count += 1 line and run it: the student sees the infinite loop and learns Ctrl + C. Ask: what is the value of count after the loop ends? (6, a classic exam question.) Variation: change it to count down from 5 to 1 (start at 5, condition count >= 1, update count -= 1).

### Slide 13: for loops and range()

Read for i in range(1, 11) aloud as "for each i from 1 up to, but not including, 11". The variable i takes each value in turn, and the indented block runs once per value. range has three forms: range(stop), range(start, stop), range(start, stop, step). Common mistake: range(1, 10) for 1 to 10 (it stops at 9). Exam question: how many times does for i in range(2, 20, 3) run? (2, 5, 8, 11, 14, 17: 6 times.) Let the student change n to their roll number's last digit and run it.

### Slide 14: Adding up and multiplying in a loop

An accumulator is a variable that collects a result round by round, like a piggy bank. Trace n = 5 on paper: i = 1: total 1, fact 1; i = 2: total 3, fact 2; i = 3: total 6, fact 6; i = 4: total 10, fact 24; i = 5: total 15, fact 120. Ask why range(1, n + 1) and not range(1, n). (The stop is never included.) Ask why fact starts at 1. (1 is the "do nothing" value for multiplying, like 0 is for adding.) Common bug: putting print inside the loop, which prints a running total every round. Check the sum with the formula n * (n + 1) // 2. Viva: what is 0 factorial? (1.) Variation: sum of only even numbers up to n, using range(2, n + 1, 2).

### Slide 15: Taking a number apart, digit by digit

This one pattern solves many lab questions: reverse a number, sum of digits, count digits, palindrome number and Armstrong number. Trace 1234 in a table with columns n, d, rev, total: (1234, 4, 4, 4), (123, 3, 43, 7), (12, 2, 432, 9), (1, 1, 4321, 10), then n becomes 0 and the loop stops. We use while, not for, because we do not know how many digits there are. Common bug: forgetting n //= 10, which gives an infinite loop. Another: after the loop n is 0, so you must keep a copy if you need the original. Variation for homework: count the digits (add 1 each round instead of adding d). Armstrong: 153 = 1^3 + 5^3 + 3^3.

### Slide 16: Stopping early and skipping a round

Analogy: you are eating rasagolas from a box. break = you are full, so you stop and close the box. continue = this one is squashed, so you skip it and take the next. Run both programs and ask the student to predict the output first. Show the PIN example live: while True: pin = input("PIN: "); if pin == "1234": print("Welcome"); break; else: print("Try again"). Common confusion: break leaves only the innermost loop it is in (important next class with nested loops). Viva: difference between break and continue? Also mention pass: a do-nothing placeholder, used when a block is required but you have nothing to write yet.

### Slide 17: Your turn: four programs

Answers are in solutions/class05_practice.py. Hints if stuck. Task 1: for i in range(1, 11): print(n, "x", i, "=", n * i). Task 2: the digits loop, but count += 1 instead of total += d; treat 0 as a special case (it has 1 digit). Task 3: copy n, add d ** 3 for each digit, compare with the copy at the end. Task 4: either range(2, n + 1, 2) or test i % 2 == 0 inside the loop: show both, the first is faster.

## Class 6 — nested loops, star and number patterns, primes and Fibonacci

### Slide 18: Patterns and classic programs

Warm-up (5 minutes): ask the student to write the digit-sum program from memory. Then ask how they would print a 3 by 4 rectangle of stars. Today is very exam focused: pattern printing, prime numbers and Fibonacci appear in almost every first-year lab exam. Encourage the student to draw each pattern on squared paper before coding it.

### Slide 19: A loop inside a loop

Key idea: for each round of the outer loop, the inner loop runs completely. So the print("*") line runs 3 x 4 = 12 times. Trace it aloud: row 1, col 1 2 3 4, new line; row 2, col 1 2 3 4, new line... Show what happens if print() is indented inside the inner loop (every star on its own line) or removed (all 12 stars on one line). end=" " keeps the cursor on the same line. Viva: how many times does the inner body run for outer range(5) and inner range(3)? (15.) Variation: make the rows and columns come from input().

### Slide 20: Triangles of stars

Show the string repetition trick in the shell first: "ab" * 3 gives "ababab". Then show the nested-loop version of the right triangle too, because some teachers want it in exams: for i in range(1, n + 1): for j in range(i): print("*", end=" "); then print(). Ask the student which line to change to make it 6 rows (only n). Common bug: range(n, 0, -1) written as range(n, 0) which prints nothing, because without a negative step range counts upwards. Let the student invent a pattern with # or their initials.

### Slide 21: The centred pyramid

The pyramid is the most asked pattern. The method matters more than the code: write a small table with columns row, spaces, stars. Row 1: 3, 1. Row 2: 2, 2. Row 3: 1, 3. Row 4: 0, 4. Spaces go down as rows go up, so spaces = n - i. Once the table is right, the code is easy. Challenge: the diamond, which is this pyramid followed by an upside-down one (the second loop runs i from n - 1 down to 1). Common bug: using "*" without the space, which gives a lopsided triangle.

### Slide 22: Patterns with numbers

In the first pattern, j restarts at 1 on every row, because the inner loop starts fresh each time. In Floyd's triangle, num lives outside both loops, so it keeps counting across rows. That difference is the whole lesson: where you create a variable decides when it resets. Ask: what changes if print(j) becomes print(i)? (1 / 2 2 / 3 3 3 / 4 4 4 4.) Another exam favourite: print(i * j) for a small multiplication grid.

### Slide 23: Is the number prime?

A prime has exactly two factors: 1 and itself. is_prime = n > 1 gives False for 0 and 1 and True for everything else, so the loop only has to prove it wrong. This True/False variable is called a flag. Test 29 (prime), 21 (3 x 7), 2 (the only even prime: the loop does not run at all), and 1. Speed-up for strong students: check i only up to int(n ** 0.5) + 1, because factors come in pairs. Python also has for ... else, which runs the else when no break happened: show it only if the student is curious. Homework link: print all primes from 1 to 50 with a nested loop.

### Slide 24: The Fibonacci series

Write 0 1 1 2 3 5 8 13 on the board and ask the student to find the rule before showing code. a is the number we print, b is the next one. In a, b = b, a + b, the right side is worked out first using the OLD values, then both are stored. If the student writes a = b then b = a + b on two lines, the result is wrong: let them try it and find out why. The classic C-style version uses a third variable: c = a + b; a = b; b = c. Fibonacci appears in nature (sunflower seeds, pine cones), which makes a nice story. Next week, recursion gives another way to write it.

### Slide 25: Your turn: four programs

Answers are in solutions/class06_practice.py. Hints. Task 1: for i in range(n): print("* " * n). Task 2: print(i, end=" ") inside the inner loop, i not j. Task 3: put the prime check inside for n in range(2, 51). Task 4: add up every i from 1 to n - 1 where n % i == 0, then compare the total with n. If the student finishes early, ask for the hollow square (stars only on the edges), a good test of if inside nested loops.

## Week 2 recap and what comes next

### Slide 26: What you can do now

Five-minute oral quiz (viva practice): 1. What does elif mean? 2. When would you choose while instead of for? 3. What does range(2, 10, 3) give? (2 5 8.) 4. Difference between break and continue? 5. What is an infinite loop and how do you stop it? (Ctrl + C.) 6. How many times does the inner loop body run for range(4) inside range(3)? (12.) 7. Why must a factorial start at 1? Collect the homework programs at the start of next week.
