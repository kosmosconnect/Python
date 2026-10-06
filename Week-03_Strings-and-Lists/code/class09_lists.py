# Class 9 - lists: index, change, methods, sorting

marks = [78, 92, 65, 88]
print(marks[0], marks[-1])        # 78 88
print(marks[1:3])                 # [92, 65]
print(len(marks))                 # 4
marks[2] = 70                     # lists are mutable
print(marks)                      # [78, 92, 70, 88]

f = ["Rasagola", "Pakhala"]
f.append("Chhena")
f.insert(0, "Dahi")
print(f)                          # ['Dahi', 'Rasagola', 'Pakhala', 'Chhena']
f.remove("Pakhala")
last = f.pop()
print(last, f)                    # Chhena ['Dahi', 'Rasagola']
print(f.index("Rasagola"), f.count("Rasagola"))   # 1 1

# Largest without max()
nums = [34, 78, 12, 91, 56]
big = nums[0]
for n in nums:
    if n > big:
        big = n
print("Largest:", big)            # 91

# sort() changes the list, sorted() makes a new one
nums = [34, 12, 91]
new = sorted(nums)
print(new, nums)                  # [12, 34, 91] [34, 12, 91]
nums.sort()
print(nums)                       # [12, 34, 91]
nums.sort(reverse=True)
print(nums)                       # [91, 34, 12]
