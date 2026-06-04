print("=" * 60)
print("HUNARMAND PUNJAB - FUNCTIONS")
print("=" * 60)

# Task 1
def add_numbers(a, b):
    return a + b

print("\nTASK 1 - Addition Function")
print("Sum:", add_numbers(10, 20))

# Task 2
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("\nTASK 2 - Prime Number Checker")

num = int(input("Enter a Number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")

# Task 3
def welcome(name="Student"):
    print("Welcome", name)

print("\nTASK 3 - Default Argument")

welcome()
welcome("Awais")

# Task 4
def total_marks(*marks):
    print("Total Marks:", sum(marks))

print("\nTASK 4 - *args Example")

total_marks(80, 90, 85, 70)

# Task 5
def student_info(**details):
    print("Student Information")

    for key, value in details.items():
        print(f"{key}: {value}")

print("\nTASK 5 - **kwargs Example")

student_info(
    Name="Awais Farooq",
    Course="Python Programming",
    Program="Hunarmand Punjab"
)

print("\nProgram Completed Successfully")