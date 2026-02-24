# Chapitre 9 : Entrées/Sorties Fichiers - Référence Rapide

## Ouvrir et Fermer des Fichiers

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

## Modes de Fichiers

| Mode | Description | Crée Fichier | Écrase |
|------|-------------|--------------|------------|
| `'r'` | Lecture (par défaut) | ❌ Non | N/A |
| `'w'` | Écriture | ✅ Oui | ✅ Oui |
| `'a'` | Ajout | ✅ Oui | ❌ Non |
| `'x'` | Création exclusive | ✅ Oui | Erreur si existe |
| `'r+'` | Lecture + Écriture | ❌ Non | Partiel |
| `'w+'` | Écriture + Lecture | ✅ Oui | ✅ Oui |
| `'a+'` | Ajout + Lecture | ✅ Oui | ❌ Non |

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

## Lire des Fichiers

### read() - Lire le fichier entier

```python
with open("data.txt", "r") as file:
    content = file.read()  # Returns string
    print(content)
```

### readline() - Lire une ligne

```python
with open("data.txt", "r") as file:
    line1 = file.readline()  # First line
    line2 = file.readline()  # Second line
    print(line1)
    print(line2)
```

### readlines() - Lire toutes les lignes en liste

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of strings
    for line in lines:
        print(line.strip())  # Remove \n
```

### Itérer sur le fichier (meilleur pour les gros fichiers)

```python
with open("data.txt", "r") as file:
    for line in file:  # Memory efficient!
        print(line.strip())
```

## Écrire dans des Fichiers

### write() - Écrire une chaîne

```python
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

### writelines() - Écrire une liste de chaînes

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### print() vers un fichier

```python
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)
    print("Second line", file=file)
```

## Chemins de Fichiers

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

## Travailler avec des Fichiers CSV

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

## Travailler avec des Fichiers JSON

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

## Gestion des Exceptions avec les Fichiers

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

## Modèles Courants de Fichiers

### Lire et traiter chaque ligne

```python
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = float(line.strip())
        total += number
print(f"Total: {total}")
```

### Compter les lignes

```python
with open("data.txt", "r") as file:
    line_count = sum(1 for line in file)
print(f"Lines: {line_count}")

# Or using readlines
with open("data.txt", "r") as file:
    line_count = len(file.readlines())
```

### Lire le fichier dans une liste

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

### Copier un fichier

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

### Ajouter à un fichier

```python
with open("log.txt", "a") as file:
    file.write("New entry\n")

# Append with timestamp
from datetime import datetime
with open("log.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Event occurred\n")
```

### Lire CSV et filtrer

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

### Mettre à jour un fichier JSON

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

## Fichiers Binaires

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

## Opérations sur les Répertoires

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

## Erreurs Courantes

```python
# ❌ Incorrect : Oublier de fermer le fichier
file = open("data.txt", "r")
content = file.read()
# Forgot file.close()!

# ✅ Correct : Utiliser un gestionnaire de contexte
with open("data.txt", "r") as file:
    content = file.read()
# Auto-closed

# ❌ Incorrect : Lire un fichier fermé
with open("data.txt", "r") as file:
    pass
content = file.read()  # Error! File is closed

# ✅ Correct : Lire à l'intérieur du contexte
with open("data.txt", "r") as file:
    content = file.read()
print(content)  # OK

# ❌ Incorrect : Écrire sans nouvelles lignes
with open("data.txt", "w") as file:
    file.write("Line 1")
    file.write("Line 2")  # Will be "Line 1Line 2"

# ✅ Correct : Ajouter des nouvelles lignes
with open("data.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

# ❌ Incorrect : Ne pas gérer fichier non trouvé
with open("missing.txt", "r") as file:  # Error!
    content = file.read()

# ✅ Correct : Gérer l'exception ou vérifier l'existence
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

## Exemples Rapides

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

## Encodage de Fichiers

```python
# Specify encoding (important for non-ASCII text)
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Writing with encoding
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 世界!")  # Chinese characters
```
