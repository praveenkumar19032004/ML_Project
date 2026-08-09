import numpy as np

# Create two NumPy arrays
a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 3, 5, 7, 9])

print("Array A:", a)
print("Array B:", b)

# Indexing
print("First Element of A:", a[0])
print("Last Element of B:", b[-1])

# Slicing
print("A[1:4]:", a[1:4])

# Array Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Mathematical Functions
print("Square of A:", np.square(a))
print("Square Root of A:", np.sqrt(a))

# Statistical Functions
print("Sum of A:", np.sum(a))
print("Mean of A:", np.mean(a))
print("Maximum of A:", np.max(a))
print("Minimum of A:", np.min(a))

# Reshape Array
c = np.arange(1, 10).reshape(3, 3)
print("\n3 x 3 Matrix:")
print(c)

# Matrix Indexing
print("Element at Row 2, Column 2:", c[1, 1])
print("First Row:", c[0])
print("Second Column:", c[:, 1])

# Transpose
print("Transpose of Matrix:")
print(c.T)
