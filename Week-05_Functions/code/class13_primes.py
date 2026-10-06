# Class 13 - the prime check as a function

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(1, 30):
    if is_prime(x):
        print(x, end=" ")
print()                          # 2 3 5 7 11 13 17 19 23 29
