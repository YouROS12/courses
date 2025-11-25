# Chapitre 1 : Introduction à Python - Référence Rapide

## Variables

```python
# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## Types de Données

| Type | Exemple | Description |
|------|---------|-------------|
| `int` | `42` | Nombres entiers |
| `float` | `3.14` | Nombres décimaux |
| `str` | `"Hello"` | Texte/chaînes |
| `bool` | `True` ou `False` | Valeurs booléennes |

## Vérification des Types

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hello")   # <class 'str'>
type(True)      # <class 'bool'>
```

## Opérateurs Arithmétiques

| Opérateur | Opération | Exemple | Résultat |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Division entière | `5 // 2` | `2` |
| `%` | Modulo (reste) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

## Priorité des Opérateurs

**PEMDAS** (du plus élevé au plus bas) :
1. `()` - Parenthèses
2. `**` - Exponentiation
3. `*`, `/`, `//`, `%` - Multiplication, Division
4. `+`, `-` - Addition, Soustraction

```python
result = 2 + 3 * 4      # 14 (pas 20)
result = (2 + 3) * 4    # 20
```

## Afficher la Sortie

```python
print("Hello, World!")
print("Name:", name)
print("Age:", age, "Height:", height)
```

## Commentaires

```python
# This is a single-line comment

# This is a
# multi-line comment
# using multiple single-line comments
```

## Règles de Nommage des Variables

✅ **Valide** :
- `name`, `age`, `first_name`
- `total_score`, `user_2`
- Commence par une lettre ou un underscore
- Utilise des lettres, des chiffres, des underscores

❌ **Invalide** :
- `2nd_place` (commence par un chiffre)
- `first-name` (contient un tiret)
- `class` (mot-clé réservé)

## Bonnes Pratiques

- Utilisez des noms de variables descriptifs : `user_age` pas `x`
- Utilisez des minuscules avec des underscores : `total_count`
- Ajoutez des commentaires pour expliquer le code complexe
- Une instruction par ligne
- Utilisez des espaces autour des opérateurs : `x = 5` pas `x=5`

## Erreurs Courantes

```python
# ❌ Incorrect : Utiliser une variable non définie
print(score)  # Error if score not defined

# ✅ Correct : Définir d'abord
score = 100
print(score)

# ❌ Incorrect : Mélanger les types sans conversion
age = "25"
next_year = age + 1  # Error

# ✅ Correct : Convertir d'abord
age = "25"
next_year = int(age) + 1
```

## Exemples Rapides

```python
# Calculate area of rectangle
width = 10
height = 5
area = width * height
print("Area:", area)  # Area: 50

# Calculate average
num1 = 85
num2 = 92
num3 = 78
average = (num1 + num2 + num3) / 3
print("Average:", average)  # Average: 85.0
```
