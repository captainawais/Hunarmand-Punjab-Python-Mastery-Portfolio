print("=" * 60)
print("HUNARMAND PUNJAB - LOOPS & ITERATIONS")
print("=" * 60)

# Task 1
print("\nTASK 1 - Numbers 1 to 20")

for num in range(1, 21):
    print(num, end=" ")

print("\n")

# Task 2
print("TASK 2 - Even Numbers Using While Loop")

num = 2

while num <= 20:
    print(num, end=" ")
    num += 2

print("\n")

# Task 3
print("TASK 3 - Multiplication Table")

number = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n")

# Task 4
print("TASK 4 - Break Example")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("\n")

# Task 5
print("TASK 5 - Continue Example")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\n")

# Task 6
print("TASK 6 - Nested Loop Pattern")

for row in range(5):
    for col in range(row + 1):
        print("*", end=" ")
    print()

print("\nProgram Completed Successfully")