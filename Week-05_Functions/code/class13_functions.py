# Class 13 - defining and calling functions

def line():
    print("=" * 20)

line()
print("Ananya")
line()

def greet(name):                 # name is a parameter
    print("Namaskar,", name)
    print("Welcome to ITER!")

greet("Ananya")                  # "Ananya" is an argument
greet("Subham")

# print only shows; return hands the value back
def area(l, b):
    return l * b

x = area(4, 5)
print(x + 1)                     # 21

# default and keyword arguments
def fare(km, rate=12):
    return km * rate

print(fare(10))                  # 120
print(fare(10, 15))              # 150
print(fare(rate=20, km=5))       # 100
