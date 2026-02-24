# Chapter 9: File I/O - Quick Reference

## Opening and Closing Files

```python
# Open file
file = open("data.txt", "r")
content = file.read()
file.close()  # Always close!

# Better: Using context manager (auto-closes)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed here
```

## File Modes

| Mode | Description | Creates File | Overwrites |
|------|-------------|--------------|------------|
| `'r'` | Read (default) | ❌ No | N/A |
| `'w'` | Write | ✅ Yes | ✅ Yes |
| `'a'` | Append | ✅ Yes | ❌ No |
| `'x'` | Exclusive create | ✅ Yes | Error if exists |
| `'r+'` | Read + Write | ❌ No | Partial |
| `'w+'` | Write + Read | ✅ Yes | ✅ Yes |
| `'a+'` | Append + Read | ✅ Yes | ❌ No |

```python
# Read mode (file must exist)
with open("data.txt", "r") as file:
    content = file.read()

# Write mode (creates or overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Append mode (adds to end)
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

## Reading Files

### read() - Read entire file

```python
with open("data.txt", "r") as file:
    content = file.read()  # Returns string
    print(content)
```

### readline() - Read one line

```python
with open("data.txt", "r") as file:
    line1 = file.readline()  # First line
    line2 = file.readline()  # Second line
    print(line1)
    print(line2)
```

### readlines() - Read all lines as list

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of strings
    for line in lines:
        print(line.strip())  # Remove \n
```

### Iterate over file (best for large files)

```python
with open("data.txt", "r") as file:
    for line in file:  # Memory efficient!
        print(line.strip())
```

## Writing Files

### write() - Write string

```python
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

### writelines() - Write list of strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### print() to file

```python
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)
    print("Second line", file=file)
```

## File Paths

```python
import os

# Current working directory
cwd = os.getcwd()
print(cwd)

# Join paths (works on any OS)
path = os.path.join("folder", "subfolder", "file.txt")

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists")

# Check if path is a file
os.path.isfile("data.txt")  # True

# Check if path is a directory
os.path.isdir("folder")  # True

# Get absolute path
abs_path = os.path.abspath("data.txt")

# Get file name from path
filename = os.path.basename("/path/to/file.txt")  # "file.txt"

# Get directory from path
dirname = os.path.dirname("/path/to/file.txt")  # "/path/to"
```

## Working with CSV Files

```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Get header row
    for row in csv_reader:
        print(row)  # Each row is a list

# Reading CSV as dictionary
with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row["name"])  # Access by column name

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"]
]

with open("output.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Writing CSV from dictionaries
data = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

## Working with JSON Files

```python
import json

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)  # Returns dict or list
    print(data["name"])

# Writing JSON
data = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "CS", "Physics"]
}

with open("output.json", "w") as file:
    json.dump(data, file)

# Pretty print JSON
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# JSON string to Python
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)  # Dict

# Python to JSON string
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)  # String
json_pretty = json.dumps(data, indent=4)  # Pretty string
```

## Exception Handling with Files

```python
# Handle file not found
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")

# Check before opening
import os
if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        content = file.read()
else:
    print("File does not exist")
```

## Common File Patterns

### Read and process each line

```python
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = float(line.strip())
        total += number
print(f"Total: {total}")
```

### Count lines

```python
with open("data.txt", "r") as file:
    line_count = sum(1 for line in file)
print(f"Lines: {line_count}")

# Or using readlines
with open("data.txt", "r") as file:
    line_count = len(file.readlines())
```

### Read file into list

```python
# Read all lines (with newlines)
with open("data.txt", "r") as file:
    lines = file.readlines()

# Read all lines (without newlines)
with open("data.txt", "r") as file:
    lines = [line.strip() for line in file]

# Or
with open("data.txt", "r") as file:
    lines = file.read().splitlines()
```

### Copy file

```python
with open("source.txt", "r") as source:
    with open("destination.txt", "w") as dest:
        dest.write(source.read())

# Or line by line (memory efficient)
with open("source.txt", "r") as source:
    with open("destination.txt", "w") as dest:
        for line in source:
            dest.write(line)
```

### Append to file

```python
with open("log.txt", "a") as file:
    file.write("New entry\n")

# Append with timestamp
from datetime import datetime
with open("log.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Event occurred\n")
```

### Read CSV and filter

```python
import csv

filtered_data = []
with open("students.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if int(row["age"]) >= 18:
            filtered_data.append(row)

# Write filtered data
with open("adults.csv", "w", newline="") as file:
    if filtered_data:
        fieldnames = filtered_data[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(filtered_data)
```

### Update JSON file

```python
import json

# Read
with open("data.json", "r") as file:
    data = json.load(file)

# Modify
data["last_updated"] = "2025-01-01"
data["count"] = data.get("count", 0) + 1

# Write back
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

## Binary Files

```python
# Read binary file
with open("image.png", "rb") as file:  # 'rb' = read binary
    binary_data = file.read()

# Write binary file
with open("copy.png", "wb") as file:  # 'wb' = write binary
    file.write(binary_data)

# Copy binary file
with open("source.png", "rb") as source:
    with open("destination.png", "wb") as dest:
        dest.write(source.read())
```

## Directory Operations

```python
import os

# List files in directory
files = os.listdir(".")  # Current directory
print(files)

# List only .txt files
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]

# Create directory
os.mkdir("new_folder")

# Create nested directories
os.makedirs("path/to/new/folder")

# Remove file
os.remove("file.txt")

# Remove directory
os.rmdir("folder")  # Must be empty

# Rename file
os.rename("old_name.txt", "new_name.txt")

# Check if directory exists
if not os.path.exists("folder"):
    os.mkdir("folder")
```

## Common Mistakes

```python
# ❌ Wrong: Forgetting to close file
file = open("data.txt", "r")
content = file.read()
# Forgot file.close()!

# ✅ Correct: Use context manager
with open("data.txt", "r") as file:
    content = file.read()
# Auto-closed

# ❌ Wrong: Reading closed file
with open("data.txt", "r") as file:
    pass
content = file.read()  # Error! File is closed

# ✅ Correct: Read inside context
with open("data.txt", "r") as file:
    content = file.read()
print(content)  # OK

# ❌ Wrong: Writing without newlines
with open("data.txt", "w") as file:
    file.write("Line 1")
    file.write("Line 2")  # Will be "Line 1Line 2"

# ✅ Correct: Add newlines
with open("data.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

# ❌ Wrong: Not handling file not found
with open("missing.txt", "r") as file:  # Error!
    content = file.read()

# ✅ Correct: Handle exception or check existence
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

## Quick Examples

```python
# Word counter
with open("document.txt", "r") as file:
    text = file.read()
    words = text.split()
    print(f"Word count: {len(words)}")

# Find and replace in file
with open("data.txt", "r") as file:
    content = file.read()

content = content.replace("old_word", "new_word")

with open("data.txt", "w") as file:
    file.write(content)

# Save list to file
my_list = ["apple", "banana", "orange"]
with open("fruits.txt", "w") as file:
    for fruit in my_list:
        file.write(f"{fruit}\n")

# Load list from file
fruits = []
with open("fruits.txt", "r") as file:
    for line in file:
        fruits.append(line.strip())

# Save dictionary to JSON
person = {"name": "Alice", "age": 25, "city": "NYC"}
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Load dictionary from JSON
with open("person.json", "r") as file:
    person = json.load(file)
print(person["name"])

# Process large CSV file
import csv
total_sales = 0
with open("sales.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        total_sales += float(row["amount"])
print(f"Total sales: ${total_sales:.2f}")
```

## File Encoding

```python
# Specify encoding (important for non-ASCII text)
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Writing with encoding
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 世界!")  # Chinese characters
```
