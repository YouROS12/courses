# Python Pre-Assessment Test

**Time Limit:** 30 minutes
**Questions:** 20
**Instructions:** Answer all questions to the best of your ability. Don't look up answers!

---

## Section 1: Basic Concepts (Questions 1-5)

### Question 1
What is the output of this code?
```python
x = 5
y = 2
print(x // y)
```
- A) 2.5
- B) 2
- C) 3
- D) Error

**Your answer:** ______

---

### Question 2
Which of the following is NOT a valid variable name in Python?
- A) `my_var`
- B) `_private`
- C) `2nd_place`
- D) `myVar2`

**Your answer:** ______

---

### Question 3
What does this code print?
```python
text = "Python"
print(text[1:4])
```
- A) Pyt
- B) yth
- C) Pyth
- D) ytho

**Your answer:** ______

---

### Question 4
How do you get user input in Python?
- A) `get_input()`
- B) `read()`
- C) `input()`
- D) `scanf()`

**Your answer:** ______

---

### Question 5
What is the result of `"3" + "3"` in Python?
- A) 6
- B) 33
- C) "6"
- D) "33"

**Your answer:** ______

---

## Section 2: Control Flow (Questions 6-10)

### Question 6
What will this code print?
```python
x = 10
if x > 5:
    print("A")
elif x > 15:
    print("B")
else:
    print("C")
```
- A) A
- B) B
- C) C
- D) AB

**Your answer:** ______

---

### Question 7
How many times will this loop run?
```python
for i in range(3):
    print(i)
```
- A) 2 times
- B) 3 times
- C) 4 times
- D) Infinite

**Your answer:** ______

---

### Question 8
What is the output?
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
- A) 0 1 2
- B) 0 1 2 3
- C) 1 2 3
- D) Infinite loop

**Your answer:** ______

---

### Question 9
Which operator means "not equal to"?
- A) `!=`
- B) `<>`
- C) `/=`
- D) `!==`

**Your answer:** ______

---

### Question 10
What does `break` do in a loop?
- A) Pauses the loop
- B) Exits the loop
- C) Skips to next iteration
- D) Restarts the loop

**Your answer:** ______

---

## Section 3: Data Structures (Questions 11-15)

### Question 11
What is the output?
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])
```
- A) 1
- B) 5
- C) -1
- D) Error

**Your answer:** ______

---

### Question 12
How do you add an item to the end of a list?
- A) `list.add(item)`
- B) `list.append(item)`
- C) `list.insert(item)`
- D) `list.push(item)`

**Your answer:** ______

---

### Question 13
What is the output?
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
```
- A) Alice
- B) "Alice"
- C) name
- D) Error

**Your answer:** ______

---

### Question 14
Which data structure does NOT allow duplicate values?
- A) List
- B) Tuple
- C) Set
- D) Dictionary

**Your answer:** ______

---

### Question 15
How do you create an empty dictionary?
- A) `dict = []`
- B) `dict = {}`
- C) `dict = ()`
- D) `dict = set()`

**Your answer:** ______

---

## Section 4: Functions and Advanced (Questions 16-20)

### Question 16
What does this function return?
```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
```
- A) 7
- B) 12
- C) 34
- D) None

**Your answer:** ______

---

### Question 17
What is the correct way to define a function in Python?
- A) `function myFunc():`
- B) `def myFunc():`
- C) `func myFunc():`
- D) `define myFunc():`

**Your answer:** ______

---

### Question 18
How do you open a file for reading in Python?
- A) `file = open("data.txt", "r")`
- B) `file = read("data.txt")`
- C) `file = open("data.txt", "read")`
- D) `file = File("data.txt")`

**Your answer:** ______

---

### Question 19
What does this code do?
```python
try:
    x = int("hello")
except ValueError:
    print("Error!")
```
- A) Crashes with error
- B) Prints "Error!"
- C) Prints "hello"
- D) Does nothing

**Your answer:** ______

---

### Question 20
What is the output?
```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)
```
- A) [1, 2, 3, 4, 5]
- B) 15
- C) 12345
- D) Error

**Your answer:** ______

---

## Answer Key

<details>
<summary>Click to reveal answers (only after completing the test!)</summary>

1. **B** - `//` is floor division, 5 // 2 = 2
2. **C** - Variable names cannot start with a number
3. **B** - Slicing [1:4] gets indices 1, 2, 3 (not including 4) = "yth"
4. **C** - `input()` is the function to get user input
5. **D** - String concatenation: "3" + "3" = "33"
6. **A** - First condition (x > 5) is True, so prints "A" and stops
7. **B** - range(3) gives 0, 1, 2 (3 values)
8. **A** - Prints 0, 1, 2 (while count is less than 3)
9. **A** - `!=` means not equal to
10. **B** - `break` exits the loop completely
11. **B** - Negative indexing: -1 is the last element (5)
12. **B** - `.append()` adds item to end of list
13. **A** - Accessing dictionary value by key returns "Alice" (without quotes in output)
14. **C** - Sets automatically remove duplicates
15. **B** - `{}` creates an empty dictionary
16. **B** - 3 * 4 = 12
17. **B** - `def` keyword defines a function
18. **A** - `open(filename, "r")` opens file for reading
19. **B** - Try-except catches the ValueError and prints "Error!"
20. **B** - sum([1,2,3,4,5]) = 15

</details>

---

## Detailed Explanations

<details>
<summary>Click for detailed explanations of each answer</summary>

### Question 1 Explanation
The `//` operator performs **floor division** (integer division), which divides and rounds down to the nearest integer. 5 // 2 = 2.5 rounded down = 2.

**Related topics:** Chapter 1 (Operators)

### Question 2 Explanation
Variable names must start with a letter or underscore, never a number. `2nd_place` starts with a number, making it invalid.

**Related topics:** Chapter 1 (Variables)

### Question 3 Explanation
String slicing `[start:end]` includes the start index but excludes the end index. `text[1:4]` gets characters at indices 1, 2, and 3, which are "y", "t", "h".

**Related topics:** Chapter 2 (String Slicing)

### Question 4 Explanation
The `input()` function is used to get user input in Python. It always returns a string.

**Related topics:** Chapter 2 (User Input)

### Question 5 Explanation
When using `+` with strings, Python concatenates them. "3" + "3" = "33" (both are strings, not numbers).

**Related topics:** Chapter 2 (String Operations)

### Question 6 Explanation
In if-elif-else chains, Python stops at the **first True condition**. Since `x > 5` is True, it prints "A" and doesn't check the elif.

**Related topics:** Chapter 3 (Conditionals)

### Question 7 Explanation
`range(3)` produces 0, 1, 2 (three values). The loop runs once for each value, so 3 times.

**Related topics:** Chapter 4 (Loops)

### Question 8 Explanation
The loop runs while count < 3. It prints 0, then 1, then 2, then count becomes 3 and the condition becomes False.

**Related topics:** Chapter 4 (While Loops)

### Question 9 Explanation
The `!=` operator checks if two values are not equal. It's the opposite of `==` (equal to).

**Related topics:** Chapter 3 (Comparison Operators)

### Question 10 Explanation
`break` immediately exits the loop, regardless of the loop condition. The program continues after the loop.

**Related topics:** Chapter 4 (Break Statement)

### Question 11 Explanation
Negative indexing counts from the end: -1 is the last element, -2 is second-to-last, etc. So `my_list[-1]` is 5.

**Related topics:** Chapter 5 (Lists)

### Question 12 Explanation
The `.append()` method adds an element to the end of a list. Other options don't exist or work differently.

**Related topics:** Chapter 5 (List Methods)

### Question 13 Explanation
Accessing a dictionary with a key returns the corresponding value. `my_dict["name"]` returns the string Alice.

**Related topics:** Chapter 6 (Dictionaries)

### Question 14 Explanation
Sets automatically maintain uniqueness - if you try to add a duplicate, it's ignored. Lists, tuples, and dictionaries (values) can have duplicates.

**Related topics:** Chapter 8 (Sets)

### Question 15 Explanation
`{}` creates an empty dictionary. `[]` is an empty list, `()` is an empty tuple, and `set()` creates an empty set.

**Related topics:** Chapter 6 (Dictionaries)

### Question 16 Explanation
The function multiplies 3 * 4 and returns 12. The `return` statement sends this value back to the caller.

**Related topics:** Chapter 7 (Functions)

### Question 17 Explanation
Functions in Python are defined using the `def` keyword, followed by the function name and parentheses.

**Related topics:** Chapter 7 (Functions)

### Question 18 Explanation
The `open()` function with "r" mode opens a file for reading. "w" is for writing, "a" is for appending.

**Related topics:** Chapter 9 (File I/O)

### Question 19 Explanation
The try-except block catches errors. When `int("hello")` fails with ValueError, the except block runs and prints "Error!".

**Related topics:** Chapter 10 (Error Handling)

### Question 20 Explanation
The `sum()` function adds up all numbers in a list. sum([1,2,3,4,5]) = 1+2+3+4+5 = 15.

**Related topics:** Chapter 5 (Lists), Built-in Functions

</details>

---

## What to Do After

1. **Count your correct answers** (out of 20)
2. **Calculate percentage** (correct / 20 × 100)
3. **Review missed questions** - understand why you got them wrong
4. **Check the scoring guide** in [README.md](README.md)
5. **Start the course** at the recommended chapter
6. **Retake this test** after completing the course to see your progress!

---

**Your Score:** _____ / 20 (____%)

**Recommended Starting Point:** Chapter _____

**Date Taken:** __________

---

*Remember: This test is just a starting point. Everyone learns at their own pace! 🐍*
