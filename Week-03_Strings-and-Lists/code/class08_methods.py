# Class 8 - string methods (they return a NEW string)

s = "  puri Beach "
print(repr(s.upper()))            # '  PURI BEACH '
print(repr(s.lower()))
print(repr(s.title()))            # '  Puri Beach '
print(repr(s.strip()))            # 'puri Beach'
print(repr(s.replace("Beach", "Temple")))
print(len(s.strip()))             # 10

# split and join
line = "I love Odia food"
words = line.split()
print(words)                      # ['I', 'love', 'Odia', 'food']
print(len(words), "words")
print("-".join(words))            # I-love-Odia-food
print("10,20,30".split(","))      # ['10', '20', '30']

# searching
s = "Jagannath"
print("nath" in s)                # True
print(s.find("nath"))             # 5
print(s.find("xyz"))              # -1
print(s.count("a"))               # 3
print("ram@gmail.com".endswith("@gmail.com"))   # True
