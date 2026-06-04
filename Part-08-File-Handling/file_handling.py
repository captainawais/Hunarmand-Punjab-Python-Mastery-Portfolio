print("=" * 60)
print("HUNARMAND PUNJAB - FILE HANDLING")
print("=" * 60)

file_name = "student_data.txt"

# =====================================
# WRITE
# =====================================

print("\nWriting Data To File...")

with open(file_name, "w") as file:
    file.write("Name: Awais Farooq\n")
    file.write("Course: Python Programming\n")
    file.write("Program: Hunarmand Punjab\n")

print("Data Written Successfully!")

# =====================================
# READ
# =====================================

print("\nReading File Content...")

with open(file_name, "r") as file:
    content = file.read()

print(content)

# =====================================
# APPEND
# =====================================

print("Appending New Data...")

with open(file_name, "a") as file:
    file.write("Instructor: Akbar Ali\n")

print("Data Appended Successfully!")

# =====================================
# FINAL OUTPUT
# =====================================

print("\nUpdated File Content:")

with open(file_name, "r") as file:
    updated_content = file.read()

print(updated_content)

print("\nProgram Completed Successfully")