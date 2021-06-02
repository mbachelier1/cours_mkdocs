# Calculabilité et décidabilité

## Un peu d'Histoire et des définitions

### Algorithme

Depuis l'Antiquité l'humanité utilise des *méthodes de calcul* pour résoudre des problèmes, mais jusqu'au début du
vingtième siècle on n'avait aucune définition précise de ce qu'est une méthode de calcul.

Pourtant lors du Congrès International des Mathématiciens de Paris de 1900, David Hilbert a formulé 24 problèmes, dont
le dixième dont l'énoncé peut être vulgarisé en :

« Existe-t-il une méthode générale pour déterminer quelles équations diophantiennes on des solutions et quelles
équations diophantiennes n'en ont pas ? »

??? note "Equations diophantiennes"

    Une équation diophantienne est une équation 

    - à une ou plusieurs inconnues;

    - polynomiale : ne figurent que des puissances entières des inconnues;

    - à coefficients entiers;

    - dont on cherche des solutions entières.

    $x^2-3x+2 = 0$ est une équation diophantienne de solution 1 et 2.

    $x^2+y^2=z^2$ en est une autre, ses solutions sont les triplets pythagoriciens.

    $3x^5+2xyz^3+y^2-z+2=0$ en est une dernière...

Ce sont les mathématiciens Church, Kleene, Turing et Gödel qui, entre 1931 et 1936 ont identifié la notion d'algorithme.

Chacun d'entre eux s'intéressa à sa manière et plus ou moins indépendamment des autres à une catégorie de fonctions. Ils
reconnurent ensuite que ces différentes classes coïncidaient et appelèrent cette classe la classe des fonctions
*calculables*. C'est ce qu'on appelle la *thèse de Church* : tous les modèles de calculs qui ont été utilisés pour
expliquer ce qu'est une fonction calculable sont équivalents.

!!! info "Fonction calculable"

    Une fonction est dite calculable s'il existe une façon finie de la décrire qui permette effectivement d'en
    calculer toutes les valeurs.

Cette définition fixe également la notion d'algorithme. Ce sont les travaux de Turing qui ont abouti la définition
d'algorithme la plus pratique à utiliser : en 1936 la notion d'algorithme était acquise.

!!! info "Algorithme"

    Un algorithme est suite finie d'instructions qu'une machine de Turing peut effectuer.

Depuis, on s'est employé à créer des entités distinctes des machines de Turing, mais qui sont dite *Turing-complètes*,
c'est-à-dire qui peuvent « faire tout ce que peut faire une machine de Turing »

Les langages de programmation que nous connaissons (Python, Java, C++ *et cætera) sont Turing-complets (ouf !), mais
HTML seul (sans CSS) n'est pas Turing-complet.

### Fonction calculable

Dans le cadre de notre cours on peut donc reformuler :

!!! info "Fonction calculable (deuxième définition)"

    Une fonction est calculable si on peut la programmer (en Python par exemple).

### Problème décidable

Dès lors, on peut s'intéresser à la notion de *problème décidable*. Un problème de *décision* peut s'envisager ainsi

|                                              cas général                                              |               exemple 1              | exemple 2                                     |
|:-----------------------------------------------------------------------------------------------------:|:------------------------------------:|-----------------------------------------------|
| Nom du problème                                                                                       | Primalité d'un entier                | Problème de l'arrêt                           |
| Donnée : spécification d'une <br> instance du problème                                                | un entier naturel                    | un programme<br>(écrit en Python par exemple) |
| Réponse : propriété portant sur<br> une instance qui spécifie les<br> instances positives du problème | décider si ce <br>nombre est premier | décider si ce programme <br> s'arrête         |

Sans rentrer dans les détails, on peut associer aux problèmes de décision des fonctions de décision. Un problème est
alors appelé *décidable* si la fonction associée est calculable. Cela nous permet de formuler une définition :

!!! info "Problème décidable"

    Un problème est décidable si on peut écrire une fonction (en Python ou autre) qui 
    
    - en entrée prend les données du problème

    - renvoie `#!python True` ou `#!python False` suivant que les les données satisfont le problème ou non.  

Par exemple, le problème « $n\in\mathbb{N}$ est-il premier ? » est-il décidable :

```python
def est_premier(n: int) -> bool:
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
```

L'algorithme implémenté en Python est fort peu efficace mais là n'est pas le problème : il existe. Donc le problème de
la primalité d'un entier positif est décidable.

Dire qu'un problème est *indécidable* signifie donc qu'il n'existe pas d'algorithme permettant de résoudre ce problème
dans tous les cas (quelles que soient les données du problème).

### Nombre calculable

Tant que nous y sommes, définissons ce qu'est un nombre calculable : 

!!! info "Nombre calculable"

    Un nombre réel est calculable si et seulement si il existe un algorithme permettant de calculer autant de décimales
    que l'on veut de l'écriture en base 10 de ce réel.

Évidemment si le nombre n'est pas une fraction, son écriture décimale n'est pas périodique, il est donc hors de question
de chercher à les connaître toutes (sauf cas particulier où l'on a nous même fabriqué l'écriture décimale du nombre).

Par exemple, on peut montrer que le nombre $e$ (celui qui permet de construire la fonction exponentielle) vaut 

$$\sum_{k=0}^{+\infty}\frac{1}{k!}=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\ldots$$

Avec $0!=1$, rappelons-le.

Il y a une infinité de termes dans la somme (c'est une limite), mais en prenant un nombre suffisant des premiers termes
de cette somme, on peut en déterminer autant de décimales de $e$ que l'on désire.

??? note "Exercice"

    1. Programmer une fonction `factorielle` dynamique.
    2. Programmer une fonction `approx` qui
        - en entrée prend un entier positif $n$.
        - renvoie $\sum_{k=0}^{+n}\frac{1}{k!}$ en calculant suivant la règle de la photo de classe pour
        minimiser les erreurs d'arithmétique en virgule flottante.
    3. Programmer la fonction `decimales_de_e` qui
        - en entrée prend un entier d positif;
        - renvoie l'écriture décimale de $e$ avec les $n$ premières décimales exactes.
  
    Pour la dernière question, on pourra utiliser la fonction `#!python round` : `#!python round(a,4)` tronque `a` à la quatrième décimale.
  
    **Remarque** : écrit tel quel, ce programme ne permet pas d'afficher beaucoup de décimales : 17 au maximum. Cela est dû
    au format de représentation des `#!python float` de Python. Pour en avoir plus, on pourrait s'y prendre autrement...


## Un programme est une donnée comme les autres

### C'est déjà vrai pour les fonctions

Lorsque nous avons étudié la programmation fonctionnelle, nous avons expliqué qu'il est possible de passer une fonction
en paramètre à une autre fonction.

Voici un exemple :

```python

def nulle_en_zero(f):
	epsilon = 10 ** -6
	return abs(f(0)) < epsilon
```

La fonction `nulle_en_zero` :

- prend en entrée une fonction $f$ (qui est censée être une fonction numérique définie « au voisinage de zéro »);
- renvoie {{pyl('True')}} si $f(0)$ est très petit et {{pyl('False')}} sinon.

### Cela reste vrai pour les programmes

De la même manière, on peut donner un programme en entrée d'un autre programme. D'ailleurs, on le fait plus souvent
qu'on ne le croit :

- Sous Linux / macOS :
    ```bash
    cat fichier.txt
    ```

demande au programme `cat` d'afficher le contenu du fichier `fichier.txt`

- Sous Windows / Linux / macOS :
    ```bash
    python fichier.py
    ```

donne le fichier `fichier.py` à l'*interpréteur* Python pour que celui-ci l'exécute.

- Lorsqu'on a écrit un programme en langage C, tel celui-ci :
    ```cplusplus
    #include <stdio.h>

    int main() {
        printf("Hello World!");
        return 0;
    }  
    ```

et qu'on a sauvegardé ce fichier texte sous le nom `hello_world.c`, alors on utilise un *compilateur* C qui prend en
entrée ce fichier et produit (sous Windows) un fichier exécutable `hello_world.exe`.

- Quand on compresse un programme, on utilise un autre programme pour le compresser.

- Quand on utilise un antivirus, il prend (entre autres) des programmes et les analyse.

- *Et cætera*.


## Un problème indécidable

C'est Alan Turing qui a prouvé le résultat suivant. Il utilisait (évidemment) des machines de Turing dans sa preuve.
Puisque Python est Turing-complet, nous utiliserons Python !

Lorsqu'on programme une fonction, il se peut qu'elle ne s'arrête pas. C'est souvent très embêtant, d'où la question 
suivante :

Existe-t-il une fonction permettant de déterminer si une fonction donnée s'arrête où non et ce, quelle que soit cette 
fonction donnée et les paramètres qu'on lui passe ?

Cette question pose ce que l'on appelle *le problème de l'arrêt*.

Supposons qu'une telle fonction existe, appelons-là `A` :
```python
def A(f,x) ->bool :
  """
  Renvoie True si f(x) s'arrête et False sinon
  """
```

Construisons alors la fonction `D` suivante :

```python
def D(f):
    if A(f,f) is True:
        while True:
            pass
    else:
        return True
```

Que peut-on dire de `D(D)` ?

  - Si `D(D)` se termine, alors cela signifie que `A(D,D)` est faux, donc que `D(D)` ne se termine pas.
  - Si `D(D)` ne se termine pas, alors on est entré dans la boucle `#!python while`, donc `A(D,D)` est vrai et 
  alors `D,(D)` se termine.
  
Dans les deux cas on arrive à une contradiction. Ainsi notre supposition est erronée :

La fonction A n'existe pas. Autrement dit il n'existe pas de programme permettant de déterminer systématiquement
si un programme donné s'arrête ou non. Le problème de l'arrêt est *indécidable*.

## Des nombres incalculables ?

Il est facile de montrer que la majorité des nombres réels sont incalculables, mais pour autant, il a fallu attendre 
< date manquante > pour que Gregory Chaitin exhibe un nombre $\Omega$ non calculable. Sa définition est extrêmement complexe
et repose sur les probabilités d'arrêts de certains algorithmes. 

## Peut-on enfoncer le clou encore un peu plus ?

Oui ! En 1931 Kurt Gödel a démontré le *premier théorème d'incomplétude*, riche en implications tant scientifiques que 
philosophiques. Pour démontrer des théorèmes, les mathématiciens doivent utiliser un *système formel* avec des axiomes, 
*et cætera*. Son théorème énonce que tout système formel assez puissant pour démontrer les théorèmes d'arithmétiques (donc
 en particulier celui que nous utilisons sans vraiment y faire attention) est *incomplet* : Il existe des propositions
pour lesquelles il n'existe ni de preuve qu'elles sont vraies, ni de preuve qu'elles sont fausses.

Ce résultat est à mettre en parallèle avec les notions précédentes même s'il n'est pas de même nature : il dépend du
système formel dans lequel on se place, au contraire de la décidabilité et la calculabilité.
