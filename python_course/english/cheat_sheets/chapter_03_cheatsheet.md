# Chapter 3: Making Decisions - Quick Reference

## Boolean Values

```python
is_student = True
is_admin = False

# Boolean from expressions
age = 25
can_vote = age >= 18  # True
```

## Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

## If Statements

```python
# Simple if
if age >= 18:
    print("You can vote")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## Logical Operators

### AND - Both conditions must be True

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR - At least one condition must be True

```python
if age < 13 or age > 65:
    print("Discounted ticket")
```

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT - Reverses the boolean value

```python
is_raining = False
if not is_raining:
    print("Go outside")
```

| A | not A |
|---|-------|
| True | False |
| False | True |

## Combining Conditions

```python
# Multiple conditions with parentheses
if (age >= 18 and has_license) or has_permit:
    print("Can drive")

# Complex logic
if age >= 18 and (is_student or is_senior):
    print("Eligible for discount")
```

## Truthy and Falsy Values

**Falsy values** (evaluate to False):
- `False`
- `0`, `0.0`
- `""` (empty string)
- `None`
- `[]` (empty list)
- `{}` (empty dict)

**Truthy values** (everything else):
- `True`
- Non-zero numbers: `1`, `-5`, `3.14`
- Non-empty strings: `"hello"`
- Non-empty collections: `[1, 2]`, `{"a": 1}`

```python
name = input("Enter name: ")
if name:  # True if name is not empty
    print(f"Hello, {name}")
else:
    print("No name entered")
```

## Nested Conditionals

```python
if age >= 18:
    if has_ticket:
        print("Enjoy the movie!")
    else:
        print("Please buy a ticket")
else:
    if is_with_parent:
        print("Needs parental guidance")
    else:
        print("Too young")
```

## Conditional Expressions (Ternary)

```python
# Shorthand for simple if-else
status = "Adult" if age >= 18 else "Minor"

# Traditional equivalent:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

## Membership Operators

```python
# Check if value is in a sequence
if "a" in "cat":  # True
    print("Contains 'a'")

if "x" not in "cat":  # True
    print("Doesn't contain 'x'")
```

## Identity Operators

```python
# Check if two variables reference same object
x = None
if x is None:
    print("x is None")

if x is not None:
    print("x has a value")
```

## Common Patterns

### Validate input

```python
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("Minor")
else:
    print("Adult")
```

### Check ranges

```python
score = int(input("Enter score: "))
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Score must be 0-100")
```

### Multiple conditions

```python
if username and password and len(password) >= 8:
    print("Valid credentials")
else:
    print("Invalid credentials")
```

## Common Mistakes

```python
# ❌ Wrong: Using = instead of ==
if age = 18:  # Error! This is assignment
    print("18 years old")

# ✅ Correct
if age == 18:
    print("18 years old")

# ❌ Wrong: Incorrect range check
if 0 < age < 18:  # Syntax is correct, but...
# ✅ Correct and more readable
if age > 0 and age < 18:
if 0 < age < 18:  # This actually works in Python!

# ❌ Wrong: Missing colon
if age >= 18
    print("Adult")

# ✅ Correct
if age >= 18:
    print("Adult")

# ❌ Wrong: Inconsistent indentation
if age >= 18:
print("Adult")  # Error!

# ✅ Correct (4 spaces indentation)
if age >= 18:
    print("Adult")
```

## Quick Examples

```python
# Grade calculator
score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Login validator
username = input("Username: ")
password = input("Password: ")

if not username:
    print("Username required")
elif not password:
    print("Password required")
elif len(password) < 8:
    print("Password too short")
else:
    print("Login successful")

# Discount calculator
age = int(input("Enter age: "))
is_student = input("Student? (yes/no): ").lower() == "yes"

if age < 12 or age > 65:
    discount = 0.50  # 50% off
elif is_student:
    discount = 0.25  # 25% off
else:
    discount = 0.0   # No discount

print(f"Discount: {discount * 100}%")
```

## Comparison Chaining

```python
# Python allows chaining comparisons
if 0 <= age < 18:
    print("Minor")

if 18 <= age <= 65:
    print("Adult")

# Equivalent to:
if age >= 0 and age < 18:
    print("Minor")
```
