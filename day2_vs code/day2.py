# ==============================
# PYTHON BASICS - ALL IN ONE
# ==============================

# 1. Variables and Data Types
name = "Praveen"
age = 22
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print("\nData Types:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# 2. Operators
a = 10
b = 5

print("\nOperators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 3. For Loop
print("\nFor Loop:")
for i in range(1, 6):
    print(i)

# 4. While Loop
print("\nWhile Loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 5. Function
def greet(name):
    print("\nHello,", name + "! Welcome to Python.")

greet(name)

# 6. Simple Program - Sum of Two Numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print("Sum =", total)

print("\nTask Completed Successfully!")
