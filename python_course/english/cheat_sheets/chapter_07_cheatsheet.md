# Chapter 7: Functions - Quick Reference

## Defining Functions

```python
# Basic function
def greet():
    print("Hello!")

# Call the function
greet()  # Output: Hello!
```

## Functions with Parameters

```python
# One parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!

# Multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(3, 5)  # 3 + 5 = 8
```

## Return Values

```python
# Return a value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Return multiple values (as tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Total: {total}")
# Min: 1, Max: 5, Total: 15

# Function without return returns None
def print_hello():
    print("Hello")

result = print_hello()  # Prints "Hello"
print(result)  # None
```

## Default Parameters

```python
# Parameters with default values
def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet()                    # Hello, Guest!
greet("Alice")             # Hello, Alice!
greet("Bob", "Hi")         # Hi, Bob!
greet(greeting="Hey")      # Hey, Guest!
```

## Keyword Arguments

```python
def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}")

# Positional arguments
describe_pet("dog", "Buddy", 3)

# Keyword arguments (order doesn't matter)
describe_pet(name="Buddy", animal="dog", age=3)
describe_pet(age=3, name="Buddy", animal="dog")

# Mix (positional must come first)
describe_pet("dog", name="Buddy", age=3)
```

## Variable Scope

```python
# Global variable
global_var = 10

def example():
    # Local variable
    local_var = 20
    print(f"Global: {global_var}")  # Can read global
    print(f"Local: {local_var}")

example()
print(global_var)  # 10 - OK
print(local_var)   # Error! local_var not defined here

# Modifying global variable
count = 0

def increment():
    global count  # Declare as global to modify
    count += 1

increment()
print(count)  # 1
```

## Docstrings

```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
        width (float): The width of the rectangle
        height (float): The height of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return width * height

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

## Lambda Functions

**Anonymous one-line functions**

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Common use: with sorted, map, filter
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(numbers, key=lambda x: x)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"])
```

## *args - Variable Positional Arguments

```python
# Accept any number of positional arguments
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())               # 0

# *args is a tuple
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

print_args("a", "b", "c")
```

## **kwargs - Variable Keyword Arguments

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=20, city="NYC")
# name: Alice
# age: 20
# city: NYC

# **kwargs is a dictionary
def describe(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    return kwargs

result = describe(color="blue", size="large")
print(result)  # {"color": "blue", "size": "large"}
```

## Combining Parameter Types

**Order matters: positional, *args, keyword, **kwargs**

```python
def example(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

example(1, 2, 3, default="custom", extra="data")
# Required: 1
# Args: (2, 3)
# Default: custom
# Kwargs: {'extra': 'data'}
```

## Common Function Patterns

### Validation

```python
def divide(a, b):
    if b == 0:
        return None  # or raise an error
    return a / b

result = divide(10, 2)  # 5.0
result = divide(10, 0)  # None
```

### Processing lists

```python
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

result = get_evens([1, 2, 3, 4, 5, 6])
print(result)  # [2, 4, 6]
```

### Building strings

```python
def format_name(first, last):
    return f"{first.title()} {last.title()}"

name = format_name("alice", "smith")
print(name)  # Alice Smith
```

### Calculations

```python
def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0
    return sum(numbers) / len(numbers)

avg = calculate_average([85, 90, 78, 92])
print(f"Average: {avg}")  # Average: 86.25
```

## Recursion

**Function calling itself**

```python
# Factorial: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # 120

# Countdown
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)  # 5 4 3 2 1 Done!
```

## Function as Arguments

```python
def apply_operation(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

def double(x):
    return x * 2

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
squared = apply_operation(numbers, square)

print(doubled)  # [2, 4, 6, 8, 10]
print(squared)  # [1, 4, 9, 16, 25]
```

## Common Mistakes

```python
# ❌ Wrong: Modifying mutable default argument
def add_item(item, items=[]):  # Dangerous!
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [1, 2] - unexpected!

# ✅ Correct: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# ❌ Wrong: Forgetting to return
def add(a, b):
    result = a + b  # Forgot return!

print(add(3, 5))  # None

# ✅ Correct
def add(a, b):
    return a + b

# ❌ Wrong: Using print instead of return
def add(a, b):
    print(a + b)  # Prints but doesn't return

result = add(3, 5)  # Prints 8
print(result * 2)   # Error! result is None

# ✅ Correct
def add(a, b):
    return a + b
```

## Best Practices

```python
# ✅ Use descriptive names
def calculate_total_price(items, tax_rate):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    return subtotal + tax

# ✅ Keep functions focused (do one thing)
def validate_email(email):
    return "@" in email and "." in email

def send_email(to, subject, body):
    if not validate_email(to):
        return False
    # Send email logic
    return True

# ✅ Use docstrings for complex functions
def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position in Fibonacci sequence

    Returns:
        int: The Fibonacci number at position n
    """
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# ✅ Validate inputs
def divide(a, b):
    """Divide a by b safely."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## Quick Examples

```python
# Temperature converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(0))   # 32.0
print(fahrenheit_to_celsius(32))  # 0.0

# Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade(85))  # B

# List statistics
def get_statistics(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

stats = get_statistics([1, 2, 3, 4, 5])
print(stats)
# {'min': 1, 'max': 5, 'avg': 3.0, 'count': 5}

# String formatter
def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:.2f}"

print(format_currency(19.99))      # $19.99
print(format_currency(50, "€"))    # €50.00

# Password validator
def validate_password(password):
    if len(password) < 8:
        return False, "Too short"
    if not any(c.isupper() for c in password):
        return False, "Needs uppercase"
    if not any(c.isdigit() for c in password):
        return False, "Needs digit"
    return True, "Valid"

is_valid, message = validate_password("Pass123")
print(f"{message}: {is_valid}")
```

## Type Hints (Python 3.5+)

```python
# Optional but helpful for documentation
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def get_stats(numbers: list) -> dict:
    return {
        "min": min(numbers),
        "max": max(numbers)
    }

# Type hints don't enforce types at runtime
# They're mainly for documentation and IDE support
```
