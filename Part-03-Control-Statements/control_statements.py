print("=" * 60)
print("HUNARMAND PUNJAB - CONTROL STATEMENTS")
print("=" * 60)

# Task 1
print("\nTASK 1 - Positive, Negative, Zero Checker")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# Task 2
print("\nTASK 2 - Student Grading System")

marks = int(input("Enter Marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# Task 3
print("\nTASK 3 - Nested Condition Example")

age = int(input("Enter Age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")

print("\nProgram Completed Successfully")