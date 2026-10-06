# Class 7 - strings: making, joining, indexing, slicing

city = "Bhubaneswar"
food = 'rasagola'
print(len(city))                  # 11

a = "Ananya"
b = "Das"
print(a + " " + b)                # Ananya Das
print("Ha" * 3)                   # HaHaHa
print("-" * 12)
print("Age: " + str(18))          # numbers must become text before +

# Indexing: starts at 0, negative counts from the end
word = "PYTHON"
print(word[0], word[3], word[-1]) # P H N

# Slicing: s[start:stop] - stop is not included
s = "Cuttack"
print(s[0:3])                     # Cut
print(s[3:7])                     # tack
print(s[:3], s[3:], s[-4:])       # Cut tack tack
print(s[::-1])                    # kcattuC
print(s[::2])                     # Ctak

# Strings are immutable: build a new one instead
name = "priyanka"
# name[0] = "P"                   # TypeError!
name = "P" + name[1:]
print(name)                       # Priyanka
