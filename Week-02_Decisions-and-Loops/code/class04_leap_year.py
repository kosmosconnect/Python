# Class 4 - leap year (check the rarest case first)

year = int(input("Year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# One-line version:
# (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
