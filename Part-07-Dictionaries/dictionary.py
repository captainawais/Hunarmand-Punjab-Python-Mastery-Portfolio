print("=" * 60)
print("HUNARMAND PUNJAB - DICTIONARIES")
print("=" * 60)

# Student Dictionary

student = {
    "Name": "Awais Farooq",
    "Age": 25,
    "Grade": "A"
}

print("\nOriginal Student Data")
print(student)

# Access Values

print("\nAccessing Values")

print("Name:", student["Name"])
print("Age:", student["Age"])
print("Grade:", student["Grade"])

# Update Values

print("\nUpdating Grade")

student["Grade"] = "A+"

print(student)

# Add New Field

student["Course"] = "Python Programming"

print("\nUpdated Dictionary")

print(student)

# Loop Through Dictionary

print("\nDictionary Items")

for key, value in student.items():
    print(f"{key} : {value}")

print("\nProgram Completed Successfully")