# Class 8 - palindrome word

word = input("Word: ").lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
