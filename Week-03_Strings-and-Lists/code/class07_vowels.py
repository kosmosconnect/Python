# Class 7 - count the vowels in a word

word = input("Word: ")
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:", count)           # Konark -> 2
