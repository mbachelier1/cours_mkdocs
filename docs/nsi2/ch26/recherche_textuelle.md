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

## Une idée pour améliorer l'algorithme naif 