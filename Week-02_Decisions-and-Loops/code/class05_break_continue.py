# Class 5 - break and continue

for n in range(1, 10):
    if n == 5:
        break                 # leave the loop
    print(n, end=" ")
print()                       # 1 2 3 4

for n in range(1, 10):
    if n % 3 == 0:
        continue              # skip this round
    print(n, end=" ")
print()                       # 1 2 4 5 7 8

# Keep asking until the PIN is right
while True:
    pin = input("PIN: ")
    if pin == "1234":
        print("Welcome")
        break
    print("Try again")
