# Class 11 - tuples and sets

point = (3, 4)
x, y = point                 # unpacking
print(x, y)                  # 3 4
days = ("Mon", "Tue", "Wed")
print(days[1], len(days))    # Tue 3
# days[0] = "Sun"            # TypeError: tuples cannot change
print(type((5)), type((5,))) # int, tuple

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b)                 # union {1, 2, 3, 4, 5}
print(a & b)                 # intersection {3, 4}
print(a - b)                 # difference {1, 2}
print(a ^ b)                 # in exactly one {1, 2, 5}
print(set([1, 1, 2, 2]))     # {1, 2}
print(3 in a)                # True
nums = [5, 3, 5, 1, 3]
print(list(set(nums)))       # repeats removed (order may change)
