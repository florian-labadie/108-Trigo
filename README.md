---

# Trigonometric Functions on Matrices

Ce projet implémente l'application de fonctions trigonométriques et hyperboliques à des matrices en utilisant des séries de puissances. Le programme en Python peut calculer des fonctions comme l'exponentielle, le cosinus, le sinus, le cosinus hyperbolique et le sinus hyperbolique pour une matrice donnée.

## Table des Matières
1. [Introduction]
2. [Modèle Mathématique]
3. [Prérequis]
4. [Installation]
5. [Utilisation]
6. [Sortie du Programme]
7. [Exemples]
8. [Contributeurs]
9. [Licence]

## Introduction

Ce projet permet d'appliquer des fonctions mathématiques à des matrices en utilisant des séries de puissances. Les fonctions disponibles incluent l'exponentielle, le cosinus, le sinus, le cosinus hyperbolique et le sinus hyperbolique.

## Modèle Mathématique

La fonction exponentielle peut être écrite comme une série de puissances :

![image](https://github.com/florian-labadie/108-Trigo/assets/146172365/63f0b307-b73a-40e3-bccd-6a0d3d21187f)

De même, d'autres fonctions comme les fonctions trigonométriques et hyperboliques peuvent être exprimées sous forme de séries de puissances. Ces séries sont particulièrement utiles pour les approximations rapides de ces fonctions et peuvent être utilisées pour exponentier divers objets mathématiques, tels que des matrices.

## Prérequis

- Python 3
- NumPy pour les calculs matriciels

## Installation

Clonez le dépôt Git :

```bash
git clone https://github.com/votre-utilisateur/trigo-matrices.git
cd trigo-matrices
```

Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

## Utilisation

Le programme prend deux arguments principaux :
- `fun` : La fonction à appliquer à la matrice (parmi "EXP", "COS", "SIN", "COSH" et "SINH").
- `ai` : Les coefficients de la matrice (fournis en une seule ligne).

Exécutez le programme comme suit :

```bash
./108trigo fun a0 a1 a2 ...
```

### Arguments

- `fun` : Fonction à appliquer (parmi "EXP", "COS", "SIN", "COSH" et "SINH").
- `ai` : Coefficients de la matrice.

## Sortie du Programme

Le programme génère la matrice résultante après l'application de la fonction spécifiée, par exemple :

```
~/B-MAT-200> ./108trigo COS 4 5 9 3 3 5 0 1 9
0.70 -0.43 -1.94
-0.16 0.67 -1.23
-0.06 -0.15 0.07
```

## Exemples

### Utilisation avec la fonction COS

Pour appliquer la fonction COS à une matrice 3 x 3:

```bash
./108trigo COS 4 5 9 3 3 5 0 1 9
```

Sortie attendue :

```
0.70 -0.43 -1.94
-0.16 0.67 -1.23
-0.06 -0.15 0.07
```

### Utilisation avec la fonction EXP

Pour appliquer la fonction EXP à une matrice 2 x 2:

```bash
./108trigo EXP 1 2 3 4
```

Sortie attendue :

```
51.97 74.74
112.10 164.07
```

### Utilisation avec la fonction SINH

Pour appliquer la fonction SINH à une matrice 2 x 2:

```bash
./108trigo SINH 1 0 2 0
```

Sortie attendue :

```
1.18 0.00
2.35 0.00
```

## Contributeurs

- Nom du Contributeur 1 ([GitHub](https://github.com/contributeur1))
- Nom du Contributeur 2 ([GitHub](https://github.com/contributeur2))

---
