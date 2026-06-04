print("=" * 60)
print("HUNARMAND PUNJAB - EXCEPTION HANDLING")
print("=" * 60)

# ==========================================
# TASK 1
# Division By Zero Handling
# ==========================================

print("\nTASK 1 - Division By Zero")

try:
    number = int(input("Enter a Number: "))
    result = 100 / number

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Please enter a valid number!")

# ==========================================
# TASK 2
# Multiple Exceptions
# ==========================================

print("\nTASK 2 - Multiple Exceptions")

try:
    values = [10, 20, 30]

    index = int(input("Enter List Index: "))

    print("Value =", values[index])

except IndexError:
    print("Error: Index out of range!")

except ValueError:
    print("Error: Please enter numeric value only!")

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("Program Executed Successfully")

print("\nException Handling Completed")