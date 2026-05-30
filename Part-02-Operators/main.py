print("=" * 50)
print("HUNARMAND PUNJAB - OPERATORS PRACTICE")
print("=" * 50)

a = 20
b = 5

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\nComparison Operators")
print(a > b)
print(a < b)
print(a == b)
print(a != b)

print("\nLogical Operators")
print(a > 10 and b < 10)
print(a > 10 or b > 10)
print(not(a < b))

print("\nAssignment Operators")
x = 10
x += 5
print("x += 5 =", x)

x -= 2
print("x -= 2 =", x)

print("\nMembership Operators")

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" not in fruits)

print("\nIdentity Operators")

list1 = [1, 2, 3]
list2 = list1

print(list1 is list2)
print(list1 is not list2)

print("\nProgram Completed Successfully")