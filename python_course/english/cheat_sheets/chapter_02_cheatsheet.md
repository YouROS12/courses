# Chapter 2: Working with Data - Quick Reference

## User Input

```python
# Get input (always returns a string)
name = input("Enter your name: ")
age = input("Enter your age: ")
```

## Type Conversion (Casting)

| Function | Converts to | Example |
|----------|-------------|---------|
| `int()` | Integer | `int("25")` → `25` |
| `float()` | Float | `float("3.14")` → `3.14` |
| `str()` | String | `str(25)` → `"25"` |
| `bool()` | Boolean | `bool(1)` → `True` |

```python
# Convert input to number
age = int(input("Enter age: "))
height = float(input("Enter height: "))
```

## String Operations

### Concatenation

```python
first = "John"
last = "Doe"
full_name = first + " " + last  # "John Doe"
```

### Repetition

```python
laugh = "ha" * 3  # "hahaha"
line = "-" * 20   # "--------------------"
```

### Indexing

```python
text = "Python"
text[0]   # "P" (first character)
text[-1]  # "n" (last character)
text[-2]  # "o" (second from end)
```

### Slicing

```python
text = "Python"
text[0:3]    # "Pyt" (start to 3, not including 3)
text[2:5]    # "tho"
text[:3]     # "Pyt" (start to 3)
text[3:]     # "hon" (3 to end)
text[:]      # "Python" (entire string)
text[::2]    # "Pto" (every 2nd character)
```

## String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | Uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Lowercase | `"HELLO".lower()` → `"hello"` |
| `.title()` | Title Case | `"hello world".title()` → `"Hello World"` |
| `.strip()` | Remove whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace text | `"cat".replace("c", "b")` → `"bat"` |
| `.split()` | Split into list | `"a b c".split()` → `["a", "b", "c"]` |
| `.find(text)` | Find position | `"hello".find("e")` → `1` |
| `.count(text)` | Count occurrences | `"aaa".count("a")` → `3` |

```python
text = "  Hello World  "
text.strip().lower()  # "hello world"
```

## String Formatting

### F-Strings (Recommended)

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# "My name is Alice and I am 25 years old."

# Expressions in f-strings
print(f"Next year I'll be {age + 1}")
# "Next year I'll be 26"

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # "Price: $19.99"
```

### .format() Method

```python
print("Name: {}, Age: {}".format(name, age))
print("Age: {1}, Name: {0}".format(name, age))
```

### % Formatting (Old Style)

```python
print("Name: %s, Age: %d" % (name, age))
```

## Escape Sequences

| Sequence | Meaning | Example |
|----------|---------|---------|
| `\n` | Newline | `"Line 1\nLine 2"` |
| `\t` | Tab | `"Name:\tJohn"` |
| `\\` | Backslash | `"C:\\Users"` |
| `\'` | Single quote | `'It\'s'` |
| `\"` | Double quote | `"She said \"Hi\""` |

```python
print("Line 1\nLine 2\nLine 3")
# Line 1
# Line 2
# Line 3
```

## String Properties

```python
text = "Python"

# Length
len(text)  # 6

# Check content
text.isalpha()    # True (all letters)
text.isdigit()    # False (not all digits)
text.isalnum()    # True (letters and/or numbers)

# Check case
text.isupper()    # False
text.islower()    # False
```

## Common Patterns

### Get and convert input

```python
# Get number from user
age = int(input("Enter age: "))

# Get decimal from user
price = float(input("Enter price: "))

# Get multiple values
name = input("Name: ")
age = int(input("Age: "))
```

### Build formatted output

```python
name = input("Enter name: ")
score = int(input("Enter score: "))
print(f"{name} scored {score} points!")
```

### Process strings

```python
text = input("Enter text: ")
# Make uppercase and strip whitespace
processed = text.strip().upper()
print(f"Processed: {processed}")
```

## Common Mistakes

```python
# ❌ Wrong: Forgetting to convert input
age = input("Enter age: ")
next_year = age + 1  # Error! age is string

# ✅ Correct
age = int(input("Enter age: "))
next_year = age + 1

# ❌ Wrong: Mixing + with string and number
print("Age: " + age)  # Error if age is int

# ✅ Correct: Convert to string or use f-string
print("Age: " + str(age))
print(f"Age: {age}")
```

## Quick Examples

```python
# Interactive calculator
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
result = num1 + num2
print(f"{num1} + {num2} = {result}")

# Name formatter
first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
print(f"Full name: {first} {last}")

# String analyzer
text = input("Enter text: ")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Word count: {len(text.split())}")
```
