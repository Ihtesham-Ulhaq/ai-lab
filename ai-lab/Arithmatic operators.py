a = 67
b = 69
x = 0
print("----- Arithmetic Operators -----")
print("'+' operator:", a + b)     # Addition
a += b
x = a
print("'+=' operator:", x)        # Addition assignment
print("'-' operator:", a - b)     # Subtraction
a -= b
x = a
print("'-=' operator:", x)        # Subtraction assignment
print("'*' operator:", a * b)     # Multiplication
a *= b
x = a
print("'*=' operator:", x)        # Multiplication assignment
print("'/' operator:", a / b)     # Division (always float)
a = b
x = a
print("'/=' operator:", x)        # Division assignment

print("'%' operator:", a % b)     # Modulus (remainder)
a %= b
x = a
print("'%=' operator:", x)        # Modulus assignment
