# Recherche textuelle

Il s'agit pour nous de trouver un motif (*pattern* en anglais) dans un texte.

## L'algorithme naïf

La manière la plus simple de procéder est de commencer par comparer les premiers caractères du
texte et du motif

- tant qu'ils sont différents, on compare le premier caractère du motif avec le caractère du texte suivant;
- si ils sont égaux alors on retient la position du caractère dans le texte et tant qu'ils sont égaux
ou que l'on n'est pas arrivé au bout du motif ou de la chaine, on compare les caractères suivants. Si on a
atteint la fin du motif, c'est qu'il figure dans le texte à la position retenue.

Cet algorithme n'est pas très performant, voici un cas pathologique :

- prenons pour motif $M$, un mot de $m$ caractères;
- considérons le motif  $M'$ composé des $m-1$ premiers caractères de $M$ auquel on ajoute 
en guise de dernier caractère un caractère différent du dernier de $M$;
- fabriquons un texte composé d'une répétition de $M'$ et appelons $n$ sa longueur.

Dans ce cas l'algorithme va nécessiter $n\times m$ comparaisons pour déterminer que $M$ ne figure
pas dans le texte.

On pourrait alors penser à 

- aligner le motif avec le texte;
- commencer par comparer le dernier caractère du motif avec le caractère correspondant du texte;
- tant qu'ils sont égaux et qu'on a pas épuisé les lettres du motif, on " se décale d'un cran vers la gauche ";
- tant qu'ils sont différents et qu'on est pas arrivé au bout du texte, on décale le motif d'un cran vers la droite.

Malheureusement, cet algorithme souffre des mêmes faiblesses que son prédécesseur comme le montre l'exemple suivant :
```
PATATE
   =
RATA        les deux lettres sont égales, on continue à comparer

PATATE
  =
RATA

PATATE
 =
RATA

PATATE
≠
RATA        les deux lettres diffèrent, on décale vers la droite

PATATE
    ≠
 RATA       idem    

PATATE
     ≠
  RATA      terminé : RATA n'est pas dans PATATE
``` 

Mais tout n'est pas perdu car on peut améliorer l'algorithme :
```
FABRIQUER
  ≠
POT         les lettres diffèrent et il n'y a pas de B dans POT donc on peut
            continuer en décalant POT de 3 lettres !
FABRIQUER
     ≠
   POT      idem

FABRIQUER
        ≠
      POT
            terminé ! 
```

Comme on peut le constater, seules 3 comparaisons ont été nécessaires pour conclure. Avec l'algorithme
naïf il en aurait fallu 6. Ceci dit, que faire quand on compare le dernier caractère du motif avec un caractère du texte 
et que ceux-ci sont différent mais que le caractère du texte apparaît quand même dans le motif ?

Regardons l'exemple suivant :
```
ANTICONSTITUTIONNELLEMENT   On commence ainsi
      ^
CONIQUE
      
ANTICONSTITUTIONNELLEMENT   Les 2 lettres diffèrent mais N apparait dans CONIQUE
      ≠                     donc on aligne les N
CONIQUE
      
ANTICONSTITUTIONNELLEMENT   
          ^                 
    CONIQUE
          
ANTICONSTITUTIONNELLEMENT   Mais à ce moment là les 2 lettres diffèrent et T n'appparaît
          ≠
    CONIQUE                 pas dans CONIQUE donc on peut décaler de 7 lettres
          
ANTICONSTITUTIONNELLEMENT
                 ^
           CONIQUE
                 
ANTICONSTITUTIONNELLEMENT   Les 2 coïncident
                 =
           CONIQUE
                 
ANTICONSTITUTIONNELLEMENT   Mais
                ≠
           CONIQUE
                
ANTICONSTITUTIONNELLEMENT
                        ^
                  CONIQUE
                        ^
ANTICONSTITUTIONNELLEMENT
                        ≠
                  CONIQUE
                        ≠
```

La méthode que l'on vient d'appliquer est l'algorithme de [Boyer-Moore-Horspool](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore-Horspool).

## L'algorithme de Boyer-Moore-Horspool

Ce qu'il faut retenir c'est que

- Il y a d'abord pré-traitement du motif à rechercher pour établir une *table de sauts*.
- On compare le motif avec le texte en commençant par le dernier caractère du motif.
- Tant que les caractères coïncident on compare les caractères précédents (et éventuellement on trouve le motif).
- Dès que les caractères ne coïncident pas, on utilise la table de saut avec le caractère du texte aligné avec le dernier caractère du motif.

### Exemple

On considère la chaîne de caractères JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE.

On voudrait savoir si le motif TROUVER figure dans cette chaîne.

#### Pré-traitement du motif


Commençons par établir la table de saut du motif. C'est simple : 

- on parcourt le motif caractère par caractère jusqu'à l'avant dernier;
- à chaque fois on note le nombre de caractères qui le sépare du dernier;
- si un caractère apparaît plusieurs fois, c'est la dernière qui prime;
- le nombre que l'on obtient est l'amplitude du décalage à faire subir au motif lorsque son dernier caractère est
aligné avec le caractère courant;
- toutes les autres lettres n'apparaissent pas dans le motif (ou alors à la fin du motif et seulement à la fin) et donc
on peut leur associer une saut d'amplitude la longueur du motif.

| caractère | amplitude du saut |  
|:--------: |:----------------: |
| T 	    |  6 	            | 
|  R  	    |  5  	            |  
|   O       |  4  	            | 
|   U  	    |  3  	            | 
|   V       |  2  	            | 
|   E       |  1              	| 
| autre     |  7             	| 


#### Parcours du texte

```
JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    On commence ainsi
      ^
TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
      ≠
TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un I on décale de 7
             ^
       TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
             ≠
       TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un E on décale de 1
              ^
        TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
              ≠
        TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un N on décale de 7
                     ^
               TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
                     ≠
               TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un O on décale de 4
                         ^
                   TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres égales, on continue à comparer
                         =                  en allant de droite à gauche
                   TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
                        ≠
                   TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un R on décale de 5
                              ^
                        TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes
                              ≠
                        TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Pour un A on décale de 7
                                     ^
                               TROUVER

JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE    Lettres différentes, on devrait décaler mais on dépasserait 
                                     ≠      donc c'est terminé
                               TROUVER
```

L'algorithme a nécéssité 8 comparaisons, on se doute qu'il en aurait fallu bien plus avec l'algorithme naïf.

!!! danger "Programmation de l'algorithe de Boyer-Moore-Horspool"

    [L'activité est ici.](https://capytale2.ac-paris.fr/web/c-auth/list?returnto=/web/code/).
