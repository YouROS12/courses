# Chapter 1: Introduction to Python - Quick Reference

## Variables

```python
# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Hello"` | Text/strings |
| `bool` | `True` or `False` | Boolean values |

## Checking Types

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hello")   # <class 'str'>
type(True)      # <class 'bool'>
```

## Arithmetic Operators

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

## Operator Precedence

**PEMDAS** (from highest to lowest):
1. `()` - Parentheses
2. `**` - Exponentiation
3. `*`, `/`, `//`, `%` - Multiplication, Division
4. `+`, `-` - Addition, Subtraction

```python
result = 2 + 3 * 4      # 14 (not 20)
result = (2 + 3) * 4    # 20
```

## Printing Output

```python
print("Hello, World!")
print("Name:", name)
print("Age:", age, "Height:", height)
```

## Comments

```python
# This is a single-line comment

# This is a
# multi-line comment
# using multiple single-line comments
```

## Variable Naming Rules

✅ **Valid**:
- `name`, `age`, `first_name`
- `total_score`, `user_2`
- Start with letter or underscore
- Use letters, numbers, underscores

❌ **Invalid**:
- `2nd_place` (starts with number)
- `first-name` (contains hyphen)
- `class` (reserved keyword)

## Best Practices

- Use descriptive variable names: `user_age` not `x`
- Use lowercase with underscores: `total_count`
- Add comments to explain complex code
- One statement per line
- Use spaces around operators: `x = 5` not `x=5`

## Common Mistakes

```python
# ❌ Wrong: Using undefined variable
print(score)  # Error if score not defined

# ✅ Correct: Define first
score = 100
print(score)

# ❌ Wrong: Mixing types without conversion
age = "25"
next_year = age + 1  # Error

# ✅ Correct: Convert first
age = "25"
next_year = int(age) + 1
```

## Quick Examples

```python
# Calculate area of rectangle
width = 10
height = 5
area = width * height
print("Area:", area)  # Area: 50

# Calculate average
num1 = 85
num2 = 92
num3 = 78
average = (num1 + num2 + num3) / 3
print("Average:", average)  # Average: 85.0
```
