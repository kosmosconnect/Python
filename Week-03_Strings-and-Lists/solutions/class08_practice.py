# Class 8 practice - answers

# Task 1: Title case
name = input("Name: ")
print(name.strip().title())                  # pRIYanka sahoo -> Priyanka Sahoo

# Task 2: Longest word
line = input("Sentence: ")
longest = ""
for w in line.split():
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)

# Task 3: Email check
email = input("Email: ").strip().lower()
if email.count("@") == 1 and (email.endswith(".com") or email.endswith(".in")):
    print("Valid")
else:
    print("Not valid")

# Task 4: Letters, digits, spaces
text = input("Sentence: ")
letters = digits = spaces = 0
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
print("Letters:", letters, "Digits:", digits, "Spaces:", spaces)
