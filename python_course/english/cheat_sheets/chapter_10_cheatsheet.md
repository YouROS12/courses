# Chapter 10: Error Handling - Quick Reference

## Basic Try-Except

```python
# Without error handling
age = int(input("Enter age: "))  # Crashes if not a number!

# With error handling
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old")
except:
    print("Invalid input!")
```

## Common Exception Types

| Exception | When it Occurs | Example |
|-----------|----------------|---------|
| `ValueError` | Invalid value conversion | `int("abc")` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `TypeError` | Wrong type operation | `"hello" + 5` |
| `IndexError` | Invalid list index | `[1, 2][5]` |
| `KeyError` | Invalid dictionary key | `{"a": 1}["b"]` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `AttributeError` | Invalid attribute | `x = 5; x.append(1)` |
| `NameError` | Undefined variable | `print(undefined_var)` |
| `ImportError` | Failed import | `import nonexistent` |

## Catching Specific Exceptions

```python
# Catch specific exception
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a number!")

# Catch multiple exceptions (separate)
try:
    numbers = [1, 2, 3]
    index = int(input("Index: "))
    print(numbers[index])
except ValueError:
    print("Invalid number!")
except IndexError:
    print("Index out of range!")

# Catch multiple exceptions (same handler)
try:
    result = 10 / int(input("Divisor: "))
except (ValueError, ZeroDivisionError):
    print("Invalid input or zero division!")
```

## Getting Exception Details

```python
# Access exception message
try:
    age = int(input("Enter age: "))
except ValueError as e:
    print(f"Error: {e}")
    # Error: invalid literal for int() with base 10: 'abc'

# More detailed error handling
try:
    file = open("data.txt", "r")
except FileNotFoundError as e:
    print(f"File error: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
```

## The else Clause

**Runs if no exception occurred**

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"Valid age: {age}")
    # This only runs if no exception
```

## The finally Clause

**Always runs, whether exception occurred or not**

```python
# File handling with cleanup
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always executes
    print("Cleanup complete")

# Better: Use context manager instead
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed
```

## Complete Try-Except Structure

```python
try:
    # Code that might raise exception
    result = 10 / int(input("Enter number: "))
except ZeroDivisionError:
    # Handle specific error
    print("Cannot divide by zero!")
except ValueError:
    # Handle another specific error
    print("Invalid number!")
except Exception as e:
    # Catch any other exception
    print(f"Unexpected error: {e}")
else:
    # Runs if no exception
    print(f"Result: {result}")
finally:
    # Always runs
    print("Operation complete")
```

## Raising Exceptions

```python
# Raise an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Using raise
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Re-raise exception
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Logging error...")
    raise  # Re-raises the same exception
```

## Custom Exceptions

```python
# Define custom exception
class InvalidAgeError(Exception):
    pass

# Use custom exception
def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age too high")
    return age

# Handle custom exception
try:
    user_age = set_age(-5)
except InvalidAgeError as e:
    print(f"Invalid age: {e}")
```

## Validation Patterns

### Retry until valid input

```python
while True:
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age must be positive!")
            continue
        break  # Valid input, exit loop
    except ValueError:
        print("Please enter a number!")

print(f"Age set to: {age}")
```

### Validate with default value

```python
def get_int(prompt, default=0):
    try:
        return int(input(prompt))
    except ValueError:
        return default

age = get_int("Enter age: ", 18)
```

### Multiple attempts

```python
max_attempts = 3
for attempt in range(max_attempts):
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        if attempt < max_attempts - 1:
            print(f"Invalid input. {max_attempts - attempt - 1} attempts left")
        else:
            print("Too many invalid attempts!")
            age = None
```

## Common Error Patterns

### Safe dictionary access

```python
# Without error handling
person = {"name": "Alice"}
print(person["age"])  # KeyError!

# With error handling
try:
    print(person["age"])
except KeyError:
    print("Age not found")

# Better: Use get()
age = person.get("age", "Unknown")
```

### Safe list access

```python
# Without error handling
numbers = [1, 2, 3]
print(numbers[10])  # IndexError!

# With error handling
try:
    print(numbers[10])
except IndexError:
    print("Index out of range")

# Better: Check length
if len(numbers) > 10:
    print(numbers[10])
```

### Safe type conversion

```python
# Without error handling
value = int(input("Number: "))  # ValueError if not number

# With error handling
try:
    value = int(input("Number: "))
except ValueError:
    value = 0  # Default value
```

### Safe file operations

```python
# Without error handling
with open("data.txt", "r") as file:  # FileNotFoundError!
    content = file.read()

# With error handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
    content = ""
```

## Debugging Patterns

### Print exception details

```python
import traceback

try:
    result = 10 / 0
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print("\nFull traceback:")
    traceback.print_exc()
```

### Log errors

```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"ERROR: Division by zero - {a}/{b}")
        print(f"Details: {e}")
        return None
```

### Assert for debugging

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)

# Raises AssertionError if conditions not met
avg = calculate_average([1, 2, "3"])  # AssertionError!
```

## Best Practices

```python
# ✅ Be specific with exceptions
try:
    age = int(input("Age: "))
except ValueError:  # Specific
    print("Invalid number")

# ❌ Avoid bare except
try:
    age = int(input("Age: "))
except:  # Too broad! Catches everything
    print("Error")

# ✅ Handle exceptions at appropriate level
def read_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return default

# ❌ Don't silence exceptions unnecessarily
try:
    risky_operation()
except:
    pass  # Silent failure - bad!

# ✅ Provide helpful error messages
try:
    age = int(input("Age: "))
except ValueError:
    print("Error: Age must be a whole number")
    print("Example: 25")

# ✅ Clean up resources
try:
    file = open("data.txt", "r")
    process(file)
finally:
    file.close()

# Better: Use context manager
with open("data.txt", "r") as file:
    process(file)
```

## Common Mistakes

```python
# ❌ Wrong: Catching wrong exception
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except ValueError:  # IndexError is raised!
    print("This won't catch it")

# ✅ Correct
except IndexError:
    print("Index out of range")

# ❌ Wrong: Exception variable scope
try:
    x = int("abc")
except ValueError as e:
    pass
print(e)  # Error! e only exists in except block

# ✅ Correct
error_msg = None
try:
    x = int("abc")
except ValueError as e:
    error_msg = str(e)
if error_msg:
    print(error_msg)

# ❌ Wrong: Using try-except for control flow
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# ✅ Better: Use .get()
value = my_dict.get("key", "default")
```

## Exception Hierarchy

```python
# Catch order matters - specific before general!

# ❌ Wrong order
try:
    age = int(input("Age: "))
except Exception:  # Catches everything!
    print("General error")
except ValueError:  # Never reached!
    print("Invalid number")

# ✅ Correct order
try:
    age = int(input("Age: "))
except ValueError:  # Specific first
    print("Invalid number")
except Exception:  # General last
    print("General error")
```

## Quick Examples

```python
# Safe calculator
def calculator():
    try:
        num1 = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ")
        num2 = float(input("Second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Safe file reader
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return ""
    except PermissionError:
        print(f"Permission denied for '{filename}'")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

# Safe JSON loader
import json

def load_json_safe(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return {}

# Input validator
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Must be positive!")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")

age = get_positive_int("Enter your age: ")

# Safe list operations
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

numbers = [1, 2, 3]
value = safe_get(numbers, 10, 0)  # Returns 0 instead of error
```

## When to Use Exceptions

**Use exceptions for:**
- ✅ Unexpected errors (file not found, network issues)
- ✅ Invalid user input
- ✅ Resource management (files, connections)
- ✅ Validation errors

**Don't use exceptions for:**
- ❌ Normal control flow
- ❌ Conditions you can check beforehand
- ❌ Expected situations

```python
# ❌ Bad: Using exception for control flow
try:
    if users[username]:
        login(username)
except KeyError:
    create_user(username)

# ✅ Good: Check condition
if username in users:
    login(username)
else:
    create_user(username)
```
