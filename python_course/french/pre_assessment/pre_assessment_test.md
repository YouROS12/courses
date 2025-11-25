# Test de Pré-évaluation Python

**Limite de temps :** 30 minutes
**Questions :** 20
**Instructions :** Répondez à toutes les questions du mieux que vous pouvez. Ne cherchez pas les réponses !

---

## Section 1 : Concepts de Base (Questions 1-5)

### Question 1
Quel est le résultat de ce code ?
```python
x = 5
y = 2
print(x // y)
```
- A) 2.5
- B) 2
- C) 3
- D) Erreur

**Votre réponse :** ______

---

### Question 2
Lequel des éléments suivants n'est PAS un nom de variable valide en Python ?
- A) `my_var`
- B) `_private`
- C) `2nd_place`
- D) `myVar2`

**Votre réponse :** ______

---

### Question 3
Qu'affiche ce code ?
```python
text = "Python"
print(text[1:4])
```
- A) Pyt
- B) yth
- C) Pyth
- D) ytho

**Votre réponse :** ______

---

### Question 4
Comment obtenir une entrée utilisateur en Python ?
- A) `get_input()`
- B) `read()`
- C) `input()`
- D) `scanf()`

**Votre réponse :** ______

---

### Question 5
Quel est le résultat de `"3" + "3"` en Python ?
- A) 6
- B) 33
- C) "6"
- D) "33"

**Votre réponse :** ______

---

## Section 2 : Flux de Contrôle (Questions 6-10)

### Question 6
Qu'affichera ce code ?
```python
x = 10
if x > 5:
    print("A")
elif x > 15:
    print("B")
else:
    print("C")
```
- A) A
- B) B
- C) C
- D) AB

**Votre réponse :** ______

---

### Question 7
Combien de fois cette boucle s'exécutera-t-elle ?
```python
for i in range(3):
    print(i)
```
- A) 2 fois
- B) 3 fois
- C) 4 fois
- D) Infini

**Votre réponse :** ______

---

### Question 8
Quel est le résultat ?
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
- A) 0 1 2
- B) 0 1 2 3
- C) 1 2 3
- D) Boucle infinie

**Votre réponse :** ______

---

### Question 9
Quel opérateur signifie "différent de" ?
- A) `!=`
- B) `<>`
- C) `/=`
- D) `!==`

**Votre réponse :** ______

---

### Question 10
Que fait `break` dans une boucle ?
- A) Met en pause la boucle
- B) Sort de la boucle
- C) Passe à l'itération suivante
- D) Redémarre la boucle

**Votre réponse :** ______

---

## Section 3 : Structures de Données (Questions 11-15)

### Question 11
Quel est le résultat ?
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])
```
- A) 1
- B) 5
- C) -1
- D) Erreur

**Votre réponse :** ______

---

### Question 12
Comment ajouter un élément à la fin d'une liste ?
- A) `list.add(item)`
- B) `list.append(item)`
- C) `list.insert(item)`
- D) `list.push(item)`

**Votre réponse :** ______

---

### Question 13
Quel est le résultat ?
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
```
- A) Alice
- B) "Alice"
- C) name
- D) Erreur

**Votre réponse :** ______

---

### Question 14
Quelle structure de données n'autorise PAS les valeurs en double ?
- A) Liste
- B) Tuple
- C) Ensemble
- D) Dictionnaire

**Votre réponse :** ______

---

### Question 15
Comment créer un dictionnaire vide ?
- A) `dict = []`
- B) `dict = {}`
- C) `dict = ()`
- D) `dict = set()`

**Votre réponse :** ______

---

## Section 4 : Fonctions et Avancé (Questions 16-20)

### Question 16
Que retourne cette fonction ?
```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
```
- A) 7
- B) 12
- C) 34
- D) None

**Votre réponse :** ______

---

### Question 17
Quelle est la bonne façon de définir une fonction en Python ?
- A) `function myFunc():`
- B) `def myFunc():`
- C) `func myFunc():`
- D) `define myFunc():`

**Votre réponse :** ______

---

### Question 18
Comment ouvrir un fichier en lecture en Python ?
- A) `file = open("data.txt", "r")`
- B) `file = read("data.txt")`
- C) `file = open("data.txt", "read")`
- D) `file = File("data.txt")`

**Votre réponse :** ______

---

### Question 19
Que fait ce code ?
```python
try:
    x = int("hello")
except ValueError:
    print("Error!")
```
- A) Plante avec une erreur
- B) Affiche "Error!"
- C) Affiche "hello"
- D) Ne fait rien

**Votre réponse :** ______

---

### Question 20
Quel est le résultat ?
```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)
```
- A) [1, 2, 3, 4, 5]
- B) 15
- C) 12345
- D) Erreur

**Votre réponse :** ______

---

## Corrigé

<details>
<summary>Cliquez pour révéler les réponses (seulement après avoir terminé le test !)</summary>

1. **B** - `//` est la division entière, 5 // 2 = 2
2. **C** - Les noms de variables ne peuvent pas commencer par un chiffre
3. **B** - Le découpage [1:4] obtient les indices 1, 2, 3 (pas 4 inclus) = "yth"
4. **C** - `input()` est la fonction pour obtenir une entrée utilisateur
5. **D** - Concaténation de chaînes : "3" + "3" = "33"
6. **A** - La première condition (x > 5) est Vraie, donc affiche "A" et s'arrête
7. **B** - range(3) donne 0, 1, 2 (3 valeurs)
8. **A** - Affiche 0, 1, 2 (tant que count est inférieur à 3)
9. **A** - `!=` signifie différent de
10. **B** - `break` sort complètement de la boucle
11. **B** - L'indexation négative : -1 est le dernier élément (5)
12. **B** - `.append()` ajoute un élément à la fin de la liste
13. **A** - L'accès à une valeur de dictionnaire par clé retourne "Alice" (sans guillemets dans la sortie)
14. **C** - Les ensembles suppriment automatiquement les doublons
15. **B** - `{}` crée un dictionnaire vide
16. **B** - 3 * 4 = 12
17. **B** - Le mot-clé `def` définit une fonction
18. **A** - `open(filename, "r")` ouvre un fichier en lecture
19. **B** - Try-except capture la ValueError et affiche "Error!"
20. **B** - sum([1,2,3,4,5]) = 15

</details>

---

## Explications Détaillées

<details>
<summary>Cliquez pour les explications détaillées de chaque réponse</summary>

### Explication Question 1
L'opérateur `//` effectue une **division entière** (division euclidienne), qui divise et arrondit vers le bas au nombre entier le plus proche. 5 // 2 = 2.5 arrondi vers le bas = 2.

**Sujets connexes :** Chapitre 1 (Opérateurs)

### Explication Question 2
Les noms de variables doivent commencer par une lettre ou un trait de soulignement, jamais par un chiffre. `2nd_place` commence par un chiffre, ce qui le rend invalide.

**Sujets connexes :** Chapitre 1 (Variables)

### Explication Question 3
Le découpage de chaînes `[start:end]` inclut l'indice de début mais exclut l'indice de fin. `text[1:4]` obtient les caractères aux indices 1, 2 et 3, qui sont "y", "t", "h".

**Sujets connexes :** Chapitre 2 (Découpage de Chaînes)

### Explication Question 4
La fonction `input()` est utilisée pour obtenir une entrée utilisateur en Python. Elle retourne toujours une chaîne.

**Sujets connexes :** Chapitre 2 (Entrée Utilisateur)

### Explication Question 5
Lors de l'utilisation de `+` avec des chaînes, Python les concatène. "3" + "3" = "33" (les deux sont des chaînes, pas des nombres).

**Sujets connexes :** Chapitre 2 (Opérations sur les Chaînes)

### Explication Question 6
Dans les chaînes if-elif-else, Python s'arrête à la **première condition Vraie**. Puisque `x > 5` est Vrai, il affiche "A" et ne vérifie pas le elif.

**Sujets connexes :** Chapitre 3 (Conditions)

### Explication Question 7
`range(3)` produit 0, 1, 2 (trois valeurs). La boucle s'exécute une fois pour chaque valeur, donc 3 fois.

**Sujets connexes :** Chapitre 4 (Boucles)

### Explication Question 8
La boucle s'exécute tant que count < 3. Elle affiche 0, puis 1, puis 2, puis count devient 3 et la condition devient Fausse.

**Sujets connexes :** Chapitre 4 (Boucles While)

### Explication Question 9
L'opérateur `!=` vérifie si deux valeurs ne sont pas égales. C'est l'opposé de `==` (égal à).

**Sujets connexes :** Chapitre 3 (Opérateurs de Comparaison)

### Explication Question 10
`break` sort immédiatement de la boucle, quelle que soit la condition de la boucle. Le programme continue après la boucle.

**Sujets connexes :** Chapitre 4 (Instruction Break)

### Explication Question 11
L'indexation négative compte depuis la fin : -1 est le dernier élément, -2 est l'avant-dernier, etc. Donc `my_list[-1]` est 5.

**Sujets connexes :** Chapitre 5 (Listes)

### Explication Question 12
La méthode `.append()` ajoute un élément à la fin d'une liste. Les autres options n'existent pas ou fonctionnent différemment.

**Sujets connexes :** Chapitre 5 (Méthodes de Liste)

### Explication Question 13
L'accès à un dictionnaire avec une clé retourne la valeur correspondante. `my_dict["name"]` retourne la chaîne Alice.

**Sujets connexes :** Chapitre 6 (Dictionnaires)

### Explication Question 14
Les ensembles maintiennent automatiquement l'unicité - si vous essayez d'ajouter un doublon, il est ignoré. Les listes, tuples et dictionnaires (valeurs) peuvent avoir des doublons.

**Sujets connexes :** Chapitre 8 (Ensembles)

### Explication Question 15
`{}` crée un dictionnaire vide. `[]` est une liste vide, `()` est un tuple vide, et `set()` crée un ensemble vide.

**Sujets connexes :** Chapitre 6 (Dictionnaires)

### Explication Question 16
La fonction multiplie 3 * 4 et retourne 12. L'instruction `return` renvoie cette valeur à l'appelant.

**Sujets connexes :** Chapitre 7 (Fonctions)

### Explication Question 17
Les fonctions en Python sont définies en utilisant le mot-clé `def`, suivi du nom de la fonction et des parenthèses.

**Sujets connexes :** Chapitre 7 (Fonctions)

### Explication Question 18
La fonction `open()` avec le mode "r" ouvre un fichier en lecture. "w" est pour l'écriture, "a" est pour l'ajout.

**Sujets connexes :** Chapitre 9 (Entrée/Sortie de Fichiers)

### Explication Question 19
Le bloc try-except capture les erreurs. Lorsque `int("hello")` échoue avec ValueError, le bloc except s'exécute et affiche "Error!".

**Sujets connexes :** Chapitre 10 (Gestion des Erreurs)

### Explication Question 20
La fonction `sum()` additionne tous les nombres dans une liste. sum([1,2,3,4,5]) = 1+2+3+4+5 = 15.

**Sujets connexes :** Chapitre 5 (Listes), Fonctions Intégrées

</details>

---

## Que Faire Après

1. **Comptez vos réponses correctes** (sur 20)
2. **Calculez le pourcentage** (correct / 20 × 100)
3. **Révisez les questions manquées** - comprenez pourquoi vous vous êtes trompé
4. **Consultez le guide de notation** dans [README.md](README.md)
5. **Commencez le cours** au chapitre recommandé
6. **Repassez ce test** après avoir terminé le cours pour voir vos progrès !

---

**Votre Score :** _____ / 20 (____%)

**Point de Départ Recommandé :** Chapitre _____

**Date de Passage :** __________

---

*Rappelez-vous : Ce test n'est qu'un point de départ. Tout le monde apprend à son propre rythme !*
