# Class 11 - dictionaries

student = {"name": "Subham",
           "roll": 21,
           "city": "Cuttack"}
print(student["name"])                 # Subham
student["cgpa"] = 8.4                  # new key: added
student["city"] = "Puri"               # same key: updated
print(student["city"], len(student))   # Puri 4
print(student.get("age"))              # None instead of a KeyError

d = {"Puri": 3, "Cuttack": 5}
print(d.get("Angul", 0))               # 0
print("Puri" in d)                     # True
print(list(d.keys()), list(d.values()))
for k, v in d.items():
    print(k, v)

# Counting letters
word = input("Word: ")
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)                            # banana -> {'b': 1, 'a': 3, 'n': 2}
