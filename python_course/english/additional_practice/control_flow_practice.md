# Control Flow Practice Problems

Practice problems for Chapters 3-4: Conditionals and loops.

---

## Conditional Statements

### Problem 1: Grade Classifier
Write a program that classifies a grade:
- 90-100: Excellent
- 80-89: Good
- 70-79: Satisfactory
- 60-69: Needs Improvement
- Below 60: Failing

Handle invalid grades (less than 0 or greater than 100).

---

### Problem 2: Leap Year Checker
Determine if a year is a leap year:
- Divisible by 4 AND not divisible by 100, OR
- Divisible by 400

---

### Problem 3: Triangle Validator
Given three side lengths, determine if they can form a valid triangle.
Rule: The sum of any two sides must be greater than the third side.

---

### Problem 4: Discount Calculator
Calculate the final price based on purchase amount:
- Under $50: No discount
- $50-$100: 10% off
- $100-$200: 15% off
- Over $200: 20% off

---

### Problem 5: Password Strength Checker
Check if a password is strong. It must:
- Be at least 8 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit

Print specific feedback for each missing requirement.

**Hint:** Use .isupper(), .islower(), .isdigit()

---

## Simple Loops

### Problem 6: Multiplication Table
Print the multiplication table for a given number (1-10).

Example for 5:
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

### Problem 7: Sum of Numbers
Calculate the sum of all numbers from 1 to N (user provides N).

---

### Problem 8: Factorial Calculator
Calculate the factorial of a number (N!).
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

---

### Problem 9: Countdown Timer
Create a countdown from N to 1, then print "Blast off!"

---

### Problem 10: Number Pyramid
Print a number pyramid:
```
1
12
123
1234
12345
```

**Hint:** Use nested loops or string building

---

## Advanced Loops

### Problem 11: Prime Number Checker
Determine if a number is prime.
Prime numbers are only divisible by 1 and themselves.

**Hint:** Check if any number from 2 to sqrt(n) divides n evenly

---

### Problem 12: Fibonacci Sequence
Generate the first N numbers in the Fibonacci sequence.
Each number is the sum of the previous two.
Start with 0, 1.

Example for N=7: 0, 1, 1, 2, 3, 5, 8

---

### Problem 13: Reverse a Number
Reverse the digits of a number.
Example: 12345 → 54321

**Hint:** Use modulus and integer division in a loop

---

### Problem 14: Digit Sum
Calculate the sum of all digits in a number.
Example: 12345 → 1+2+3+4+5 = 15

---

### Problem 15: Perfect Number Checker
A perfect number equals the sum of its divisors (excluding itself).
Example: 6 = 1 + 2 + 3

Check if a number is perfect.

---

## Pattern Printing

### Problem 16: Right Triangle
Print a right triangle of stars:
```
*
**
***
****
*****
```

---

### Problem 17: Inverted Triangle
Print an inverted triangle:
```
*****
****
***
**
*
```

---

### Problem 18: Pyramid
Print a centered pyramid:
```
    *
   ***
  *****
 *******
*********
```

**Hint:** Combine spaces and stars

---

## Interactive Programs

### Problem 19: Number Guessing Game
Generate a random number between 1 and 100.
Let the user guess until they get it right.
Provide "higher" or "lower" hints.

**Hint:** `import random; number = random.randint(1, 100)`

---

### Problem 20: Menu-Driven Calculator
Create a calculator with a menu:
```
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

Keep running until user chooses Exit.
Handle division by zero.

---

## Solutions

<details>
<summary>Click to reveal solutions</summary>

### Solution 1: Grade Classifier
```python
grade = float(input("Enter grade (0-100): "))

if grade < 0 or grade > 100:
    print("Invalid grade!")
elif grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Satisfactory")
elif grade >= 60:
    print("Needs Improvement")
else:
    print("Failing")
```

### Solution 2: Leap Year Checker
```python
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

### Solution 3: Triangle Validator
```python
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")
```

### Solution 4: Discount Calculator
```python
amount = float(input("Purchase amount: $"))

if amount < 50:
    discount = 0
elif amount < 100:
    discount = 0.10
elif amount < 200:
    discount = 0.15
else:
    discount = 0.20

final_price = amount * (1 - discount)
print(f"Discount: {discount*100}%")
print(f"Final price: ${final_price:.2f}")
```

### Solution 5: Password Strength Checker
```python
password = input("Enter password: ")

is_strong = True
feedback = []

if len(password) < 8:
    is_strong = False
    feedback.append("Must be at least 8 characters")

if not any(c.isupper() for c in password):
    is_strong = False
    feedback.append("Must contain uppercase letter")

if not any(c.islower() for c in password):
    is_strong = False
    feedback.append("Must contain lowercase letter")

if not any(c.isdigit() for c in password):
    is_strong = False
    feedback.append("Must contain a digit")

if is_strong:
    print("Strong password!")
else:
    print("Weak password:")
    for item in feedback:
        print(f"- {item}")
```

### Solution 6: Multiplication Table
```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Solution 7: Sum of Numbers
```python
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of 1 to {n} = {total}")

# Or use formula: total = n * (n + 1) // 2
```

### Solution 8: Factorial Calculator
```python
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
```

### Solution 9: Countdown Timer
```python
n = int(input("Countdown from: "))

for i in range(n, 0, -1):
    print(i)
print("Blast off!")
```

### Solution 10: Number Pyramid
```python
n = int(input("Number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### Solution 11: Prime Number Checker
```python
num = int(input("Enter a number: "))

if num < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
```

### Solution 12: Fibonacci Sequence
```python
n = int(input("How many numbers? "))

a, b = 0, 1
print(a, end=" ")
if n > 1:
    print(b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c

print()  # New line
```

### Solution 13: Reverse a Number
```python
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"Reversed: {reversed_num}")

# Or using string: reversed_num = int(str(num)[::-1])
```

### Solution 14: Digit Sum
```python
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print(f"Sum of digits: {total}")

# Or using string: total = sum(int(d) for d in str(num))
```

### Solution 15: Perfect Number Checker
```python
num = int(input("Enter a number: "))
divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
```

### Solution 16: Right Triangle
```python
n = int(input("Number of rows: "))

for i in range(1, n + 1):
    print("*" * i)
```

### Solution 17: Inverted Triangle
```python
n = int(input("Number of rows: "))

for i in range(n, 0, -1):
    print("*" * i)
```

### Solution 18: Pyramid
```python
n = int(input("Number of rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

### Solution 19: Number Guessing Game
```python
import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You got it in {attempts} attempts!")
        break
    elif guess < number:
        print("Higher!")
    else:
        print("Lower!")
```

### Solution 20: Menu-Driven Calculator
```python
while True:
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {num1 / num2}")
```

</details>

---

*Excellent work! These problems build strong problem-solving skills. 🐍*
