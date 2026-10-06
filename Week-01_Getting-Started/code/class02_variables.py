# Class 2 - Variables and data types (slides: "labelled box", "Four basic types")

# A variable is a labelled box that holds a value
name = "Ananya"
age = 18
cgpa = 8.7
print(name, age, cgpa)

age = 19                  # the box now holds 19; 18 is gone
print(age)

# The four basic data types
roll_no = 2026            # int   - whole numbers
price = 49.50             # float - decimals
city = "Puri"             # str   - text in quotes
is_hosteller = True       # bool  - True or False (capital T and F)

print(type(roll_no))      # <class 'int'>
print(type(price))        # <class 'float'>
print(type(city))         # <class 'str'>
print(type(is_hosteller)) # <class 'bool'>

# Python's reserved keywords (cannot be used as variable names)
import keyword
print(keyword.kwlist)
