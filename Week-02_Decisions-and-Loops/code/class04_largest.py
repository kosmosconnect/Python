# Class 4 - largest of three numbers

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
