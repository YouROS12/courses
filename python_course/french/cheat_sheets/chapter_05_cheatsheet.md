# Chapitre 5 : Listes - Référence Rapide

## Créer des Listes

```python
# Empty list
my_list = []
my_list = list()

# List with items
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

# List from range
nums = list(range(5))  # [0, 1, 2, 3, 4]
```

## Accéder aux Éléments

### Indexation

```python
fruits = ["apple", "banana", "orange", "grape"]

fruits[0]   # "apple" (first item)
fruits[1]   # "banana"
fruits[-1]  # "grape" (last item)
fruits[-2]  # "orange" (second from end)
```

### Découpage

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:5]    # [2, 3, 4] (indices 2, 3, 4)
numbers[:4]     # [0, 1, 2, 3] (start to 4)
numbers[6:]     # [6, 7, 8, 9] (6 to end)
numbers[:]      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)
numbers[::2]    # [0, 2, 4, 6, 8] (every 2nd)
numbers[1::2]   # [1, 3, 5, 7, 9] (odd indices)
numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

## Modifier les Listes

### Changer les Éléments

```python
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"  # ["apple", "mango", "orange"]
```

### Ajouter des Éléments

```python
fruits = ["apple", "banana"]

# Append to end
fruits.append("orange")  # ["apple", "banana", "orange"]

# Insert at position
fruits.insert(1, "mango")  # ["apple", "mango", "banana", "orange"]

# Extend with another list
fruits.extend(["grape", "kiwi"])
# ["apple", "mango", "banana", "orange", "grape", "kiwi"]

# Concatenate (creates new list)
more_fruits = fruits + ["pear", "peach"]
```

### Supprimer des Éléments

```python
fruits = ["apple", "banana", "orange", "grape"]

# Remove by value
fruits.remove("banana")  # ["apple", "orange", "grape"]

# Remove by index (returns removed item)
item = fruits.pop(1)     # "orange", list is now ["apple", "grape"]
last = fruits.pop()      # "grape", list is now ["apple"]

# Delete by index
del fruits[0]            # list is now []

# Clear entire list
fruits.clear()           # []
```

## Méthodes de Listes

| Méthode | Description | Exemple |
|--------|-------------|---------|
| `.append(x)` | Ajouter x à la fin | `nums.append(5)` |
| `.insert(i, x)` | Insérer x à l'index i | `nums.insert(0, 1)` |
| `.remove(x)` | Supprimer le premier x | `nums.remove(3)` |
| `.pop(i)` | Supprimer et retourner l'élément à i | `nums.pop(2)` |
| `.clear()` | Supprimer tous les éléments | `nums.clear()` |
| `.index(x)` | Trouver l'index de x | `nums.index(5)` |
| `.count(x)` | Compter les occurrences de x | `nums.count(3)` |
| `.sort()` | Trier sur place | `nums.sort()` |
| `.reverse()` | Inverser sur place | `nums.reverse()` |
| `.copy()` | Copie superficielle | `new = nums.copy()` |

## Trier les Listes

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# Sort in place (modifies original)
numbers.sort()           # [1, 1, 2, 3, 4, 5, 9]
numbers.sort(reverse=True)  # [9, 5, 4, 3, 2, 1, 1]

# Create sorted copy (original unchanged)
sorted_nums = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)

# Sort strings alphabetically
fruits = ["banana", "apple", "orange"]
fruits.sort()  # ["apple", "banana", "orange"]
```

## Opérations sur les Listes

```python
# Length
len([1, 2, 3])  # 3

# Check membership
3 in [1, 2, 3]      # True
5 not in [1, 2, 3]  # True

# Concatenation
[1, 2] + [3, 4]  # [1, 2, 3, 4]

# Repetition
[1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Min/Max/Sum
min([3, 1, 4])  # 1
max([3, 1, 4])  # 4
sum([1, 2, 3])  # 6
```

## Itérer sur les Listes

```python
fruits = ["apple", "banana", "orange"]

# Basic iteration
for fruit in fruits:
    print(fruit)

# With index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (better)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With enumerate (custom start)
for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruit}")
```

## Compréhensions de Listes

**Façon concise de créer des listes**

```python
# Basic syntax: [expression for item in iterable]

# Create list of squares
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Create list of uppercase strings
fruits = ["apple", "banana", "orange"]
upper_fruits = [fruit.upper() for fruit in fruits]
# ["APPLE", "BANANA", "ORANGE"]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Traditional equivalent:
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
```

## Listes Imbriquées

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
matrix[0]     # [1, 2, 3] (first row)
matrix[0][0]  # 1 (first row, first column)
matrix[1][2]  # 6 (second row, third column)

# Iterate over 2D list
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # New line after each row
```

## Modèles Courants

### Construire une liste à partir de la saisie

```python
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
```

### Trouver le maximum

```python
numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
# Or simply: max_num = max(numbers)
```

### Filtrer une liste

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
# [2, 4, 6, 8, 10]
```

### Sommer les éléments

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # 15

# Or manually:
total = 0
for num in numbers:
    total += num
```

## Copier les Listes

```python
original = [1, 2, 3]

# ❌ Incorrect : Ceci est juste une référence !
copy1 = original
copy1[0] = 99
print(original)  # [99, 2, 3] - original changed!

# ✅ Façons correctes de copier :
copy2 = original.copy()
copy3 = original[:]
copy4 = list(original)

copy2[0] = 99
print(original)  # [1, 2, 3] - original unchanged
```

## Erreurs Courantes

```python
# ❌ Incorrect : Index hors limites
fruits = ["apple", "banana"]
print(fruits[5])  # Error!

# ✅ Correct : Vérifier la longueur
if len(fruits) > 5:
    print(fruits[5])

# ❌ Incorrect : Modifier la liste pendant l'itération
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can cause issues!

# ✅ Correct : Créer une nouvelle liste
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]

# ❌ Incorrect : Confondre append et extend
nums = [1, 2, 3]
nums.append([4, 5])  # [1, 2, 3, [4, 5]]

# ✅ Correct : Utiliser extend pour plusieurs éléments
nums = [1, 2, 3]
nums.extend([4, 5])  # [1, 2, 3, 4, 5]
```

## Exemples Rapides

```python
# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
# unique = [1, 2, 3, 4]

# Or use set: unique = list(set(numbers))

# Reverse a list
original = [1, 2, 3, 4, 5]
reversed_list = original[::-1]  # [5, 4, 3, 2, 1]

# Or: original.reverse()  # modifies in place

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4, 2]
count_of_2 = numbers.count(2)  # 4

# Find all indices of a value
numbers = [1, 2, 3, 2, 4, 2]
indices = [i for i, x in enumerate(numbers) if x == 2]
# indices = [1, 3, 5]

# Create a list of even numbers from 0 to 20
evens = [x for x in range(0, 21, 2)]
# Or: evens = list(range(0, 21, 2))
```

## Liste vs Chaîne

```python
# String to list
text = "hello"
chars = list(text)  # ['h', 'e', 'l', 'l', 'o']

# Split string into words
sentence = "Python is awesome"
words = sentence.split()  # ["Python", "is", "awesome"]

# List to string
chars = ['h', 'e', 'l', 'l', 'o']
text = "".join(chars)  # "hello"

words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # "Python is awesome"
```
