# Diviser pour régner

## Un exemple déjà traité

![tours](https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif){align=right width=33%} Nous avons
déjà rencontré des situations où l'on appliquait cette stratégie.

La plus marquante était sans doute celle des *tours de Hanoï* dont voici un script de résolution :

```python
def hanoi(n: int, depart: str, interm: str, dest: str) -> None:
    if n > 0:
        hanoi(n - 1, depart, dest, interm)
        print("Déplacer un palet de", depart, "vers", dest)
        hanoi(n - 1, interm, depart, dest)

```

L'appel

```python
hanoi(3, 'A', 'B', 'C')
```

affiche

```
Déplacer un palet de A vers C
Déplacer un palet de A vers B
Déplacer un palet de C vers B
Déplacer un palet de A vers C
Déplacer un palet de B vers A
Déplacer un palet de B vers C
Déplacer un palet de A vers C
```

## Le principe

L'exemple précédent est caractéristique de la stratégie «diviser pour régner», qui consiste à

1. Décomposer un problème en un ou plusieurs *sous-problèmes* de même nature mais plus petits.

2. Résoudre les sous-problèmes, généralement de manière récursive, jusqu'à ce qu'on arrive aux *cas d'arrêt* :
   des sous-problèmes que l'on sait résoudre immédiatement.

3. Construire la solution au problème initial à partir des solutions des sous-problèmes.

## Le tri fusion

![merge_sort](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-so
rt-example-300px.gif){align=right width=33%} Voici un deuxième exemple d'application de cette stratégie : le *tri
fusion*. On doit cet algorithme à
[John Von Neumann](https://fr.wikipedia.org/wiki/John_von_Neumann).

On dispose d'une liste d'entiers que l'on veut trier dans l'ordre croissant.

1. On scinde cette liste en deux listes de longueurs «à peu près égales».

2. On trie ces listes en utilisant... le tri fusion.

3. On *fusionne* les deux listes triées par ordre croissant pour ne plus en obtenir qu'une.

[Une chorégraphie du tri fusion](https://youtu.be/XaqR3G_NVoo)

Voici comment coder le tri fusion :

On a tout d'abord besoin d'une fonction `scinde` qui renvoie la première moitié et la deuxième moitié de la liste qu'on
lui passe en argument.

```python
def scinde(lst: list) -> tuple:
    return lst[:len(lst) // 2], lst[len(lst) // 2:]
```

Ensuite, on a besoin d'une fonction `fusion` qui, étant donnée deux listes triées, les fusionne.

```python
def fusion(lst1: list, lst2: list) -> list:
    if not lst1 or not lst2: # si l'une des listes est vide
        return lst1 or lst2 # alors on renvoie l'autre
    else:
        a, b = lst1[0], lst2[0]
        if a < b : # sinon on compare leurs premiers éléments
            return [a] + fusion(lst1[1:], lst2) # on place le plus petit en tête et on fusionne le reste
        elif b > a:
            return [b] + fusion(lst1, lst2[1:])
        else : # dans le cas où les 2 éléments sont égaux on peut les placer tous les deux
            return [a, b]+ fusion(lst1[1:], lst2[1:])
```

Enfin, la fonction `tri_fusion`.

```python
def tri_fusion(lst: list) -> list:
    if len(lst) < 2: # cas d'arrêt
        return lst
    lst1, lst2 = scinde(lst) # sinon on scinde
    return fusion(tri_fusion(lst1), tri_fusion(lst2)) # et on fusionne les sous-listes triées
```

## Complexité du tri fusion

notons $n$ la taille de la liste à trier et considérons comme seule *opération élémentaire* le fait d'accéder à un élément 
d'une liste.


À chaque appel récursif, la somme des tailles des deux listes diminue au minimum de 1 : ainsi la complexité de `fusion` 
est au plus $n$, elle est en $\mathcal{O}(n)$.

Ainsi (ne rentrons pas dans les détails) puisque la taille de la 

