# Chapter 4: Loops - Quick Reference

## While Loops

### Basic While Loop

```python
# Loop while condition is True
count = 0
while count < 5:
    print(count)
    count += 1  # Must update to avoid infinite loop!
# Output: 0 1 2 3 4
```

### While with User Input

```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

### Infinite Loops (Be Careful!)

```python
# ❌ Will run forever!
while True:
    print("Forever")  # No way to exit!

# ✅ Use break to exit
while True:
    response = input("Continue? (yes/no): ")
    if response == "no":
        break
```

## For Loops

### Iterate Over Range

```python
# Loop 5 times (0 to 4)
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Range with start and stop
for i in range(2, 6):
    print(i)
# Output: 2 3 4 5

# Range with step
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8
```

### Iterate Over String

```python
for char in "Python":
    print(char)
# Output: P y t h o n (each on new line)
```

### Iterate Over List

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

## The range() Function

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 8)      # 2, 3, 4, 5, 6, 7
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Convert to list to see values
list(range(5))   # [0, 1, 2, 3, 4]
```

## Break Statement

**Exits the loop immediately**

```python
# Find first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Found: {num}")
        break  # Exit loop
# Output: Found: 7

# Exit on user command
while True:
    command = input("Enter 'quit' to exit: ")
    if command == "quit":
        break
    print(f"You entered: {command}")
```

## Continue Statement

**Skip to next iteration**

```python
# Print only odd numbers
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# Output: 1 3 5 7 9

# Skip empty inputs
while True:
    name = input("Enter name (or 'done'): ")
    if name == "done":
        break
    if not name:
        continue  # Skip empty input
    print(f"Hello, {name}")
```

## Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each row

# Pattern printing
for row in range(5):
    for col in range(row + 1):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****
```

## Loop Patterns

### Accumulator Pattern

```python
# Sum numbers from 1 to 10
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")  # Sum: 55
```

### Counter Pattern

```python
# Count positive numbers
numbers = [5, -2, 8, -7, 3]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(f"Positive count: {count}")  # 3
```

### Find Maximum

```python
# Find largest number
numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum: {max_num}")  # 9
```

### Validation Loop

```python
# Keep asking until valid input
while True:
    age = int(input("Enter age (0-120): "))
    if 0 <= age <= 120:
        break
    print("Invalid age!")
print(f"Your age: {age}")
```

## Loop with Else

**else block runs if loop completes normally (no break)**

```python
# Search for a value
numbers = [1, 2, 3, 4, 5]
target = 6

for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found")  # This runs if no break
# Output: Not found
```

## Enumerate (with index)

```python
fruits = ["apple", "banana", "orange"]

# Get both index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: orange

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. orange
```

## Common Mistakes

```python
# ❌ Wrong: Infinite loop (forgot to update)
count = 0
while count < 5:
    print(count)
    # Missing: count += 1

# ✅ Correct
count = 0
while count < 5:
    print(count)
    count += 1

# ❌ Wrong: Modifying loop variable
for i in range(5):
    i += 1  # Doesn't affect loop!
    print(i)

# ✅ Correct: Use while if you need to control variable
i = 0
while i < 5:
    i += 1
    print(i)

# ❌ Wrong: Using range with float
for i in range(1.5, 5.5):  # Error!
    print(i)

# ✅ Correct: Use while for floats
i = 1.5
while i < 5.5:
    print(i)
    i += 1.0
```

## While vs For

**Use while when:**
- You don't know how many iterations needed
- Looping until a condition changes
- Waiting for user input

```python
# Unknown iterations
while password != "correct":
    password = input("Password: ")
```

**Use for when:**
- You know the number of iterations
- Iterating over a sequence
- Using range with known values

```python
# Known iterations
for i in range(10):
    print(i)
```

## Quick Examples

```python
# Countdown timer
for i in range(5, 0, -1):
    print(f"{i}...")
print("Blast off!")

# Calculate factorial
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")  # 5! = 120

# Menu system
while True:
    print("\n1. Start")
    print("2. Options")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        print("Starting...")
    elif choice == "2":
        print("Options...")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

# Guess the number
secret = 7
attempts = 0
while True:
    guess = int(input("Guess (1-10): "))
    attempts += 1
    if guess == secret:
        print(f"Correct! Took {attempts} attempts")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

# Sum of even numbers
total = 0
for num in range(2, 21, 2):
    total += num
print(f"Sum of even numbers 2-20: {total}")
```

## Loop Control Summary

| Statement | Effect |
|-----------|--------|
| `break` | Exit loop immediately |
| `continue` | Skip to next iteration |
| `pass` | Do nothing (placeholder) |

```python
# pass as placeholder
for i in range(5):
    if i == 2:
        pass  # TODO: implement later
    else:
        print(i)
```
