# Q8: Function with default argument

def introduce(name, age=None):
    if age is None:
        print(f"My name is {name}. My age is secret.")
    else:
        print(f"My name is {name}. I am {age} years old.")
      
introduce("John", 20)
introduce("John")

# Q9: Drop minimum value using *args

def drop_minimum(*args):
    numbers = list(args)
    minimum = min(numbers)
    numbers.remove(minimum)
    return numbers
  
print(drop_minimum(5, -2, 8, 4, -5, 7, 10))

# Q10: Find maximum of three numbers

def find_max(a, b, c):
    return max(a, b, c)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print("Maximum =", find_max(x, y, z))

main()
# Q11: Lambda function

add = lambda a, b: a + b

print(add(10, 20))

# Q12: Lambda function for temperature conversion

fahrenheit = lambda c: (c * 9 / 5) + 32

c = float(input("Enter temperature in Celsius: "))
print("Fahrenheit =", fahrenheit(c))

# Q13: Create file using exception handling

try:
    with open("student.txt", "x") as file:
        file.write("Python is easy to learn.\n")
        file.write("File handling is important.\n")
        file.write("Practice makes perfect.\n")
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

except Exception as e:
    print("Error:", e)

# Q14(a): Read complete file

with open("student.txt", "r") as file:
    print(file.read())

# Q14(b): Read line by line

with open("student.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")

# Q15: Count total words

with open("student.txt", "r") as file:
    text = file.read()
    words = text.split()

print("Total words:", len(words))

# Q16: Append new line

with open("student.txt", "a") as file:
    file.write("Python file handling becomes simple with practice.\n")

print("Line added successfully.")

# Q17: Exception handling for IndexError

numbers = [7, 4, 0, -2, 3]

print("List:", numbers)

try:
    index = int(input("Enter index: "))
    print("Value =", numbers[index])

except IndexError:
    print("IndexError: Invalid index!")

except ValueError:
    print("Please enter a valid integer.")

#18.calculator.py
# Module containing calculator functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# main.py
# Import calculator module and call its functions

import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculator.add(a, b))
print("Subtraction =", calculator.subtract(a, b))
print("Multiplication =", calculator.multiply(a, b))
print("Division =", calculator.divide(a, b))




