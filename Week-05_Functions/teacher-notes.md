# Python Week 5 – Functions & Recursion: teacher notes

## Week 5 cover

### Slide 1: Functions and recursion

Week 5 is about organising code. Classes: (13) defining functions, parameters and return; (14) scope, returning several values, lambda and sorting with a key, then rewriting the mini-project with functions; (15) recursion. Functions are the single biggest step from "beginner scripts" to real programs, and recursion is a guaranteed exam topic. Check the Week 4 mini-project extensions first.

## Class 13 — defining functions, parameters, return and arguments

### Slide 2: Functions

Warm-up: "How many times have you used print, input, len and range?" Hundreds. They are functions someone else wrote. Today the student writes their own. Analogy: a pressure cooker. You put ingredients in (arguments), it does its job, and you take food out (the return value). You do not need to know how it works inside every time you use it.

### Slide 3: Write once, use many times

Three reasons to use functions, easy to remember: 1. Reuse: write once, call many times. 2. Readability: a name like line() or is_prime(n) says what the code does. 3. Fixing: a bug is fixed in one place. Ask the student to change the line to use "-" instead of "=": in the left version three edits, in the right version one. Point out the blank line after the function: the def only defines; nothing runs until line() is called.

### Slide 4: Defining and calling a function

Vocabulary that comes up in viva: the parameter is the name in the definition (name); the argument is the actual value you pass when calling ("Ananya"). Show what happens if you call greet() with nothing (TypeError: missing 1 required positional argument). Also show that calling a function before its def line gives a NameError, because Python reads top to bottom. Naming rules are the same as variables; use verbs: greet, calculate_area, is_even.

### Slide 5: print shows it, return hands it back

A function with no return gives back None. This is the most important slide of the class. On the left, area prints 20 and then returns None, so x is None and None + 1 crashes. On the right, area returns 20 into x. Analogy: print is a shopkeeper telling you the price; return is the shopkeeper handing you the packet, which you can then use. return also ends the function immediately: any line after it does not run. Viva: difference between print and return? Ask the student to write def square(n): return n * n and use it in print(square(3) + square(4)).

### Slide 6: Default and keyword arguments

Story: an auto-rickshaw fare in Bhubaneswar, usually Rs. 12 per km, but more at night. fare(10) uses the default 12. fare(10, 15) overrides it. fare(rate=20, km=5) uses keyword arguments, so the order does not matter. print itself uses keyword arguments: print("a", "b", sep="-", end="!"). Viva: positional vs keyword arguments? (Positional are matched by order, keyword by name.)

### Slide 7: Week 2's prime check as a function

Compare with the Week 2 prime program: the flag variable and break are gone, because return False exits immediately. Now printing primes from 1 to 30 is a two-line loop, because the hard part has a name. This pattern (a small function used inside a loop) is how real programs are built. Common bug: putting return True inside the loop (indented under the for), which returns after checking only 2. Let the student make that mistake and find it. Note range(1, 30) stops at 29, which is prime, so 29 is the last number printed.

### Slide 8: Your turn: four programs

Answers are in solutions/class13_practice.py. Hints. Task 1: return 3.14159 * r * r; for r = 7, area is about 153.94 and perimeter about 43.98. Task 2: the Week 2 elif program, but with return instead of print. Task 3: the accumulator loop inside the function, then for i in range(1, 7): print(i, fact(i)). Task 4: move the Week 3 vowel loop into the function and return count.

## Class 14 — scope, several return values, lambda, sorting with key, tidy code

### Slide 9: More about functions

Warm-up: write is_even(n) and use it to print the even numbers from 1 to 20. Today mixes several short topics that come up in viva: scope, multiple return values, lambda. The second half rewrites the Week 4 record manager with functions, which shows why functions matter in a real program.

### Slide 10: Local and global variables

Analogy: a variable inside a function is like something written on the classroom whiteboard: it is wiped when the class (function call) ends, and other classrooms cannot see it. The local city inside trip is a different variable that happens to have the same name. The global keyword lets a function change a global (global count), but avoid it: it makes programs hard to follow. Viva: what is the scope of a variable? (The part of the program where it can be used.)

### Slide 11: Returning more than one value

This is something C cannot do directly, and students like it. The function returns the tuple (235, 78.33, 92); the unpacking line splits it into three variables. If the student writes result = stats([...]), then result is the tuple and result[0] is the total. The number of variables on the left must match the number of values, otherwise a ValueError. Good practice: make the student write min_max(nums) that returns both the smallest and largest.

### Slide 12: Tiny one-line functions

lambda arguments: expression. It can only hold one expression and returns it automatically. map applies a function to every item; filter keeps items for which the function returns True. In practice a list comprehension is often clearer: [x * x for x in nums] does the same as map. The real everyday use is the key in sorting, on the next slide. Viva: what is a lambda function? (An anonymous, single-expression function.)

### Slide 13: Sorting students by marks

Build it up in the shell: marks.items() gives pairs; sorted(marks.items()) sorts by name (the first item of each pair); adding key=lambda p: p[1] sorts by marks instead. reverse=True puts the highest first. key works with any function: sorted(names, key=len) sorts words by length. enumerate(list, 1) gives a counter starting at 1 together with each item; it is handy for numbered menus too.

### Slide 14: The record manager, rebuilt with functions

Open code/class14_records_functions.py and walk through it. Compare with the Week 4 version: the menu loop is now about 15 lines and reads like English. Each function can be tested on its own, for example print(topper({"A": [1, 2, 3]})). Functions receive the dictionary as a parameter (db) instead of using a global: this makes them reusable. Let the student add a grade(avg) function and use it inside show_all.

### Slide 15: Your turn: four programs

Answers are in solutions/class14_practice.py. Hints. Task 1: track small and big in one loop, return small, big. Task 2: sorted(words, key=len). Task 3: list(filter(lambda n: n % 2 == 1, range(1, 21))). Task 4: the elif ladder from Week 2 inside a function that returns the grade string.

## Class 15 — recursion: base case, factorial, tracing, Fibonacci

### Slide 16: Recursion

Warm-up: write fact(n) with a loop. Then: 5! = 5 x 4!, and 4! = 4 x 3!... a problem defined using a smaller copy of itself. That is recursion. It feels like magic at first; tracing on paper is what makes it click, so keep paper ready. Recursion questions (factorial, Fibonacci, sum of digits, tracing output) appear in nearly every first-year exam.

### Slide 17: Every recursive function has two parts

Act out the queue story with three or four objects on the table. The question travels forward (the calls), the first person answers directly (the base case), and the answers travel back, each person adding one (the return values). That forward-then-back shape is exactly what happens in the computer. If there is no first person who knows the answer, the question never stops: that is infinite recursion, and Python stops it with RecursionError after about 1000 calls.

### Slide 18: Recursive factorial

Write the mathematical definition on the board first, then show how the code copies it line by line. Ask: what happens with fact(0)? It skips the base case, calls fact(-1), fact(-2)... forever: RecursionError. Fix: use if n <= 1: return 1, which also makes 0! = 1 correct. Ask the student to write power(x, n) the same way: base case n == 0 gives 1, recursive case x * power(x, n - 1).

### Slide 19: What really happens in fact(4)

Draw this as a staircase going down then up, or as a stack of plates: each new call is a plate on top, and plates are removed from the top. That is why it is called the call stack. Every waiting call keeps its own n (a local variable): there are four different n's alive at the same time. Exam questions often ask to trace a recursive function's output, so practise with fact(3) and a sum function: def s(n): return 0 if n == 0 else n + s(n - 1).

### Slide 20: Fibonacci and digit sum, recursively

fib has two base cases (0 and 1) and two recursive calls. It is short but slow: fib(30) makes over a million calls, because it recalculates the same values. Show this by timing fib(30); the Week 2 loop version is instant. dsum uses the same % 10 and // 10 trick from Week 2: the last digit plus the digit sum of the rest. Ask the student to trace dsum(123): 3 + dsum(12) = 3 + (2 + dsum(1)) = 3 + 2 + 1 = 6.

### Slide 21: Recursion or a loop?

Be honest with the student: in day-to-day Python, loops are used more. Recursion shines when the data itself is nested, like folders inside folders or a family tree. Each recursive call uses memory on the call stack, which is why Python limits the depth (about 1000). Optional fun: Tower of Hanoi with 3 discs, a famous recursion puzzle, solved in 5 lines: def hanoi(n, a, b, c): if n: hanoi(n - 1, a, c, b); print(a, "->", c); hanoi(n - 1, b, a, c).

### Slide 22: Your turn: four programs

Answers are in solutions/class15_practice.py. Hints. For each task first write the base case, then the recursive case. Task 1: n == 0 gives 1. Task 2: n == 0 gives 0, else n + total(n - 1). Task 3: an empty string (or length 1) is its own reverse; else s[-1] + rev(s[:-1]). Task 4: if b == 0 return a, else return gcd(b, a % b). GCD is a common exam program.

## Week 5 recap and what comes next

### Slide 23: What you can do now

Oral quiz: 1. Parameter vs argument? 2. print vs return? 3. What does a function without return give back? (None.) 4. Local vs global variable? 5. Write a lambda that triples a number. 6. What are the two parts of a recursive function? 7. What happens without a base case? (RecursionError.) 8. Trace fact(3). Next week the record manager will save its data to a file, so keep the function version.
