def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def square(a):
    return a ** 2

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Sum:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(2, 3))
print("Square:", square(5))