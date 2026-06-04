import math
import random

print("=" * 60)
print("HUNARMAND PUNJAB - MODULES & PACKAGES")
print("=" * 60)

# =====================================
# MATH MODULE
# =====================================

print("\nMATH MODULE")

number = 25

print("Square Root of", number, "=", math.sqrt(number))

factorial_number = 5

print(
    "Factorial of",
    factorial_number,
    "=",
    math.factorial(factorial_number)
)

# =====================================
# RANDOM MODULE
# =====================================

print("\nRANDOM MODULE")

random_number = random.randint(1, 100)

print("Random Number:", random_number)

# =====================================
# BONUS EXAMPLES
# =====================================

print("\nBONUS EXAMPLES")

print("Value of PI:", math.pi)

print("Power Example (2^5):", math.pow(2, 5))

print("\nProgram Completed Successfully")