# Class 7 practice - answers

# Task 1: Initials
first = input("First name: ")
last = input("Last name: ")
print(first[0] + "." + last[0] + ".")        # S.N.

# Task 2: Reverse with a loop
word = input("Word: ")
rev = ""
for ch in word:
    rev = ch + rev                           # add to the front
print(rev, rev == word[::-1])

# Task 3: Count the letter "a"
sentence = input("Sentence: ")
count = 0
for ch in sentence:
    if ch == "a":
        count += 1
print('"a" appears', count, "times")

# Task 4: Middle letter
word = input("Odd-length word: ")
if len(word) % 2 == 0:
    print("Please enter an odd-length word")
else:
    print("Middle:", word[len(word) // 2])   # Cuttack -> t
