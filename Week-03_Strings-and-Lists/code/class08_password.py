# Class 8 - simple password strength check

pw = input("New password: ")
if len(pw) < 8:
    print("Too short")
elif pw.isdigit() or pw.isalpha():
    print("Mix letters and numbers")
else:
    print("Strong enough")
