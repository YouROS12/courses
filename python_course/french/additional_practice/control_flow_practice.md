# Problèmes de Pratique de Flux de Contrôle

Problèmes de pratique pour les Chapitres 3-4 : Conditions et boucles.

---

## Instructions Conditionnelles

### Problème 1 : Classificateur de Note
Écrivez un programme qui classifie une note :
- 90-100 : Excellent
- 80-89 : Bien
- 70-79 : Satisfaisant
- 60-69 : Nécessite une amélioration
- En dessous de 60 : Échec

Gérez les notes invalides (inférieures à 0 ou supérieures à 100).

---

### Problème 2 : Vérificateur d'Année Bissextile
Déterminez si une année est bissextile :
- Divisible par 4 ET non divisible par 100, OU
- Divisible par 400

---

### Problème 3 : Validateur de Triangle
Étant donné trois longueurs de côtés, déterminez s'ils peuvent former un triangle valide.
Règle : La somme de deux côtés quelconques doit être supérieure au troisième côté.

---

### Problème 4 : Calculateur de Réduction
Calculez le prix final en fonction du montant d'achat :
- Moins de 50 $ : Aucune réduction
- 50-100 $ : 10 % de réduction
- 100-200 $ : 15 % de réduction
- Plus de 200 $ : 20 % de réduction

---

### Problème 5 : Vérificateur de Force de Mot de Passe
Vérifiez si un mot de passe est fort. Il doit :
- Avoir au moins 8 caractères
- Contenir au moins une lettre majuscule
- Contenir au moins une lettre minuscule
- Contenir au moins un chiffre

Affichez des commentaires spécifiques pour chaque exigence manquante.

**Indice :** Utilisez .isupper(), .islower(), .isdigit()

---

## Boucles Simples

### Problème 6 : Table de Multiplication
Affichez la table de multiplication pour un nombre donné (1-10).

Exemple pour 5 :
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

### Problème 7 : Somme des Nombres
Calculez la somme de tous les nombres de 1 à N (l'utilisateur fournit N).

---

### Problème 8 : Calculateur de Factorielle
Calculez la factorielle d'un nombre (N!).
Exemple : 5! = 5 × 4 × 3 × 2 × 1 = 120

---

### Problème 9 : Compte à Rebours
Créez un compte à rebours de N à 1, puis affichez "Décollage !"

---

### Problème 10 : Pyramide de Nombres
Affichez une pyramide de nombres :
```
1
12
123
1234
12345
```

**Indice :** Utilisez des boucles imbriquées ou la construction de chaînes

---

## Boucles Avancées

### Problème 11 : Vérificateur de Nombre Premier
Déterminez si un nombre est premier.
Les nombres premiers ne sont divisibles que par 1 et eux-mêmes.

**Indice :** Vérifiez si un nombre entre 2 et racine carrée(n) divise n de manière égale

---

### Problème 12 : Séquence de Fibonacci
Générez les N premiers nombres de la séquence de Fibonacci.
Chaque nombre est la somme des deux précédents.
Commencez par 0, 1.

Exemple pour N=7 : 0, 1, 1, 2, 3, 5, 8

---

### Problème 13 : Inverser un Nombre
Inversez les chiffres d'un nombre.
Exemple : 12345 → 54321

**Indice :** Utilisez le modulo et la division entière dans une boucle

---

### Problème 14 : Somme des Chiffres
Calculez la somme de tous les chiffres d'un nombre.
Exemple : 12345 → 1+2+3+4+5 = 15

---

### Problème 15 : Vérificateur de Nombre Parfait
Un nombre parfait est égal à la somme de ses diviseurs (sauf lui-même).
Exemple : 6 = 1 + 2 + 3

Vérifiez si un nombre est parfait.

---

## Impression de Motifs

### Problème 16 : Triangle Rectangle
Affichez un triangle rectangle d'étoiles :
```
*
**
***
****
*****
```

---

### Problème 17 : Triangle Inversé
Affichez un triangle inversé :
```
*****
****
***
**
*
```

---

### Problème 18 : Pyramide
Affichez une pyramide centrée :
```
    *
   ***
  *****
 *******
*********
```

**Indice :** Combinez espaces et étoiles

---

## Programmes Interactifs

### Problème 19 : Jeu de Devinette de Nombre
Générez un nombre aléatoire entre 1 et 100.
Laissez l'utilisateur deviner jusqu'à ce qu'il trouve le bon nombre.
Fournissez des indices "plus haut" ou "plus bas".

**Indice :** `import random; number = random.randint(1, 100)`

---

### Problème 20 : Calculatrice avec Menu
Créez une calculatrice avec un menu :
```
1. Additionner
2. Soustraire
3. Multiplier
4. Diviser
5. Quitter
```

Continuez à exécuter jusqu'à ce que l'utilisateur choisisse Quitter.
Gérez la division par zéro.

---

## Solutions

<details>
<summary>Cliquez pour révéler les solutions</summary>

### Solution 1 : Classificateur de Note
```python
grade = float(input("Entrez la note (0-100) : "))

if grade < 0 or grade > 100:
    print("Note invalide !")
elif grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Bien")
elif grade >= 70:
    print("Satisfaisant")
elif grade >= 60:
    print("Nécessite une amélioration")
else:
    print("Échec")
```

### Solution 2 : Vérificateur d'Année Bissextile
```python
year = int(input("Entrez l'année : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} est une année bissextile")
else:
    print(f"{year} n'est pas une année bissextile")
```

### Solution 3 : Validateur de Triangle
```python
a = float(input("Côté 1 : "))
b = float(input("Côté 2 : "))
c = float(input("Côté 3 : "))

if a + b > c and b + c > a and a + c > b:
    print("Triangle valide")
else:
    print("Triangle invalide")
```

### Solution 4 : Calculateur de Réduction
```python
amount = float(input("Montant d'achat : $"))

if amount < 50:
    discount = 0
elif amount < 100:
    discount = 0.10
elif amount < 200:
    discount = 0.15
else:
    discount = 0.20

final_price = amount * (1 - discount)
print(f"Réduction : {discount*100}%")
print(f"Prix final : ${final_price:.2f}")
```

### Solution 5 : Vérificateur de Force de Mot de Passe
```python
password = input("Entrez le mot de passe : ")

is_strong = True
feedback = []

if len(password) < 8:
    is_strong = False
    feedback.append("Doit avoir au moins 8 caractères")

if not any(c.isupper() for c in password):
    is_strong = False
    feedback.append("Doit contenir une lettre majuscule")

if not any(c.islower() for c in password):
    is_strong = False
    feedback.append("Doit contenir une lettre minuscule")

if not any(c.isdigit() for c in password):
    is_strong = False
    feedback.append("Doit contenir un chiffre")

if is_strong:
    print("Mot de passe fort !")
else:
    print("Mot de passe faible :")
    for item in feedback:
        print(f"- {item}")
```

### Solution 6 : Table de Multiplication
```python
num = int(input("Entrez un nombre : "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Solution 7 : Somme des Nombres
```python
n = int(input("Entrez N : "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Somme de 1 à {n} = {total}")

# Ou utilisez la formule : total = n * (n + 1) // 2
```

### Solution 8 : Calculateur de Factorielle
```python
n = int(input("Entrez un nombre : "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
```

### Solution 9 : Compte à Rebours
```python
n = int(input("Compte à rebours depuis : "))

for i in range(n, 0, -1):
    print(i)
print("Décollage !")
```

### Solution 10 : Pyramide de Nombres
```python
n = int(input("Nombre de lignes : "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### Solution 11 : Vérificateur de Nombre Premier
```python
num = int(input("Entrez un nombre : "))

if num < 2:
    print("Pas premier")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} est premier")
    else:
        print(f"{num} n'est pas premier")
```

### Solution 12 : Séquence de Fibonacci
```python
n = int(input("Combien de nombres ? "))

a, b = 0, 1
print(a, end=" ")
if n > 1:
    print(b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c

print()  # Nouvelle ligne
```

### Solution 13 : Inverser un Nombre
```python
num = int(input("Entrez un nombre : "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"Inversé : {reversed_num}")

# Ou en utilisant une chaîne : reversed_num = int(str(num)[::-1])
```

### Solution 14 : Somme des Chiffres
```python
num = int(input("Entrez un nombre : "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print(f"Somme des chiffres : {total}")

# Ou en utilisant une chaîne : total = sum(int(d) for d in str(num))
```

### Solution 15 : Vérificateur de Nombre Parfait
```python
num = int(input("Entrez un nombre : "))
divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(f"{num} est un nombre parfait")
else:
    print(f"{num} n'est pas un nombre parfait")
```

### Solution 16 : Triangle Rectangle
```python
n = int(input("Nombre de lignes : "))

for i in range(1, n + 1):
    print("*" * i)
```

### Solution 17 : Triangle Inversé
```python
n = int(input("Nombre de lignes : "))

for i in range(n, 0, -1):
    print("*" * i)
```

### Solution 18 : Pyramide
```python
n = int(input("Nombre de lignes : "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

### Solution 19 : Jeu de Devinette de Nombre
```python
import random

number = random.randint(1, 100)
attempts = 0

print("Devinez le nombre entre 1 et 100 !")

while True:
    guess = int(input("Votre supposition : "))
    attempts += 1

    if guess == number:
        print(f"Correct ! Vous l'avez trouvé en {attempts} tentatives !")
        break
    elif guess < number:
        print("Plus haut !")
    else:
        print("Plus bas !")
```

### Solution 20 : Calculatrice avec Menu
```python
while True:
    print("\n=== Calculatrice ===")
    print("1. Additionner")
    print("2. Soustraire")
    print("3. Multiplier")
    print("4. Diviser")
    print("5. Quitter")

    choice = input("Choisissez (1-5) : ")

    if choice == "5":
        print("Au revoir !")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Choix invalide !")
        continue

    num1 = float(input("Premier nombre : "))
    num2 = float(input("Deuxième nombre : "))

    if choice == "1":
        print(f"Résultat : {num1 + num2}")
    elif choice == "2":
        print(f"Résultat : {num1 - num2}")
    elif choice == "3":
        print(f"Résultat : {num1 * num2}")
    elif choice == "4":
        if num2 == 0:
            print("Impossible de diviser par zéro !")
        else:
            print(f"Résultat : {num1 / num2}")
```

</details>

---

*Excellent travail ! Ces problèmes développent de solides compétences en résolution de problèmes.*
