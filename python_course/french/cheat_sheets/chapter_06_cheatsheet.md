# Chapitre 6 : Dictionnaires - Référence Rapide

## Créer des Dictionnaires

```python
# Empty dictionary
my_dict = {}
my_dict = dict()

# Dictionary with items
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Using dict() constructor
person = dict(name="Bob", age=25, city="NYC")
```

## Accéder aux Valeurs

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Access by key
student["name"]     # "Alice"
student["age"]      # 20

# Using get() method (safer)
student.get("name")        # "Alice"
student.get("email")       # None (no error)
student.get("email", "N/A")  # "N/A" (default value)
```

## Ajouter et Modifier

```python
student = {"name": "Alice", "age": 20}

# Add new key-value pair
student["grade"] = "A"
# {"name": "Alice", "age": 20, "grade": "A"}

# Modify existing value
student["age"] = 21
# {"name": "Alice", "age": 21, "grade": "A"}

# Update multiple items
student.update({"grade": "A+", "gpa": 4.0})
```

## Supprimer des Éléments

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Remove by key (returns value)
age = student.pop("age")  # 20
# student = {"name": "Alice", "grade": "A"}

# Remove last inserted item (Python 3.7+)
item = student.popitem()  # ("grade", "A")

# Delete by key
del student["name"]
# student = {}

# Clear all items
student.clear()  # {}
```

## Méthodes de Dictionnaires

| Méthode | Description | Exemple |
|--------|-------------|---------|
| `.get(key, default)` | Obtenir valeur en toute sécurité | `d.get("name", "Unknown")` |
| `.keys()` | Obtenir toutes les clés | `d.keys()` |
| `.values()` | Obtenir toutes les valeurs | `d.values()` |
| `.items()` | Obtenir paires clé-valeur | `d.items()` |
| `.update(other)` | Fusionner dictionnaires | `d.update(d2)` |
| `.pop(key)` | Supprimer et retourner valeur | `d.pop("age")` |
| `.popitem()` | Supprimer et retourner dernier élément | `d.popitem()` |
| `.clear()` | Supprimer tous les éléments | `d.clear()` |
| `.copy()` | Copie superficielle | `new = d.copy()` |

## Vérifier les Clés

```python
student = {"name": "Alice", "age": 20}

# Check if key exists
"name" in student     # True
"grade" in student    # False
"age" not in student  # False

# Using get to check
if student.get("email"):
    print(student["email"])
else:
    print("No email")
```

## Itérer sur les Dictionnaires

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Iterate over keys
for key in student:
    print(key)
# name
# age
# grade

# Iterate over keys (explicit)
for key in student.keys():
    print(key, student[key])

# Iterate over values
for value in student.values():
    print(value)
# Alice
# 20
# A

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 20
# grade: A
```

## Compréhensions de Dictionnaires

```python
# Basic syntax: {key_expr: value_expr for item in iterable}

# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {"a": 1, "b": 2, "c": 3}

# Squares dictionary
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dictionary
student = {"name": "alice", "city": "nyc"}
upper = {k: v.upper() for k, v in student.items()}
# {"name": "ALICE", "city": "NYC"}
```

## Dictionnaires Imbriqués

```python
# Dictionary of dictionaries
students = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
    "student3": {"name": "Charlie", "grade": "A"}
}

# Access nested values
students["student1"]["name"]  # "Alice"
students["student2"]["grade"]  # "B"

# Iterate over nested dictionary
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

## Modèles Courants

### Compter les occurrences

```python
# Count letter frequencies
text = "hello world"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Or using get:
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Result: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### Grouper des éléments

```python
# Group students by grade
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

# Result: {"A": ["Alice", "Charlie"], "B": ["Bob"]}
```

### Construire à partir de la saisie utilisateur

```python
phonebook = {}
while True:
    name = input("Name (or 'quit'): ")
    if name == "quit":
        break
    phone = input("Phone: ")
    phonebook[name] = phone
```

### Table de correspondance

```python
# Grade to GPA mapping
grade_to_gpa = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

grade = "B"
gpa = grade_to_gpa[grade]  # 3.0
```

## Fusionner des Dictionnaires

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update (modifies dict1)
dict1.update(dict2)
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}

# Using ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}

# Using | operator (Python 3.9+)
merged = dict1 | dict2

# If keys overlap, later value wins
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
# {"a": 1, "b": 3, "c": 4}
```

## Dictionnaire vs Liste

**Utiliser un Dictionnaire quand :**
- Vous avez besoin d'associations clé-valeur
- La recherche rapide par clé est importante
- Les clés sont significatives (noms, IDs)
- L'ordre n'a pas beaucoup d'importance

**Utiliser une Liste quand :**
- L'ordre est important
- Vous avez besoin d'indexation par position
- Tous les éléments sont de type similaire
- Vous devez trier fréquemment

```python
# List: ordered, indexed by position
fruits = ["apple", "banana", "orange"]
fruits[0]  # "apple"

# Dictionary: key-value pairs
fruit_prices = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.60
}
fruit_prices["apple"]  # 0.50
```

## Erreurs Courantes

```python
# ❌ Incorrect : Accéder à une clé non existante
person = {"name": "Alice"}
print(person["age"])  # KeyError!

# ✅ Correct : Utiliser get() ou vérifier d'abord
print(person.get("age"))  # None
if "age" in person:
    print(person["age"])

# ❌ Incorrect : Utiliser une clé mutable (liste)
d = {[1, 2]: "value"}  # Error! List is mutable

# ✅ Correct : Utiliser une clé immuable (tuple)
d = {(1, 2): "value"}  # OK

# ❌ Incorrect : Essayer d'utiliser les méthodes de liste
person = {"name": "Alice", "age": 20}
person.append("email")  # Error! No append method

# ✅ Correct : Ajouter une paire clé-valeur
person["email"] = "alice@example.com"
```

## Trier les Dictionnaires

```python
person = {"name": "Alice", "age": 20, "city": "NYC"}

# Sort by keys
sorted_keys = dict(sorted(person.items()))

# Sort by values
sorted_values = dict(sorted(person.items(), key=lambda x: x[1]))

# Get sorted keys/values as lists
sorted_keys = sorted(person.keys())
sorted_values = sorted(person.values())
```

## Exemples Rapides

```python
# Simple phonebook
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

name = input("Name to lookup: ")
if name in phonebook:
    print(f"{name}: {phonebook[name]}")
else:
    print("Not found")

# Word frequency counter
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word}: {count}")

# Grade book
gradebook = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 75, "english": 80}
}

# Add new student
gradebook["Charlie"] = {"math": 95, "english": 90}

# Calculate average for a student
alice_avg = sum(gradebook["Alice"].values()) / len(gradebook["Alice"])
print(f"Alice's average: {alice_avg}")

# Menu-driven program
menu = {
    "1": "New contact",
    "2": "Search contact",
    "3": "Delete contact",
    "4": "Exit"
}

for key, value in menu.items():
    print(f"{key}. {value}")

choice = input("Choose: ")
if choice in menu:
    print(f"You selected: {menu[choice]}")
```

## Valeurs Par Défaut avec setdefault

```python
person = {"name": "Alice"}

# setdefault: get value, or set and return default
age = person.setdefault("age", 20)  # 20
# person = {"name": "Alice", "age": 20}

# If key exists, return existing value
name = person.setdefault("name", "Bob")  # "Alice"
# person unchanged
```

## Dictionnaire à partir de Listes

```python
# Using zip
keys = ["name", "age", "city"]
values = ["Alice", 20, "NYC"]
person = dict(zip(keys, values))
# {"name": "Alice", "age": 20, "city": "NYC"}

# Using fromkeys (same value for all keys)
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
# {"a": 0, "b": 0, "c": 0}
```
