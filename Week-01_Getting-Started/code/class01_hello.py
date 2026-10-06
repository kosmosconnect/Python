# Class 1 - My first Python program (slide: "Hello, World!")
print("Hello, World!")
print("Welcome to Bhubaneswar")
print(10 + 5)                       # no quotes, so Python calculates: 15
print("Odisha", "India", sep=" | ")  # sep= changes what goes between items

# Bonus tricks
print("Hi", end=" ")                 # end=" " keeps the next print on the same line
print("there!")
print("*\n* *\n* * *")               # \n starts a new line

# The four golden rules: remove the # from ONE line below to see its error
# Print("Hi")                        # NameError: capital P
# print("Hi')                        # SyntaxError: quotes do not match
#     print("Hi")                    # IndentationError: random spaces at the start
# This whole line is a comment, so Python skips it
