# Class 9 - read 5 marks into a list, then total and average

marks = []
for i in range(5):
    m = int(input("Marks: "))
    marks.append(m)
total = sum(marks)
avg = total / len(marks)
print("Marks:", marks)
print(f"Average: {avg:.1f}")
