print("=" * 60)
print("HUNARMAND PUNJAB - LISTS, TUPLES & SETS")
print("=" * 60)

# ==========================
# LIST
# ==========================

print("\nLIST EXAMPLE")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("All Fruits:")

for fruit in fruits:
    print("-", fruit)

# ==========================
# TUPLE
# ==========================

print("\nTUPLE EXAMPLE")

colors = ("Red", "Green", "Blue")

print("Tuple Values:")

for color in colors:
    print("-", color)

print("\nTuple is immutable (cannot be changed).")

# ==========================
# SET
# ==========================

print("\nSET EXAMPLE")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("\nUnion:")
print(set1.union(set2))

print("\nIntersection:")
print(set1.intersection(set2))

print("\nDifference:")
print(set1.difference(set2))

print("\nProgram Completed Successfully")