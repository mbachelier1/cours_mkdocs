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
   ^
RATA        les deux lettres sont égales, on continue à comparer
   ^

PATATE
  ^
RATA
  ^

PATATE
 ^
RATA
 ^

PATATE
^
RATA        les deux lettres diffèrent, on décale vers la droite
^

PATATE
    ^
 RATA       idem
    ^     

PATATE
     ^
  RATA
     ^      terminé : RATA n'est pas dans PATATE
``` 

Mais tout n'est pas perdu car on peut améliorer l'algorithme :
```
FABRIQUER
  ^
POT         les lettres diffèrent et il n'y a pas de B dans POT donc on peut
  ^         continuer en décalant POT de 3 lettres !

FABRIQUER
     ^
   POT      idem
     ^

FABRIQUER
        ^
      POT
        ^   terminé ! 
```

Comme on peut le constater, seules 3 comparaisons ont été nécessaires pour conclure. Avec l'algorithme
naïf il en aurait fallu 6. Ceci dit, que faire quand on compare le dernier caractère du motif avec un caractère du texte 
et que ceux-ci sont différent mais que le caractère du texte apparaît quand même dans le motif ?

Regardons l'exemple suivant :
```
ANTICONSTITUTIONNELLEMENT
      ^                     les 2 lettres diffèrent mais O apparait dans CONIQUE,
CONIQUE                     plus précisement 5 caractères à gauche du E
      ^                     donc on aligne les deux O 
ANTICONSTITUTIONNELLEMENT
          ^
    CONIQUE                 T n'est pas dans CONIQUE
          ^

ANTICONSTITUTIONNELLEMENT
                 ^
           CONIQUE          les 2 lettres sont égales, on continue à comparer
                 ^
ANTICONSTITUTIONNELLEMENT
                ^
           CONIQUE          les 2 lettres diffèrent mais N apparait dans CONIQUE
                ^           4 lettres à gauche de E donc on aligne les N

ANTICONSTITUTIONNELLEMENT
                    ^
              CONIQUE       on continue à comparer
                    ^ 

ANTICONSTITUTIONNELLEMENT
                   ^        les lettres diffèrent et il n'y a pas de L dans conique
              CONIQUE       mais en décalant, on dépasse la fin du texte
```
PRACAC
   CAC
