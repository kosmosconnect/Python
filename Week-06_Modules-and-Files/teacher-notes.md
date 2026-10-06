# Python Week 6 – Modules, Files & Mini-project 2: teacher notes

## Week 6 cover

### Slide 1: Modules, files and Mini-project 2

Week 6 connects programs to the outside world. Classes: (16) modules: math, random, datetime and your own; (17) reading and writing text files and CSV files; (18) Mini-project 2, an expense tracker that saves to a CSV file. Until now every program forgot everything when it closed; this week the data stays. Check the Week 5 recursion homework first.

## Class 16 — modules: math, random, datetime and your own

### Slide 2: Modules

Warm-up: write a function that returns the square root of a number without using ** 0.5. Hard! Someone already wrote it, in the math module. A module is just a Python file full of useful functions. Python comes with hundreds of them (the "standard library"), and millions more can be installed with pip. Knowing what exists saves enormous time.

### Slide 3: Three ways to bring in a module

Style 1 is the clearest: math.sqrt tells the reader where sqrt comes from. Style 2 is handy for one or two names. Style 3 is common for long names (import numpy as np is famous). Avoid from math import *: it dumps every name in and can hide your own variables. Show dir(math) in the shell for a list of names. Viva: what is a module? (A .py file with functions and variables you can import.) What is a package? (A folder of modules.)

### Slide 4: The math module

Run each line in the shell. Real use for ceil: 47 students, 6 per bench: math.ceil(47 / 6) = 8 benches needed. Compare with 47 // 6 = 7, which forgets the leftover students. Mention math.sin, math.cos and math.radians for students who like trigonometry, and math.log10. Note sqrt and pow always return floats.

### Slide 5: Dice, OTPs and lucky draws

Run it three times: the output changes every time, so the numbers on the slide are just one example. Note randint includes both ends, unlike range. Mini-game for the student (good practice of loops and if): the computer picks a number from 1 to 50 and the user guesses, with "too high" or "too low" hints, counting the tries. The answer is in solutions/class16_practice.py. random.seed(1) makes the results repeatable, which helps when testing.

### Slide 6: Working with dates

The output depends on the day you run it; the slide shows 6 October 2026. Ask the student to put their real end-semester exam date in the date(...) line. %d is day, %m month, %Y four-digit year, %B the full month name. Age calculator challenge: read a birth year and print the age this year (today.year - birth_year). For times as well as dates, use datetime.now().

### Slide 7: Any .py file is a module

Do this live: create two files in the same folder. This is how big programs are organised: the record manager could keep its functions in records_lib.py. If the import fails, the files are not in the same folder. Mention pip install for third-party modules (for example pip install requests), but we will not need any this course. The if __name__ == "__main__": line, which runs code only when the file is run directly, is an advanced topic: mention it only if asked.

### Slide 8: Your turn: four programs

Answers are in solutions/class16_practice.py. Hints. Task 1: secret = random.randint(1, 50), a while True loop with a tries counter and break when correct. Task 2: math.ceil(students / per_bench). Task 3: date.today().year - birth_year. Task 4: random.randint(100000, 999999), then compare input() with str(otp).

## Class 17 — text files, modes, reading, writing and CSV

### Slide 9: Files

Warm-up: run the Week 4 record manager, add a student, close it, run it again. The student is gone! Variables live in memory (RAM), which is wiped when the program ends. Files live on disk. Today we learn to save and load. Keep a file browser open next to the editor so the student can watch files appear.

### Slide 10: Opening a file: pick a mode

The most dangerous beginner mistake: opening an existing file with "w" wipes its contents immediately, before anything is written. Use "a" to add. The with block is the modern, safe way: older code uses f = open(...) and f.close(), and forgetting close can lose data. The file is created in the folder the program runs from; if the student cannot find it, print os.getcwd(). Viva: difference between w and a modes?

### Slide 11: Writing a list to a file

After running, open cities.txt in Notepad or VS Code so the student sees real data on disk. Run the program a second time and look again: the first block rewrites the file, then Konark is appended once more, so there is still only one Konark. Change the second "a" to "w" and ask what will be left (only Konark). f.write only accepts strings: to save a number use str(n) or an f-string.

### Slide 12: Reading a file line by line

Show what happens without strip(): blank lines between cities, because the line already ends with \n and print adds another. Three ways to read: read() gives one big string, readlines() a list of lines, and the for loop goes line by line (best for big files). Reading a file that does not exist gives FileNotFoundError; next week we learn to catch it. Quick check: use os.path.exists("cities.txt") before opening.

### Slide 13: Counting lines, words and characters

chars counts the \n at the end of each line too: Bhubaneswar 11 + Cuttack 7 + Puri 4 + Konark 6 = 28 letters, plus 4 new-line characters = 32. Variations for practice: count how many lines contain a given word, find the longest line, or copy one file to another with every line in capital letters.

### Slide 14: CSV files: tables that Excel can open

CSV means comma-separated values: each line is a row, commas separate the columns. Open marks.csv in Excel or Google Sheets to show it becomes a table. newline="" stops blank rows appearing on Windows. When reading, every value comes back as a string ('92'), just like input(), so use int(row[1]) for maths. Skip the header row with next(reader) before the loop.

### Slide 15: Your turn: four programs

Answers are in solutions/class17_practice.py. Hints. Task 1: open with "a" and write f"{date.today()}: {text}\n". Task 2: if word.lower() in line.lower(). Task 3: next(reader) skips the header, then add int(row[1]) and count rows. Task 4: open the source with "r" and the target with "w" in the same with line: with open(a) as src, open(b, "w") as dst.

## Class 18 — Mini-project 2: expense tracker saved to CSV

### Slide 16: Mini-project 2

Guided build again, about the student's own life: hostel and college expenses. It uses functions (Week 5), lists and dictionaries (Weeks 3 and 4), files and CSV (this week). Build it in steps and run after every step. At the end, open expenses.csv in Excel: students love seeing their own data as a real spreadsheet.

### Slide 17: What the expense tracker does

Discuss the file design first: one row per expense with four columns. Why save each expense immediately (append) instead of only at exit? Because if the program crashes or the laptop dies, nothing is lost. Categories to suggest: Food, Travel, Books, Mobile, Other. Ask the student what they spent money on this week to create real test data.

### Slide 18: Loading saved expenses

Each row comes back as a list of 4 strings: ['2026-10-06', 'Food', '40', 'Hostel Maggi']. The amount is a string, so later we use float(row[2]). Test load() on its own: print(load()) should give [] the first time. Next week's try/except gives another way to handle a missing file; both are fine.

### Slide 19: Adding and saving an expense

Mode "a" adds the row to the end of the file, so old expenses stay. Run it, then open expenses.csv to show the new line. Improvement for the student: check the amount with amt.replace(".", "").isdigit() before saving, and ask again if it is not a number (or use try/except next week).

### Slide 20: Totals by category

The for line unpacks each 4-item row straight into four variables. {cat:10} pads the name to 10 characters and {total:8.2f} lines the amounts up in a column: a neat touch for reports. The full program with the menu is in code/class18_expenses.py. Run it, add five or six expenses over two runs, and show that the report includes the ones from the first run.

### Slide 21: Your turn: grow the tracker

Answers are in solutions/class18_practice.py. Hints. Task 1: the date string starts with "2026-10", so compare row[0][:7] with str(date.today())[:7]. Task 2: the largest pattern on float(row[2]). Task 3: compare the sum with BUDGET. Task 4: data.pop(), then open the file with "w" and writerows(data). Encourage the student to keep using the tracker for a week: real data makes the reports interesting.

## Week 6 recap and what comes next

### Slide 22: What you can do now

Oral quiz: 1. Three ways to import? 2. ceil vs floor? 3. Does randint(1, 6) include 6? (Yes.) 4. Difference between w and a modes? 5. Why use with? (It closes the file automatically.) 6. What does readlines() return? 7. Why strip() when reading lines? 8. What does CSV stand for? Next week: what happens when the user types "abc" for the amount... the program crashes. Exceptions fix that.
