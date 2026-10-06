# Class 3 - Simple interest calculator (Input -> Process -> Output)

# Input
p = float(input("Principal (Rs.): "))
r = float(input("Rate (% per year): "))
t = float(input("Time (years): "))

# Process
si = p * r * t / 100

# Output
print(f"Simple interest = Rs. {si:.2f}")
print(f"Total amount = Rs. {p + si:.2f}")

# Extension: compound interest
amount = p * (1 + r / 100) ** t
print(f"With compound interest = Rs. {amount:.2f}")
