# Class 14 - scope, several return values, lambda, sorting with key

city = "Bhubaneswar"             # global

def trip():
    city = "Puri"                # local: a different variable
    print("In trip:", city)

trip()
print("Outside:", city)

def stats(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg, max(marks)

t, a, top = stats([78, 92, 65])
print(t, round(a, 1), top)       # 235 78.3 92

sq = lambda x: x * x
add = lambda a, b: a + b
print(sq(5), add(2, 3))          # 25 5
nums = [1, 2, 3, 4]
print(list(map(sq, nums)))       # [1, 4, 9, 16]
print(list(filter(lambda n: n > 2, nums)))   # [3, 4]

marks = {"Ananya": 92, "Subham": 78,
         "Priyanka": 88}
ranked = sorted(marks.items(),
                key=lambda p: p[1],
                reverse=True)
for rank, (name, m) in enumerate(ranked, 1):
    print(rank, name, m)
