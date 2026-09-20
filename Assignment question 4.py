## Question 4: Random Floats — Minimum and Maximum##
import random

# Generate 5 random floating-point numbers between 0 and 10
numbers = [random.uniform(0, 10) for _ in range(5)]

print("Generated numbers:", [round(n, 2) for n in numbers])
print("Minimum value:", round(min(numbers), 2))
print("Maximum value:", round(max(numbers), 2))