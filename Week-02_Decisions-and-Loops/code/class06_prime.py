# Class 6 - is the number prime?

n = int(input("Number: "))
is_prime = n > 1          # 0 and 1 are not prime
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break             # one divisor is enough
if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")
