# Basic Python Practice Problems

Practice problems for Chapters 1-2: Variables, data types, operators, and strings.

---

## Variables and Data Types

### Problem 1: Variable Swap
Write code to swap the values of two variables without using a third variable.

**Hint:** Use tuple unpacking

---

### Problem 2: Type Checker
Create a program that asks the user for input and prints the type of the entered value (as interpreted by Python).

---

### Problem 3: BMI Calculator
Calculate Body Mass Index (BMI) using the formula: BMI = weight(kg) / (height(m))²

Ask user for weight and height, then display the BMI with 2 decimal places.

---

## Arithmetic Operations

### Problem 4: Circle Calculator
Given the radius of a circle, calculate:
- Area (π × r²)
- Circumference (2 × π × r)

Use 3.14159 for π.

---

### Problem 5: Time Converter
Convert a given number of seconds into hours, minutes, and seconds.

Example: 3665 seconds = 1 hour, 1 minute, 5 seconds

**Hint:** Use integer division (//) and modulus (%)

---

### Problem 6: Average of Three
Ask the user for three numbers and calculate their average.

---

### Problem 7: Even or Odd Checker (Without If)
Given a number, determine if it's even or odd using only the modulus operator (%).
Print the result of n % 2 (0 means even, 1 means odd).

---

## String Manipulation

### Problem 8: Name Formatter
Ask for first name and last name separately. Output:
- Full name (First Last)
- Reversed name (Last, First)
- Initials (F.L.)
- All uppercase
- All lowercase

---

### Problem 9: String Statistics
For a given string, calculate and display:
- Total length
- Number of spaces
- Number of uppercase letters
- Number of lowercase letters
- Number of digits

**Hint:** Use string methods like .isupper(), .islower(), .isdigit()

---

### Problem 10: Email Parser
Given an email address like "john.doe@example.com", extract:
- Username (john.doe)
- Domain (example.com)

**Hint:** Use .split('@')

---

### Problem 11: Palindrome Checker (Simple)
Ask the user for a word. Check if it reads the same forwards and backwards.
Don't worry about case or spaces for now (we'll improve this later with if statements).

Just compare: word == word[::-1]

---

### Problem 12: Text Censorship
Replace all occurrences of a "bad word" with asterisks.
Ask user for text and word to censor.

**Hint:** Use .replace()

---

## Mixed Challenges

### Problem 13: Receipt Generator
Create a simple receipt calculator:
- Ask for item name and price (3 items)
- Calculate subtotal
- Calculate tax (8%)
- Calculate total

Format output nicely:
```
Item 1: Pizza         $12.99
Item 2: Drink         $ 2.50
Item 3: Dessert       $ 5.99
              ---------------
Subtotal:             $21.48
Tax (8%):             $ 1.72
Total:                $23.20
```

---

### Problem 14: Temperature Converter
Convert between Celsius and Fahrenheit:
- Celsius to Fahrenheit: F = C × 9/5 + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9

Ask the user for temperature and which direction to convert.

---

### Problem 15: Mad Libs Generator
Create a short story with blanks. Ask the user for:
- A noun
- A verb
- An adjective
- An adverb

Then print a story using their words.

Example: "The [adjective] [noun] [adverb] [verb]s across the room."

---

## Solutions

<details>
<summary>Click to reveal solutions</summary>

### Solution 1: Variable Swap
```python
a = 5
b = 10
print(f"Before: a={a}, b={b}")

a, b = b, a

print(f"After: a={a}, b={b}")
```

### Solution 2: Type Checker
```python
user_input = input("Enter something: ")
print(f"Type: {type(user_input)}")

# Note: input() always returns string
# For actual type checking, try converting:
try:
    num = int(user_input)
    print("It's an integer!")
except:
    print("It's a string!")
```

### Solution 3: BMI Calculator
```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
```

### Solution 4: Circle Calculator
```python
radius = float(input("Enter radius: "))
pi = 3.14159

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

### Solution 5: Time Converter
```python
total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")
```

### Solution 6: Average of Three
```python
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))

average = (num1 + num2 + num3) / 3
print(f"Average: {average:.2f}")
```

### Solution 7: Even or Odd Checker
```python
number = int(input("Enter a number: "))
result = number % 2
print(f"Result: {result} (0=even, 1=odd)")
```

### Solution 8: Name Formatter
```python
first = input("First name: ")
last = input("Last name: ")

print(f"Full name: {first} {last}")
print(f"Reversed: {last}, {first}")
print(f"Initials: {first[0]}.{last[0]}.")
print(f"Uppercase: {first.upper()} {last.upper()}")
print(f"Lowercase: {first.lower()} {last.lower()}")
```

### Solution 9: String Statistics
```python
text = input("Enter text: ")

length = len(text)
spaces = text.count(' ')
uppercase = sum(1 for c in text if c.isupper())
lowercase = sum(1 for c in text if c.islower())
digits = sum(1 for c in text if c.isdigit())

print(f"Length: {length}")
print(f"Spaces: {spaces}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digits}")
```

### Solution 10: Email Parser
```python
email = input("Enter email: ")
parts = email.split('@')
username = parts[0]
domain = parts[1]

print(f"Username: {username}")
print(f"Domain: {domain}")
```

### Solution 11: Palindrome Checker
```python
word = input("Enter a word: ").lower()
reversed_word = word[::-1]
is_palindrome = (word == reversed_word)

print(f"Is palindrome: {is_palindrome}")
```

### Solution 12: Text Censorship
```python
text = input("Enter text: ")
bad_word = input("Word to censor: ")
censored = text.replace(bad_word, "*" * len(bad_word))

print(f"Censored: {censored}")
```

### Solution 13: Receipt Generator
```python
item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: "))

item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: "))

item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: "))

subtotal = price1 + price2 + price3
tax = subtotal * 0.08
total = subtotal + tax

print("\n" + "="*30)
print(f"{item1:20} ${price1:>7.2f}")
print(f"{item2:20} ${price2:>7.2f}")
print(f"{item3:20} ${price3:>7.2f}")
print(" "*20 + "-"*10)
print(f"{'Subtotal':20} ${subtotal:>7.2f}")
print(f"{'Tax (8%)':20} ${tax:>7.2f}")
print(f"{'Total':20} ${total:>7.2f}")
print("="*30)
```

### Solution 14: Temperature Converter
```python
temp = float(input("Enter temperature: "))
direction = input("Convert to (F)ahrenheit or (C)elsius? ").upper()

if direction == 'F':
    result = temp * 9/5 + 32
    print(f"{temp}°C = {result:.2f}°F")
else:
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.2f}°C")
```

### Solution 15: Mad Libs Generator
```python
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

story = f"""
Once upon a time, there was a {adjective} {noun}.
Every day, it would {adverb} {verb} across the meadow.
The other {noun}s were amazed by how {adverb} it could {verb}.
The end.
"""

print(story)
```

</details>

---

*Great work on practicing the basics! Move on to control flow problems next. 🐍*
