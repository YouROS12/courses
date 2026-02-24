# Frequently Asked Questions (FAQ) and Troubleshooting

## Table of Contents

- [Getting Started](#getting-started)
- [Technical Issues](#technical-issues)
- [Python Basics](#python-basics)
- [Common Errors](#common-errors)
- [Course Content](#course-content)
- [Best Practices](#best-practices)
- [Platform-Specific](#platform-specific)

---

## Getting Started

### Q: Do I need any programming experience to take this course?

**A:** No! This course is designed for complete beginners. We start from the very basics and build up gradually.

### Q: What do I need to install?

**A:** Nothing! You can use Google Colab (free, browser-based) for all exercises. If you prefer working locally, you'll need Python 3.7+ and Jupyter Notebook. See [GETTING_STARTED.md](GETTING_STARTED.md) for details.

### Q: How long does it take to complete the course?

**A:** It depends on your pace:
- **Intensive**: 2 weeks (2-3 hours/day)
- **Balanced**: 6-8 weeks (4-6 hours/week)
- **Relaxed**: 10-12 weeks (2-3 hours/week)

### Q: Can I skip chapters if I already know some Python?

**A:** Yes! Take the [Pre-Assessment Test](pre_assessment/) to see which chapters you can skip. However, we recommend at least skimming each chapter to ensure you haven't missed anything.

### Q: Which Python version should I use?

**A:** Python 3.7 or higher. All course materials work with Python 3.7+. We recommend using the latest stable version (Python 3.11 or 3.12 as of 2025).

---

## Technical Issues

### Q: Google Colab says "Session disconnected" - did I lose my work?

**A:** No! Your work is automatically saved to Google Drive. Just click "Reconnect" and your code will still be there.

**Prevention:**
- Files → Save a copy in Drive (creates a backup)
- Download notebook periodically (File → Download → .ipynb)
- Session timeout is 90 minutes of inactivity

### Q: My Python code works in Colab but not locally (or vice versa)

**A:** Common causes:

1. **Different Python versions**
   ```bash
   # Check your version
   python --version  # or python3 --version
   ```

2. **Missing packages**
   ```bash
   # Install course requirements
   pip install -r requirements.txt
   ```

3. **File paths** - Colab uses Linux paths, Windows uses backslashes
   ```python
   # Use os.path.join for cross-platform compatibility
   import os
   path = os.path.join("folder", "file.txt")
   ```

### Q: Jupyter Notebook won't start

**A:** Try these solutions:

```bash
# 1. Reinstall Jupyter
pip uninstall jupyter notebook
pip install jupyter notebook

# 2. Try running with Python explicitly
python -m notebook

# 3. Check if another instance is running
# Close all terminal windows and try again

# 4. Specify a port
jupyter notebook --port=8889
```

### Q: `pip install` doesn't work

**A:** Try these alternatives:

```bash
# If using Python 3 explicitly
pip3 install package_name

# Or use Python module
python -m pip install package_name
python3 -m pip install package_name

# On Windows, might need:
py -m pip install package_name

# If permission denied (Linux/Mac)
pip install --user package_name
```

---

## Python Basics

### Q: What's the difference between `=`, `==`, and `===`?

**A:**
- `=` is **assignment**: `x = 5` (sets x to 5)
- `==` is **comparison**: `x == 5` (checks if x equals 5)
- `===` **doesn't exist in Python** (you might be thinking of JavaScript)

### Q: When should I use single quotes vs double quotes for strings?

**A:** It doesn't matter in Python! These are identical:
```python
name = "Alice"
name = 'Alice'
```

**Best practice:** Be consistent. Use double quotes for text and single quotes for single characters or when the text contains quotes:
```python
message = "He said 'Hello'"  # Easier than escaping
char = 'a'
```

### Q: What's the difference between `print()` and `return`?

**A:**
- `print()` displays text in the console (for humans)
- `return` sends a value back from a function (for code)

```python
def add(a, b):
    print(a + b)     # Shows result, returns None
    return a + b     # Sends result back

result = add(3, 5)   # Prints 8
print(result)        # Prints None if only using print()

def add_proper(a, b):
    return a + b     # Returns value

result = add_proper(3, 5)  # result = 8
print(result)              # Prints 8
```

### Q: Why do I sometimes get `None` as output?

**A:** Functions without `return` statement return `None`:

```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement

result = greet("Alice")  # Prints "Hello, Alice"
print(result)            # Prints "None"
```

**Fix:** Add a return statement if you need the value:
```python
def greet(name):
    return f"Hello, {name}"
```

### Q: What's the difference between a list and a tuple?

**A:**

| Feature | List | Tuple |
|---------|------|-------|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutable** | ✅ Can change | ❌ Cannot change |
| **Speed** | Slower | Faster |
| **Use** | General collection | Immutable data, dict keys |

```python
# List - mutable
my_list = [1, 2, 3]
my_list[0] = 10  # OK

# Tuple - immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # Error!
```

---

## Common Errors

### Q: `IndentationError: expected an indented block`

**A:** Python requires consistent indentation (4 spaces recommended):

```python
# ❌ Wrong
if age >= 18:
print("Adult")  # Not indented!

# ✅ Correct
if age >= 18:
    print("Adult")  # 4 spaces
```

**Fix:** Always indent code inside functions, loops, if statements, etc.

### Q: `NameError: name 'x' is not defined`

**A:** You're using a variable before defining it:

```python
# ❌ Wrong
print(name)  # Error! name not defined yet

# ✅ Correct
name = "Alice"
print(name)
```

**Also check for typos:**
```python
user_name = "Alice"
print(username)  # Error! Variable is user_name, not username
```

### Q: `TypeError: can only concatenate str (not "int") to str`

**A:** Can't mix strings and numbers with `+`:

```python
# ❌ Wrong
age = 25
print("Age: " + age)  # Error!

# ✅ Correct - convert to string
print("Age: " + str(age))

# ✅ Better - use f-string
print(f"Age: {age}")
```

### Q: `IndexError: list index out of range`

**A:** You're trying to access an index that doesn't exist:

```python
numbers = [1, 2, 3]  # Indices: 0, 1, 2
print(numbers[3])    # Error! No index 3

# ✅ Check length first
if len(numbers) > 3:
    print(numbers[3])

# Or use try-except
try:
    print(numbers[3])
except IndexError:
    print("Index doesn't exist")
```

### Q: `KeyError: 'key'`

**A:** Dictionary key doesn't exist:

```python
person = {"name": "Alice"}
print(person["age"])  # Error! No 'age' key

# ✅ Use .get() method
age = person.get("age", 0)  # Returns 0 if not found

# ✅ Or check first
if "age" in person:
    print(person["age"])
```

### Q: `SyntaxError: invalid syntax`

**A:** Common causes:

```python
# Missing colon
if age >= 18
    print("Adult")  # Error! Missing : after if

# Correct:
if age >= 18:
    print("Adult")

# Wrong quotes
name = "Alice'  # Mismatched quotes

# Correct:
name = "Alice"

# Missing parentheses
print "Hello"  # Python 2 syntax

# Correct (Python 3):
print("Hello")
```

### Q: `ValueError: invalid literal for int() with base 10`

**A:** Trying to convert non-numeric string to number:

```python
age = int("abc")  # Error! "abc" is not a number

# ✅ Validate input
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number")
    age = 0
```

---

## Course Content

### Q: I don't understand a concept. What should I do?

**A:**

1. **Reread the chapter** - sometimes it clicks the second time
2. **Run the examples yourself** - type them out, don't copy-paste
3. **Modify the examples** - see what happens when you change things
4. **Check the cheat sheet** - quick reference for syntax
5. **Take a break** - come back with fresh eyes
6. **Try explaining it** - teach someone else or write it down
7. **Look at the examples** in the practice notebook
8. **Search online** - Python.org, Real Python, Stack Overflow

### Q: Should I memorize all the syntax?

**A:** No! Focus on understanding concepts. Keep the cheat sheets handy for syntax reference. With practice, you'll naturally remember the common patterns.

**Do memorize:**
- Basic syntax (if, for, def)
- Common patterns

**Don't memorize:**
- All methods and their exact syntax
- Exact error messages
- Obscure features you rarely use

### Q: The exercises are too hard. What should I do?

**A:**

1. **Break down the problem** - solve one small part at a time
2. **Start simpler** - create an easier version first
3. **Review examples** - look at similar problems in the chapter
4. **Use print() statements** - see what your code is doing
5. **Comment your plan** - write what you want to do before coding
6. **Ask for help** - explain the problem to someone

### Q: I finished a chapter. Should I move on or practice more?

**A:**

**Move on if:**
- ✅ You completed all exercises
- ✅ You understand the key concepts
- ✅ You can explain it to someone else
- ✅ You scored 70%+ on the quiz

**Practice more if:**
- ❌ You struggled with most exercises
- ❌ You copied solutions without understanding
- ❌ You can't explain the concepts
- ❌ You scored below 70% on the quiz

### Q: Are quizzes graded?

**A:** The course is self-paced and self-graded. Quiz answer keys are included for you to check your work. Be honest with yourself!

---

## Best Practices

### Q: How should I practice coding?

**A:**

**Do:**
- ✅ Type every example yourself
- ✅ Experiment by modifying code
- ✅ Start small and build up
- ✅ Code a little bit every day
- ✅ Build small projects
- ✅ Read other people's code

**Don't:**
- ❌ Copy-paste code
- ❌ Just read without coding
- ❌ Skip the exercises
- ❌ Avoid errors
- ❌ Try to memorize everything
- ❌ Give up too quickly

### Q: How do I debug my code?

**A:**

1. **Read the error message** - it tells you what's wrong
2. **Check the line number** - error messages show where the problem is
3. **Use print() statements** - see variable values
4. **Comment out code** - find which part causes the error
5. **Simplify** - make a minimal version that reproduces the error
6. **Check for typos** - variable names, brackets, quotes
7. **Check indentation** - must be consistent

```python
# Debug with print()
def calculate_total(prices):
    total = 0
    for price in prices:
        print(f"Adding {price}, total is now {total}")  # Debug
        total += price
    return total
```

### Q: How do I stay motivated?

**A:**

- **Set small goals** - one chapter at a time
- **Track progress** - use the progress tracker
- **Build projects** - apply what you learn
- **Join communities** - share your progress
- **Take breaks** - avoid burnout
- **Celebrate wins** - finished a chapter? Great!
- **Remember why you started** - what do you want to build?

---

## Platform-Specific

### Windows

**Q: `python` command not found**

**A:** Try `py` instead:
```bash
py --version
py script.py
```

Or add Python to PATH during installation.

**Q: ModuleNotFoundError after installing package**

**A:** Multiple Python installations. Try:
```bash
py -m pip install package_name
```

### macOS

**Q: `python` is Python 2**

**A:** Use `python3` explicitly:
```bash
python3 --version
python3 script.py
pip3 install package_name
```

**Q: Permission denied when installing**

**A:** Use `--user` flag:
```bash
pip3 install --user package_name
```

### Linux

**Q: `pip` not found**

**A:** Install pip:
```bash
sudo apt update
sudo apt install python3-pip
```

**Q: Permission denied**

**A:** Either use `--user` or `sudo` (prefer --user):
```bash
pip3 install --user package_name
# Or with sudo (not recommended)
sudo pip3 install package_name
```

---

## Still Need Help?

If your question isn't answered here:

1. **Check documentation:**
   - [Python Official Docs](https://docs.python.org/3/)
   - [Python Tutorial](https://docs.python.org/3/tutorial/)

2. **Search online:**
   - [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
   - [Real Python](https://realpython.com/)
   - Google your exact error message

3. **Course resources:**
   - [Getting Started Guide](GETTING_STARTED.md)
   - [Cheat Sheets](cheat_sheets/)
   - [Instructor Guide](INSTRUCTOR_GUIDE.md)

---

## Contributing

Found a question that should be here? Spotted an error? Contributions to this FAQ are welcome!

---

*Happy learning! 🐍*
