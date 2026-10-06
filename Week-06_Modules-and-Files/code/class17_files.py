# Class 17 - writing, appending, reading and counting

cities = ["Bhubaneswar", "Cuttack", "Puri"]
with open("cities.txt", "w") as f:           # "w" starts a fresh file
    for c in cities:
        f.write(c + "\n")

with open("cities.txt", "a") as f:           # "a" adds to the end
    f.write("Konark\n")
print("Saved!")

with open("cities.txt") as f:
    for line in f:
        print(line.strip())

with open("cities.txt") as f:
    lines = f.readlines()
print(len(lines), "cities")

# Count lines, words and characters of any file
name = input("File: ")
lines = words = chars = 0
with open(name) as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
print(f"{lines} lines, {words} words, {chars} chars")
