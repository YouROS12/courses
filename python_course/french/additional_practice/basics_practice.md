# Problèmes de Pratique Python de Base

Problèmes de pratique pour les Chapitres 1-2 : Variables, types de données, opérateurs et chaînes.

---

## Variables et Types de Données

### Problème 1 : Échange de Variables
Écrivez du code pour échanger les valeurs de deux variables sans utiliser une troisième variable.

**Indice :** Utilisez le déballage de tuples

---

### Problème 2 : Vérificateur de Type
Créez un programme qui demande à l'utilisateur une entrée et affiche le type de la valeur entrée (tel qu'interprété par Python).

---

### Problème 3 : Calculateur d'IMC
Calculez l'Indice de Masse Corporelle (IMC) en utilisant la formule : IMC = poids(kg) / (taille(m))²

Demandez à l'utilisateur son poids et sa taille, puis affichez l'IMC avec 2 décimales.

---

## Opérations Arithmétiques

### Problème 4 : Calculateur de Cercle
Étant donné le rayon d'un cercle, calculez :
- Aire (π × r²)
- Circonférence (2 × π × r)

Utilisez 3.14159 pour π.

---

### Problème 5 : Convertisseur de Temps
Convertissez un nombre donné de secondes en heures, minutes et secondes.

Exemple : 3665 secondes = 1 heure, 1 minute, 5 secondes

**Indice :** Utilisez la division entière (//) et le modulo (%)

---

### Problème 6 : Moyenne de Trois
Demandez à l'utilisateur trois nombres et calculez leur moyenne.

---

### Problème 7 : Vérificateur Pair ou Impair (Sans If)
Étant donné un nombre, déterminez s'il est pair ou impair en utilisant uniquement l'opérateur modulo (%).
Affichez le résultat de n % 2 (0 signifie pair, 1 signifie impair).

---

## Manipulation de Chaînes

### Problème 8 : Formateur de Nom
Demandez le prénom et le nom séparément. Affichez :
- Nom complet (Prénom Nom)
- Nom inversé (Nom, Prénom)
- Initiales (P.N.)
- Tout en majuscules
- Tout en minuscules

---

### Problème 9 : Statistiques de Chaîne
Pour une chaîne donnée, calculez et affichez :
- Longueur totale
- Nombre d'espaces
- Nombre de lettres majuscules
- Nombre de lettres minuscules
- Nombre de chiffres

**Indice :** Utilisez des méthodes de chaîne comme .isupper(), .islower(), .isdigit()

---

### Problème 10 : Analyseur d'Email
Étant donné une adresse e-mail comme "jean.dupont@exemple.com", extrayez :
- Nom d'utilisateur (jean.dupont)
- Domaine (exemple.com)

**Indice :** Utilisez .split('@')

---

### Problème 11 : Vérificateur de Palindrome (Simple)
Demandez à l'utilisateur un mot. Vérifiez s'il se lit de la même façon dans les deux sens.
Ne vous inquiétez pas de la casse ou des espaces pour l'instant (nous améliorerons cela plus tard avec les instructions if).

Comparez simplement : mot == mot[::-1]

---

### Problème 12 : Censure de Texte
Remplacez toutes les occurrences d'un "mot interdit" par des astérisques.
Demandez à l'utilisateur le texte et le mot à censurer.

**Indice :** Utilisez .replace()

---

## Défis Mixtes

### Problème 13 : Générateur de Reçu
Créez un calculateur de reçu simple :
- Demandez le nom et le prix de l'article (3 articles)
- Calculez le sous-total
- Calculez la taxe (8%)
- Calculez le total

Formatez la sortie joliment :
```
Article 1 : Pizza         12,99 $
Article 2 : Boisson        2,50 $
Article 3 : Dessert        5,99 $
              ---------------
Sous-total :              21,48 $
Taxe (8%) :                1,72 $
Total :                   23,20 $
```

---

### Problème 14 : Convertisseur de Température
Convertissez entre Celsius et Fahrenheit :
- Celsius vers Fahrenheit : F = C × 9/5 + 32
- Fahrenheit vers Celsius : C = (F - 32) × 5/9

Demandez à l'utilisateur la température et dans quelle direction convertir.

---

### Problème 15 : Générateur de Mad Libs
Créez une courte histoire avec des espaces vides. Demandez à l'utilisateur :
- Un nom
- Un verbe
- Un adjectif
- Un adverbe

Puis affichez une histoire en utilisant leurs mots.

Exemple : "Le [adjectif] [nom] [verbe] [adverbe] à travers la pièce."

---

## Solutions

<details>
<summary>Cliquez pour révéler les solutions</summary>

### Solution 1 : Échange de Variables
```python
a = 5
b = 10
print(f"Avant : a={a}, b={b}")

a, b = b, a

print(f"Après : a={a}, b={b}")
```

### Solution 2 : Vérificateur de Type
```python
user_input = input("Entrez quelque chose : ")
print(f"Type : {type(user_input)}")

# Note : input() retourne toujours une chaîne
# Pour une vérification de type réelle, essayez de convertir :
try:
    num = int(user_input)
    print("C'est un entier !")
except:
    print("C'est une chaîne !")
```

### Solution 3 : Calculateur d'IMC
```python
weight = float(input("Entrez le poids (kg) : "))
height = float(input("Entrez la taille (m) : "))

bmi = weight / (height ** 2)
print(f"Votre IMC est : {bmi:.2f}")
```

### Solution 4 : Calculateur de Cercle
```python
radius = float(input("Entrez le rayon : "))
pi = 3.14159

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Aire : {area:.2f}")
print(f"Circonférence : {circumference:.2f}")
```

### Solution 5 : Convertisseur de Temps
```python
total_seconds = int(input("Entrez les secondes : "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} secondes = {hours}h {minutes}m {seconds}s")
```

### Solution 6 : Moyenne de Trois
```python
num1 = float(input("Premier nombre : "))
num2 = float(input("Deuxième nombre : "))
num3 = float(input("Troisième nombre : "))

average = (num1 + num2 + num3) / 3
print(f"Moyenne : {average:.2f}")
```

### Solution 7 : Vérificateur Pair ou Impair
```python
number = int(input("Entrez un nombre : "))
result = number % 2
print(f"Résultat : {result} (0=pair, 1=impair)")
```

### Solution 8 : Formateur de Nom
```python
first = input("Prénom : ")
last = input("Nom : ")

print(f"Nom complet : {first} {last}")
print(f"Inversé : {last}, {first}")
print(f"Initiales : {first[0]}.{last[0]}.")
print(f"Majuscules : {first.upper()} {last.upper()}")
print(f"Minuscules : {first.lower()} {last.lower()}")
```

### Solution 9 : Statistiques de Chaîne
```python
text = input("Entrez du texte : ")

length = len(text)
spaces = text.count(' ')
uppercase = sum(1 for c in text if c.isupper())
lowercase = sum(1 for c in text if c.islower())
digits = sum(1 for c in text if c.isdigit())

print(f"Longueur : {length}")
print(f"Espaces : {spaces}")
print(f"Majuscules : {uppercase}")
print(f"Minuscules : {lowercase}")
print(f"Chiffres : {digits}")
```

### Solution 10 : Analyseur d'Email
```python
email = input("Entrez l'email : ")
parts = email.split('@')
username = parts[0]
domain = parts[1]

print(f"Nom d'utilisateur : {username}")
print(f"Domaine : {domain}")
```

### Solution 11 : Vérificateur de Palindrome
```python
word = input("Entrez un mot : ").lower()
reversed_word = word[::-1]
is_palindrome = (word == reversed_word)

print(f"Est un palindrome : {is_palindrome}")
```

### Solution 12 : Censure de Texte
```python
text = input("Entrez du texte : ")
bad_word = input("Mot à censurer : ")
censored = text.replace(bad_word, "*" * len(bad_word))

print(f"Censuré : {censored}")
```

### Solution 13 : Générateur de Reçu
```python
item1 = input("Nom de l'article 1 : ")
price1 = float(input("Prix de l'article 1 : "))

item2 = input("Nom de l'article 2 : ")
price2 = float(input("Prix de l'article 2 : "))

item3 = input("Nom de l'article 3 : ")
price3 = float(input("Prix de l'article 3 : "))

subtotal = price1 + price2 + price3
tax = subtotal * 0.08
total = subtotal + tax

print("\n" + "="*30)
print(f"{item1:20} ${price1:>7.2f}")
print(f"{item2:20} ${price2:>7.2f}")
print(f"{item3:20} ${price3:>7.2f}")
print(" "*20 + "-"*10)
print(f"{'Sous-total':20} ${subtotal:>7.2f}")
print(f"{'Taxe (8%)':20} ${tax:>7.2f}")
print(f"{'Total':20} ${total:>7.2f}")
print("="*30)
```

### Solution 14 : Convertisseur de Température
```python
temp = float(input("Entrez la température : "))
direction = input("Convertir en (F)ahrenheit ou (C)elsius ? ").upper()

if direction == 'F':
    result = temp * 9/5 + 32
    print(f"{temp}°C = {result:.2f}°F")
else:
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.2f}°C")
```

### Solution 15 : Générateur de Mad Libs
```python
noun = input("Entrez un nom : ")
verb = input("Entrez un verbe : ")
adjective = input("Entrez un adjectif : ")
adverb = input("Entrez un adverbe : ")

story = f"""
Il était une fois, il y avait un {adjective} {noun}.
Chaque jour, il {verb}ait {adverb} à travers la prairie.
Les autres {noun}s étaient émerveillés par la façon dont il pouvait {verb}er {adverb}.
Fin.
"""

print(story)
```

</details>

---

*Excellent travail pour avoir pratiqué les bases ! Passez aux problèmes de flux de contrôle ensuite.*
