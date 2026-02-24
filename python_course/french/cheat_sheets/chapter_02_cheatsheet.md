# Chapitre 2 : Travailler avec les Données - Référence Rapide

## Saisie Utilisateur

```python
# Get input (always returns a string)
name = input("Enter your name: ")
age = input("Enter your age: ")
```

## Conversion de Type (Casting)

| Fonction | Convertit en | Exemple |
|----------|-------------|---------|
| `int()` | Entier | `int("25")` → `25` |
| `float()` | Flottant | `float("3.14")` → `3.14` |
| `str()` | Chaîne | `str(25)` → `"25"` |
| `bool()` | Booléen | `bool(1)` → `True` |

```python
# Convert input to number
age = int(input("Enter age: "))
height = float(input("Enter height: "))
```

## Opérations sur les Chaînes

### Concaténation

```python
first = "John"
last = "Doe"
full_name = first + " " + last  # "John Doe"
```

### Répétition

```python
laugh = "ha" * 3  # "hahaha"
line = "-" * 20   # "--------------------"
```

### Indexation

```python
text = "Python"
text[0]   # "P" (first character)
text[-1]  # "n" (last character)
text[-2]  # "o" (second from end)
```

### Découpage

```python
text = "Python"
text[0:3]    # "Pyt" (start to 3, not including 3)
text[2:5]    # "tho"
text[:3]     # "Pyt" (start to 3)
text[3:]     # "hon" (3 to end)
text[:]      # "Python" (entire string)
text[::2]    # "Pto" (every 2nd character)
```

## Méthodes de Chaînes

| Méthode | Description | Exemple |
|--------|-------------|---------|
| `.upper()` | Majuscules | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Minuscules | `"HELLO".lower()` → `"hello"` |
| `.title()` | Première Lettre Majuscule | `"hello world".title()` → `"Hello World"` |
| `.strip()` | Supprimer espaces | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Remplacer texte | `"cat".replace("c", "b")` → `"bat"` |
| `.split()` | Diviser en liste | `"a b c".split()` → `["a", "b", "c"]` |
| `.find(text)` | Trouver position | `"hello".find("e")` → `1` |
| `.count(text)` | Compter occurrences | `"aaa".count("a")` → `3` |

```python
text = "  Hello World  "
text.strip().lower()  # "hello world"
```

## Formatage de Chaînes

### F-Strings (Recommandé)

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# "My name is Alice and I am 25 years old."

# Expressions in f-strings
print(f"Next year I'll be {age + 1}")
# "Next year I'll be 26"

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # "Price: $19.99"
```

### Méthode .format()

```python
print("Name: {}, Age: {}".format(name, age))
print("Age: {1}, Name: {0}".format(name, age))
```

### Formatage % (Ancien Style)

```python
print("Name: %s, Age: %d" % (name, age))
```

## Séquences d'Échappement

| Séquence | Signification | Exemple |
|----------|---------|---------|
| `\n` | Nouvelle ligne | `"Line 1\nLine 2"` |
| `\t` | Tabulation | `"Name:\tJohn"` |
| `\\` | Barre oblique inverse | `"C:\\Users"` |
| `\'` | Apostrophe | `'It\'s'` |
| `\"` | Guillemet double | `"She said \"Hi\""` |

```python
print("Line 1\nLine 2\nLine 3")
# Line 1
# Line 2
# Line 3
```

## Propriétés des Chaînes

```python
text = "Python"

# Length
len(text)  # 6

# Check content
text.isalpha()    # True (all letters)
text.isdigit()    # False (not all digits)
text.isalnum()    # True (letters and/or numbers)

# Check case
text.isupper()    # False
text.islower()    # False
```

## Modèles Courants

### Obtenir et convertir la saisie

```python
# Get number from user
age = int(input("Enter age: "))

# Get decimal from user
price = float(input("Enter price: "))

# Get multiple values
name = input("Name: ")
age = int(input("Age: "))
```

### Construire une sortie formatée

```python
name = input("Enter name: ")
score = int(input("Enter score: "))
print(f"{name} scored {score} points!")
```

### Traiter les chaînes

```python
text = input("Enter text: ")
# Make uppercase and strip whitespace
processed = text.strip().upper()
print(f"Processed: {processed}")
```

## Erreurs Courantes

```python
# ❌ Incorrect : Oublier de convertir la saisie
age = input("Enter age: ")
next_year = age + 1  # Error! age is string

# ✅ Correct
age = int(input("Enter age: "))
next_year = age + 1

# ❌ Incorrect : Mélanger + avec chaîne et nombre
print("Age: " + age)  # Error if age is int

# ✅ Correct : Convertir en chaîne ou utiliser f-string
print("Age: " + str(age))
print(f"Age: {age}")
```

## Exemples Rapides

```python
# Interactive calculator
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
result = num1 + num2
print(f"{num1} + {num2} = {result}")

# Name formatter
first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
print(f"Full name: {first} {last}")

# String analyzer
text = input("Enter text: ")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Word count: {len(text.split())}")
```
