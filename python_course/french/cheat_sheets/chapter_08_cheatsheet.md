# Chapitre 8 : Tuples et Ensembles - Référence Rapide

## Tuples

### Créer des Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# Tuple with items
coordinates = (3, 4)
person = ("Alice", 25, "NYC")

# Single element tuple (note the comma!)
single = (42,)   # Tuple
not_tuple = (42)  # Just an integer

# Without parentheses
point = 1, 2, 3  # Also a tuple

# From list
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)
```

### Accéder aux Éléments de Tuple

```python
point = (10, 20, 30)

# Indexing
point[0]   # 10
point[-1]  # 30

# Slicing
point[0:2]  # (10, 20)
point[:2]   # (10, 20)
point[1:]   # (20, 30)

# Length
len(point)  # 3
```

### Opérations sur les Tuples

```python
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)

# Repetition
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# Membership
3 in (1, 2, 3)      # True
5 not in (1, 2, 3)  # True

# Min, Max, Sum
numbers = (3, 1, 4, 1, 5)
min(numbers)  # 1
max(numbers)  # 5
sum(numbers)  # 14
```

### Méthodes de Tuples

**Les tuples n'ont que 2 méthodes (ils sont immuables)**

```python
numbers = (1, 2, 2, 3, 2, 4)

# Count occurrences
numbers.count(2)  # 3

# Find index
numbers.index(3)  # 3 (first occurrence)
```

### Déballage de Tuples

```python
# Unpack tuple into variables
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# Multiple values
person = ("Alice", 25, "NYC")
name, age, city = person
print(name)  # Alice

# Swap values using tuple unpacking
a = 5
b = 10
a, b = b, a  # Swap!
print(a, b)  # 10 5

# Ignore values with _
data = (1, 2, 3, 4, 5)
first, second, *rest = data
print(first)  # 1
print(second) # 2
print(rest)   # [3, 4, 5]

# Unpack in loop
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x={x}, y={y}")
```

### Immuabilité

```python
point = (10, 20)

# ❌ Cannot modify
point[0] = 15  # Error! Tuples are immutable

# ✅ Can create new tuple
point = (15, 20)  # OK - creating new tuple

# Nested mutable objects can be modified
data = ([1, 2], [3, 4])
data[0].append(3)  # OK - modifying the list inside
print(data)  # ([1, 2, 3], [3, 4])
```

### Quand Utiliser les Tuples

```python
# ✅ Coordinates
point = (10, 20)

# ✅ RGB colors
color = (255, 0, 128)

# ✅ Database records
student = (1, "Alice", 85, "A")

# ✅ Return multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

# ✅ Dictionary keys (tuples are hashable, lists aren't)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# ✅ Immutable data (can't be changed accidentally)
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

---

## Ensembles

### Créer des Ensembles

```python
# Empty set (must use set())
empty = set()  # Not {} - that's a dict!

# Set with items
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

# From list (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3]
numbers_set = set(numbers_list)  # {1, 2, 3}

# From string
chars = set("hello")  # {'h', 'e', 'l', 'o'}
```

### Propriétés des Ensembles

```python
# Unordered (no indexing)
my_set = {1, 2, 3}
# my_set[0]  # Error! Sets don't support indexing

# Unique elements only
my_set = {1, 2, 2, 3, 3}
print(my_set)  # {1, 2, 3}

# Mutable (can add/remove)
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Length
len(my_set)  # 4

# Membership (very fast!)
2 in my_set     # True
5 not in my_set # True
```

### Ajouter et Supprimer

```python
fruits = {"apple", "banana"}

# Add single element
fruits.add("orange")
# {"apple", "banana", "orange"}

# Add multiple elements
fruits.update(["grape", "kiwi"])
# {"apple", "banana", "orange", "grape", "kiwi"}

# Remove (raises error if not found)
fruits.remove("banana")
# {"apple", "orange", "grape", "kiwi"}

# Discard (no error if not found)
fruits.discard("banana")  # OK even though banana is gone
fruits.discard("mango")   # OK - no error

# Pop (remove and return arbitrary element)
item = fruits.pop()
print(item)

# Clear all elements
fruits.clear()  # set()
```

### Opérations sur les Ensembles

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements from both)
set1 | set2           # {1, 2, 3, 4, 5, 6}
set1.union(set2)      # Same

# Intersection (common elements)
set1 & set2               # {3, 4}
set1.intersection(set2)   # Same

# Difference (in set1 but not set2)
set1 - set2            # {1, 2}
set1.difference(set2)  # Same

# Symmetric difference (in either but not both)
set1 ^ set2                      # {1, 2, 5, 6}
set1.symmetric_difference(set2)  # Same
```

### Comparaisons d'Ensembles

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# Subset (all elements in set1 are in set2)
set1.issubset(set2)  # True
set1 <= set2         # True

# Superset (set2 contains all elements of set1)
set2.issuperset(set1)  # True
set2 >= set1           # True

# Disjoint (no common elements)
set1.isdisjoint({4, 5, 6})  # True

# Equality
set1 == set3  # True
set1 == set2  # False
```

### Itérer sur les Ensembles

```python
fruits = {"apple", "banana", "orange"}

# Note: Order is not guaranteed
for fruit in fruits:
    print(fruit)

# Convert to sorted list for ordered iteration
for fruit in sorted(fruits):
    print(fruit)  # Alphabetical order
```

### Compréhensions d'Ensembles

```python
# Basic syntax: {expression for item in iterable}

# Squares
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# From string (unique characters)
unique_chars = {char.lower() for char in "Hello World"}
# {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
```

### Ensembles Gelés

**Ensembles immuables**

```python
# Create frozen set
frozen = frozenset([1, 2, 3])

# Can't modify
# frozen.add(4)  # Error!

# Can use as dictionary key
data = {
    frozenset([1, 2]): "A",
    frozenset([3, 4]): "B"
}

# Same operations as sets (except mutations)
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([2, 3, 4])
frozen1 | frozen2  # frozenset({1, 2, 3, 4})
```

### Modèles Courants d'Ensembles

### Supprimer les doublons d'une liste

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
# [1, 2, 3, 4, 5] (order may vary)

# Preserve order (Python 3.7+)
unique = list(dict.fromkeys(numbers))
```

### Trouver les éléments communs

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
# [3, 4]
```

### Trouver les uniques à chaque liste

```python
only_in_list1 = list(set(list1) - set(list2))  # [1, 2]
only_in_list2 = list(set(list2) - set(list1))  # [5, 6]
```

### Vérifier les doublons

```python
numbers = [1, 2, 3, 4, 5]
has_duplicates = len(numbers) != len(set(numbers))
# False
```

### Test d'appartenance (rapide !)

```python
# Set lookup is O(1) - very fast!
valid_users = {"alice", "bob", "charlie"}

username = input("Username: ")
if username in valid_users:
    print("Welcome!")
```

## Tuple vs Ensemble vs Liste

| Fonctionnalité | Liste | Tuple | Ensemble |
|---------|------|-------|-----|
| **Ordonné** | ✅ Oui | ✅ Oui | ❌ Non |
| **Mutable** | ✅ Oui | ❌ Non | ✅ Oui |
| **Doublons** | ✅ Oui | ✅ Oui | ❌ Non |
| **Indexation** | ✅ Oui | ✅ Oui | ❌ Non |
| **Syntaxe** | `[1, 2]` | `(1, 2)` | `{1, 2}` |
| **Cas d'usage** | Collection générale | Données immuables, clés dict | Éléments uniques, recherche rapide |

```python
# List: ordered, mutable, allows duplicates
my_list = [1, 2, 2, 3]
my_list[0] = 10  # OK
my_list.append(4)  # OK

# Tuple: ordered, immutable, allows duplicates
my_tuple = (1, 2, 2, 3)
# my_tuple[0] = 10  # Error!
# my_tuple.append(4)  # Error!

# Set: unordered, mutable, no duplicates
my_set = {1, 2, 2, 3}  # Becomes {1, 2, 3}
# my_set[0]  # Error! No indexing
my_set.add(4)  # OK
```

## Exemples Rapides

```python
# Coordinates (tuple)
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

dist = distance((0, 0), (3, 4))
print(f"Distance: {dist}")  # 5.0

# Remove duplicates (set)
def unique_words(text):
    words = text.lower().split()
    return set(words)

text = "the quick brown fox jumps over the lazy dog"
unique = unique_words(text)
print(f"Unique words: {len(unique)}")

# Find common friends (set intersection)
alice_friends = {"Bob", "Charlie", "David"}
bob_friends = {"Alice", "Charlie", "Eve"}
mutual = alice_friends & bob_friends
print(f"Mutual friends: {mutual}")  # {"Charlie"}

# Return multiple values (tuple)
def analyze_list(numbers):
    return (
        min(numbers),
        max(numbers),
        sum(numbers) / len(numbers)
    )

minimum, maximum, average = analyze_list([1, 2, 3, 4, 5])

# Tag system (set)
post1_tags = {"python", "coding", "tutorial"}
post2_tags = {"python", "data", "science"}

# All tags
all_tags = post1_tags | post2_tags
# {"python", "coding", "tutorial", "data", "science"}

# Common tags
common_tags = post1_tags & post2_tags
# {"python"}
```

## Erreurs Courantes

```python
# ❌ Incorrect : Tuple à un seul élément sans virgule
single = (42)   # This is just an int!
print(type(single))  # <class 'int'>

# ✅ Correct
single = (42,)  # Tuple
print(type(single))  # <class 'tuple'>

# ❌ Incorrect : Syntaxe d'ensemble vide
empty = {}  # This is a dict!
print(type(empty))  # <class 'dict'>

# ✅ Correct
empty = set()
print(type(empty))  # <class 'set'>

# ❌ Incorrect : Essayer de modifier un tuple
point = (10, 20)
point[0] = 15  # Error!

# ✅ Correct : Créer un nouveau tuple
point = (15, 20)

# ❌ Incorrect : Essayer d'indexer un ensemble
my_set = {1, 2, 3}
print(my_set[0])  # Error!

# ✅ Correct : Convertir en liste ou itérer
my_list = list(my_set)
print(my_list[0])  # OK
```
