# Chapitre 3 : Prendre des Décisions - Référence Rapide

## Valeurs Booléennes

```python
is_student = True
is_admin = False

# Boolean from expressions
age = 25
can_vote = age >= 18  # True
```

## Opérateurs de Comparaison

| Opérateur | Signification | Exemple | Résultat |
|----------|---------|---------|--------|
| `==` | Égal à | `5 == 5` | `True` |
| `!=` | Différent de | `5 != 3` | `True` |
| `>` | Supérieur à | `5 > 3` | `True` |
| `<` | Inférieur à | `5 < 3` | `False` |
| `>=` | Supérieur ou égal | `5 >= 5` | `True` |
| `<=` | Inférieur ou égal | `3 <= 5` | `True` |

## Instructions If

```python
# Simple if
if age >= 18:
    print("You can vote")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## Opérateurs Logiques

### AND - Les deux conditions doivent être True

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR - Au moins une condition doit être True

```python
if age < 13 or age > 65:
    print("Discounted ticket")
```

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT - Inverse la valeur booléenne

```python
is_raining = False
if not is_raining:
    print("Go outside")
```

| A | not A |
|---|-------|
| True | False |
| False | True |

## Combiner des Conditions

```python
# Multiple conditions with parentheses
if (age >= 18 and has_license) or has_permit:
    print("Can drive")

# Complex logic
if age >= 18 and (is_student or is_senior):
    print("Eligible for discount")
```

## Valeurs Truthy et Falsy

**Valeurs Falsy** (évaluées à False) :
- `False`
- `0`, `0.0`
- `""` (chaîne vide)
- `None`
- `[]` (liste vide)
- `{}` (dict vide)

**Valeurs Truthy** (tout le reste) :
- `True`
- Nombres non nuls : `1`, `-5`, `3.14`
- Chaînes non vides : `"hello"`
- Collections non vides : `[1, 2]`, `{"a": 1}`

```python
name = input("Enter name: ")
if name:  # True if name is not empty
    print(f"Hello, {name}")
else:
    print("No name entered")
```

## Conditions Imbriquées

```python
if age >= 18:
    if has_ticket:
        print("Enjoy the movie!")
    else:
        print("Please buy a ticket")
else:
    if is_with_parent:
        print("Needs parental guidance")
    else:
        print("Too young")
```

## Expressions Conditionnelles (Ternaire)

```python
# Shorthand for simple if-else
status = "Adult" if age >= 18 else "Minor"

# Traditional equivalent:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

## Opérateurs d'Appartenance

```python
# Check if value is in a sequence
if "a" in "cat":  # True
    print("Contains 'a'")

if "x" not in "cat":  # True
    print("Doesn't contain 'x'")
```

## Opérateurs d'Identité

```python
# Check if two variables reference same object
x = None
if x is None:
    print("x is None")

if x is not None:
    print("x has a value")
```

## Modèles Courants

### Valider la saisie

```python
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("Minor")
else:
    print("Adult")
```

### Vérifier les plages

```python
score = int(input("Enter score: "))
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Score must be 0-100")
```

### Conditions multiples

```python
if username and password and len(password) >= 8:
    print("Valid credentials")
else:
    print("Invalid credentials")
```

## Erreurs Courantes

```python
# ❌ Incorrect : Utiliser = au lieu de ==
if age = 18:  # Error! This is assignment
    print("18 years old")

# ✅ Correct
if age == 18:
    print("18 years old")

# ❌ Incorrect : Vérification de plage incorrecte
if 0 < age < 18:  # Syntax is correct, but...
# ✅ Correct et plus lisible
if age > 0 and age < 18:
if 0 < age < 18:  # This actually works in Python!

# ❌ Incorrect : Deux-points manquants
if age >= 18
    print("Adult")

# ✅ Correct
if age >= 18:
    print("Adult")

# ❌ Incorrect : Indentation incohérente
if age >= 18:
print("Adult")  # Error!

# ✅ Correct (4 espaces d'indentation)
if age >= 18:
    print("Adult")
```

## Exemples Rapides

```python
# Grade calculator
score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Login validator
username = input("Username: ")
password = input("Password: ")

if not username:
    print("Username required")
elif not password:
    print("Password required")
elif len(password) < 8:
    print("Password too short")
else:
    print("Login successful")

# Discount calculator
age = int(input("Enter age: "))
is_student = input("Student? (yes/no): ").lower() == "yes"

if age < 12 or age > 65:
    discount = 0.50  # 50% off
elif is_student:
    discount = 0.25  # 25% off
else:
    discount = 0.0   # No discount

print(f"Discount: {discount * 100}%")
```

## Chaînage de Comparaisons

```python
# Python allows chaining comparisons
if 0 <= age < 18:
    print("Minor")

if 18 <= age <= 65:
    print("Adult")

# Equivalent to:
if age >= 0 and age < 18:
    print("Minor")
```
