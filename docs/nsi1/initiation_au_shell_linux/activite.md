# Initiation au shell Linux

Cette activité est basée sur un travail original de [Martin Quinson](http://people.irisa.fr/Martin.Quinson/)

## Petit tutoriel

Comme les autres systèmes d'exploitation, Linux range les fichiers dans une
arborescence de répertoires. Voici quelques commandes utiles. Tapez-les une à une pour constater le résultat.

- `#!bashpwd` savoir où on est sur le disque (Print Working Directory)
- #!bashmkdir machin` créer un nouveau répertoire nommé machin
- `#!bash ls` lister les fichiers et répertoires du répertoire courant
- `#!bash cd machin` entrer dans le répertoire machin (Change Directory)
- `#!bash pwd`
- `#!bash cd ..` aller dans le répertoire "..", c'est-à-dire un étage plus haut
- `#!bash pwd` 
- `#!bash touch bidule` créer un fichier vide nommé bidule (ou change sa date d'accès si le fichier existe)
- `#!bash ls` 
- `#!bash rm bidule` effacer le fichier bidule. Attention, c'est une opération irréversible.
- `#!bash ls` 
- `#!bash rmdir machin` effacer le répertoire machin (il faut qu'il soit
  vide). On peut aussi utiliser `#!bash rm -r machin` pour effacer
  récursivement `machin` et tout son contenu.
- `#!bash ls` 
- `#!bash clear` permet d'effacer l'écran pour nettoyer.

Au besoin, lisez la documentation de ces commandes avec par exemple
`#!bash man ls` (++q++ pour quiter cette aide).

Sachez aussi que :

- les touches ++up++   et ++down++ du clavier permettent de naviguer dans l'historique des commandes déjà tapées
- la touche ++tab++ (tabulation) permet de compléter un nom de fichier

##1. Créer des arborescences

Il s'agit maintenant de créer l'aborescence suivante.

```
📁 EXO
├── 📁 dir1
│    └── 📁 dir2
│         └── 🖹 doc1
└── 📁 dir3
    └── 🖹 doc2
```

Les logos sont juste là pour l'explication, les noms de fichiers et
répertoires ne doivent contenir que des lettres et des chiffres dans
cet exercice. 

Le répertoire au sommet est l'endroit où commence
l'exercice, noté `EXO`.

Pour commencer l'exercice, dans le terminal, entrez `#!bash bash 01_start`


Coincé? Utilisez la commande `#!bash ls -R` pour afficher
*récursivement* le contenu de tous les répertoires.

Si c'est plus grave, tapez `#!bash cd` pour revenir au répertoire de départ et `#!bash bash 01_start` pour tout recommencer.

Lorsque vous avez terminé, tapez `#!bash bash 01_verif` pour vérifier et passer à l'exercice suivant.

## 2. Renommer et déplacer

Nous avons vu quelques commandes pour se déplacer sur le disque et
pour créer des fichiers et répertoires. Pour ne pas les oublier,
imprimez le [pense-bête du shell](https://framagit.org/mquinson/C-2nd-language/raw/master/refcard/refcard-shell.pdf?inline=false).

Dans cet exercice, nous allons apprendre à déplacer des fichiers.

### Petit tutoriel

Pour commencer, dans le terminal, entrez `#!bash bash 02_start`

Utilisez la commande `#!bash tree` pour voir la situation
initiale.

La commande `#!bash mv` permet de déplacer (MoVe) des fichiers et
répertoires. Sa syntaxe est très facile : De base, 
`#!bash mv toto bidule` permet de renommer le fichier `toto` en `bidule`.
Cela marche aussi si `toto` est un répertoire. Vérifiez le résultat
avec la commande `#!bash tree`.

Si le second paramètre de la commande `#!bash mv` existe, ça doit être un
répertoire dans lequel le premier paramètre est déplacé. Par exemple
`#!bash mv bidule dir1` déplace le fichier `bidule` dans le
répertoire `dir1`. Vérifiez l'état courant avec 
`#!bash tree` ou `#!bash ls -R` (listing récursif).

Enfin, si vous passez plus de deux paramètres à la commande `#!bash mv`, tous
ceux du début de la ligne sont déplacés dans le répertoire indiqué en
dernier paramètre. Par exemple `#!bash mv machin dir1/bidule truc` déplace les fichiers `machin` et `dir1/bidule`
(c'est-à-dire le fichier `bidule` placé dans `dir1`) dans le
répertoire `truc`. Vérifiez l'état actuel avec `#!bash tree`.

La commande `#!bash mv`, comme beaucoup d'autres, accepte beaucoup de
paramètres intéressants. Par exemple `#!bash mv -i [paramètres habituels]`
passe en mode interactif : vous devez confirmer chaque opération qui écrase
un fichier existant.
Consultez le manuel de cette commande en tapant
`#!bash man mv `.

### Au travail

Si vous avez bien suivi le tutoriel, votre arborescence devrait être la suivante:
```
📁 EXO
├── 📁 dir1
│    └── 📁 dir2
│         └── 🖹 doc1
└── 📁 dir3
    └── 🖹 doc2
```

L'objectif est de renommer tous les éléments pour les mettre en
majuscule, comme suit. Il n'est pas possible de juste recréer
l'arborescence, car le contenu des fichiers doc1 et doc2 doit être
préservé.

```
📁 EXO
├── 📁 DIR1
│    └── 📁 DIR2
│         └── 🖹 DOC1
└── 📁 DIR3
    └── 🖹 DOC2
```

Coincé? Utilisez la commande ```tree``` pour afficher récursivement
le contenu de tous les répertoires. 

Si c'est plus grave, tapez ``cd`` pour revenir au répertoire de départ et ``bash 02_start`` pour tout recommencer.

Lorsque vous avez terminé, tapez ``bash 02_verif`` pour vérifier et passer à l'exercice suivant.


## 3. Déplacer en masse

Bien. Vous avez compris comment déplacer des fichiers en shell. Mais
avouez que c'est assez rébarbatif : on irait beaucoup plus vite à la
souris avec un bon navigateur de fichiers. 

Alors, à quoi bon utiliser le shell ? Eh bien, parce que les
opérations non triviales vont beaucoup plus vite à réaliser en shell !

Dans le terminal, entrez ``bash 03_start``.

Affichez le contenu du répertoire ``EXO``. C'est le bazar, non ?

Heureusement pour vous, la commande ```mv *.html web``` va déplacer
tous les fichiers dont le nom termine par `.html` dans le répertoire
`web` (et seulement ceux-là). À la souris, il serait fastidieux de
devoir les sélectionner les uns après les autres.

Dans cet exercice, il vous est demandé de
déplacer tous les fichiers `html` dans le répertoire `web`, les
fichiers `pdf` dans le répertoire `print` (que vous devez créer) et
les fichiers `png` dans le répertoire `image`. 

Avouez que pouvoir déplacer autant de fichiers en une seule commande
est tout de même agréable, non ?

Pour (re)commencer l'exercice, dans le terminal, entrez ``bash 03_start``.

Lorsque vous avez terminé, tapez ``bash 03_verif`` pour vérifier et passer à l'exercice suivant.

## 4. Lire le contenu des fichiers



Commencez donc par un petit ``bash 04_start``.


Il existe de nombreuses commandes pour afficher le contenu des
fichiers à l'écran. La plus simple est ```cat fichier```,
qui affiche le contenu du fichier sur la console. 

Si on affiche un fichier contenant non pas du texte mais du binaire,
on peut avoir des résultats surprenants: 
```cat fichier-binaire``` affiche un fichier peu
intelligible en l'état. Si votre terminal est ... dérangé après un tel
affichage, il suffit de taper ```reset``` pour tout
réinitialiser. 

Si le fichier est plus long, cette méthode permet assez facilement de
voir la fin du contenu. C'est déjà ça. Par exemple, 
```cat fichier_long``` risque de vous remplir l'écran. Et
si on demande à afficher un programme binaire, c'est long ET illisible
à priori: ```cat /bin/cat``` affiche le programme cat
lui-même. 

Si on veut voir le début d'un fichier, on peut utiliser la commande 
```head fichier_long``` qui n'affiche que les premières
lignes du fichier passé. On peut aussi préciser que l'on veut les 50
premières lignes avec l'option ``-n``: ```head -n 50 fichier_long```

De même, la commande ```tail -n 10 fichier_long``` permet
d'afficher les 10 dernières lignes d'un fichier long.
Enfin, la commande ```less fichier_long``` permet
de se promener dans l'affichage d'un fichier : la navigation se fait avec
les mêmes raccourcis que le manuel (le manuel appelle ``less`` en interne).
Pour rappel : les flèches et page vers le haut/bas permettent de se déplacer
dans le fichier, ++q++ quitte le programme et on voit l'aide avec ++h++.

### But de l'exercice

Pour passer à la suite, il suffit de trouver différents mots de passe,
répartis dans différents fichiers du répertoire. 

Normalement ++ctrl+c++ ne fonctionne pas dans le terminal et il faut
sélectionner à la souris puis faire ++ctrl+ins++ pour copier, et
++shift+ins++ pour coller. 

**Ceci dit, dans CoCalc, les développeurs ont eu la bonne idée d'autoriser également les bons vieux ++ctrl+c++ pour copier et 
++ctrl+v++ pour coller, donc il ne faut pas vous en priver.**

Bien entendu, il est presque impossible de taper la bonne commande,
juste du premier coup. On pourrait la copier/coller depuis juste au
dessus avec ++ctrl+ins++ et ++shift+ins++, mais ce serait affreusement
lent et frustrant. Il y a bien mieux : on peut retrouver les commandes
qu'on vient d'écrire simplement avec les flèches haut/bas et les
modifier. 

En fait, le terminal est un truc de fainéants où tout est fait pour
vous simplifier la vie, vous allez voir. Vous avez la flemme de
chercher manuellement dans l'historique la ligne où vous utilisez
``head``? Tapez simplement ++ctrl+r++ pour passer en mode recherche, et
écrivez ``head``. Le shell va fouiller l'historique pour vous. Appuyez
sur ``Entrée`` quand vous l'avez trouvé. Essayez aussi d'utiliser les
flèches pendant/après la recherche ou de refaire ++ctrl+r++ en cours de
recherche: c'est assez bien fait. 


1. Quel est le contenu du fichier `mot-de-passe` ?

2. Quelle information se cache à la fin du fichier `cache-cache-passe` ?

3. Quelle information se cache au début du fichier `cache-cache-passe` ?

4. Quelle information se cache un peu après le début du fichier `cache-cache-passe` ?

5. Quelle information se cache vers le milieu du fichier `cache-cache-passe` ?



Vous ne trouvez pas les informations ? Essayez avec les commandes
``cat``, ``head`` et ``less``.


## 5. Trouver des fichiers

Vous avez l'habitude, maintenant : ``bash 05_start``.

Il arrive souvent qu'on ait besoin de retrouver un fichier sur son
disque. Deux commandes sont bien pratiques en pareille situation.

La commande ``locate`` **qui n'est pas installée sur CoCalc** utilise une base de données des fichiers sur
disque et permet de retrouver très rapidement un fichier par son nom.
Le défaut est qu'il faut que le fichier soit là depuis assez longtemps
pour qu'il ait été indexé dans la base. Mais si vous cherchez un
fichier dont vous connaissez une partie du nom sans savoir du tout où
il se trouve, cette commande est faite pour vous. 

La commande ``find`` qui elle, en revanche, est installée sur CoCalc, permet de fouiller le disque de façon bien plus
approfondie. Par exemple, la commande ```find ddd -name "pas-la"```
cherche dans le répertoire ``ddd`` un fichier dont le nom est "pas-la"
(il y en a un, juste pour l'exemple).

### But de l'exercice

La commande ``find`` offre de nombreuses autres possibilités, que vous
pourrez découvrir en lisant la documentation avec ```man find```.
Cela vous permettra de répondre aux questions suivantes.

Comme précédemment, pas question de retaper la ligne de commande en
entier à chaque tentative. Soyez fainéants. Utilisez l'historique des
commandes.
Les informaticiens sont de grands fainéants prêts à tout pour faire
travailler l'ordinateur à leur place.

#### Dans aaa

Un fichier nommé 'ici' se cache quelque part dans le répertoire 'aaa',
mais la commande ```tree``` n'aide pas beaucoup. Il va
falloir utiliser ``find``!


1. Que contient ce fichier 'ici'?

[reponse1]:<>(find aaa -name "ici")

#### Dans bbb

Cette fois, on ne connaît même pas le nom du fichier. On sait juste
que c'est un fichier, et que le prédicat ``-type`` de ``find`` peut
nous aider.

Notez que pour chercher dans le manuel, il faut appuyer sur la touche
++slash++ après l'avoir ouvert avec ```man find```. Tapez ensuite
la chaîne à chercher (par exemple ``-type``) et entrée. On saute à
l'occurrence suivante avec ++n++ (précédente avec ++shift+n++), et on quitte le
manuel avec ++q++.

#### Dans ccc

Il y a maintenant une multitude de fichiers, et on cherche celui dont
la taille est supérieure à zéro. Les prédicats ``-size`` ou 
``-empty`` vont probablement nous rendre service, ainsi que les
connecteurs logiques ``-and``,``-or`` ou ``-not``, à vous de voir...


3. Que contient le fichier caché dans 'ccc'?

[reponse3]:<>(find ccc -type f -not -size 0 -exec cat {} \;) 

#### Dans ddd

Cette fois, il y a une multitude de fichiers, et il faut utiliser celui
modifié plus récemment que le fichier ``timestamp`` placé à la racine de `EXO`.
Notez que c'est bien la date de dernière modification qui compte.



4. Que contient le fichier caché dans 'ddd'?

[reponse4]:<>(find ddd -type f -newer timestamp -exec cat {} \;)

## 6. Fouiller des fichiers
...

La commande ```find``` est très pratique pour trouver un fichier
d'après son nom ou ses attributs de fichier, mais elle ne permet pas
d'ouvrir les fichiers à la recherche d'un contenu particulier. C'est
l'un des multiples services que la commande ```grep``` peut rendre.

Grep permet de chercher efficacement un texte donné dans des fichiers
ou des flux de données.  Cet outil est installé sur tous les Unix de
la terre, et il existe des versions pour Windows. Tout les
utilisateurs du terminal utilisent grep de temps à autres.

Allez, un petit `bash 06_start` pour la route...

Voici un exemple : ```grep xeruti aa/*``` cherche la chaîne
``xeruti`` dans tous les fichiers du répertoire `aa/`. Chaque fois que
cette chaîne est trouvée, grep écrit le nom du fichier où il l'a
trouvé séparé par ':' de la ligne complète contenant la chaîne.

Mais grep est bien plus puissant que cela. Il permet de chercher non
seulement des mots, mais également des motifs avancés comme "un i
suivi d'un nombre pair de t (ou bien d'un nombre impair de s), mais
uniquement si c'est en début de ligne". En informatique, ces motifs
s'appellent des expressions régulières (*regular expression* ou *regex*
en anglais), et c'est d'ailleurs de là que vient le nom de grep:
*Global Regular Expression Print* (affichage d'expressions
régulières globales). 

La syntaxe des expressions régulières fleure bon les années 70 (en
informatique, cela veut dire que c'est affreusement préhistorique),
mais la puissance de la chose vaut bien la peine qu'on apprenne un peu
à s'en servir. En cas de problème, on trouve même des assistants à
l'écriture de regex sur internet.

Vous devez maintenant utiliser la commande grep pour trouver des
informations dans le répertoire de l'exercice. La page de manuel de
grep n'est pas très utile car elle n'est absolument pas pédagogique
(c'est un guide de référence), et elle ne donne même pas l'intégralité
de la syntaxe. Préférez la [page
wikipédia](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re#Utilisation).

### Chercher un mot

On trouve 243 fichiers aux noms parfaitement inintéressants dans le répertoire
``aa``. L'un d'entre eux contient la chaîne 'ici'. Utilisez grep pour trouver
lequel.

1. Quel est le mot étrange sur une ligne contenant 'ici' dans 'aa' ?
   
[Reponse1]:<>(grep ici aa/*)

### Limiter aux mots débutant la ligne

Cette fois, dans le répertoire ``bb``,
'ici' est dans deux fichiers et il faut sélectionner la
ligne où le motif est placé en début de ligne. Bien sûr, vous pouvez
grepper 'ici' sans spécifier et choisir à la main lequel des deux
recopier. Mais rien ne sert de tricher ici: ce n'est pas évalué. Il
vaut mieux chercher la regex magique sélectionnant directement la
bonne ligne (relisez wikipedia au besoin).

2. Quel est le mot étrange sur une ligne débutant par 'ici' dans 'bb' ?

[Reponse2]:<>(grep "^ici" /bb*)


### Ignorer la casse

Cette fois, dans le répertoire ``cc``,
on cherche "plutot" sans accent, mais on ne sait pas s'il
est écrit en majuscule ou minuscule. Il y a une option pour ignorer la
casse, comme indiqué sur la page man de grep (```man grep```)
ou dans le message d'aide du programme (```grep --help```).

3. Quel est le mot étrange sur une ligne contenant 'plutot' dans 'cc' ? 

[Reponse3]:<>(grep -i plutot cc/*)

### Répéter un motif

Comme indiqué sur wikipédia, on utilise des accolades pour indiquer
des répétitions de motif. Mais grep demande à ce qu'on écrive ``\{`` au
lieu de ``{``. À la fin, la regex pour attraper ``hiiiiiiiiii`` sera
``'hi\{10\}'``. N'oubliez pas les guillemets simples: ``hi\{10\}``
serait d'abord interprété par le shell qui passerait des choses
étranges à grep.

Là encore, il est plus facile de tricher que de trouver la bonne
regex. Soyez fort, persistez !

4. Quel est le mot sur une ligne contenant entre 3 et 7 'a' consécutifs dans 'dd' ?

[Reponse4]:<>(grep 'a\{3,7\}' dd/*)


### Classes de caractères

On cherche un mot contenant trois voyelles successives, suivies de
quelque chose qui n'est pas un chiffre. On est obligé de décrire les
voyelles en extension (il s'agit de l'une des lettres suivantes:
``aeoiu``), mais on peut décrire les chiffres en intension (un
caractère entre ``0`` et ``9``).

En grep, il faut bien écrire ``[`` et non ``\[``. Mais c'est toujours
une bonne idée de protéger ses expressions régulières du shell avec
des guillemets simples.

5. Quel est le mot sur une ligne contenant trois voyelles consécutives, non suivies d'un chiffre dans 'ee' ?

[Reponse5]:<>(grep '[aeiou]\{3\}[^0-9]' ee/*)

## 7. Enchaînements de commandes


Jusqu'à présent, nous avons utilisé le terminal pour lancer des
programmes les uns après les autres, mais ça n'allait pas très loin
car ces programmes étaient très simples. La puissance du shell ne
vient pas d'outils de plus en plus perfectionnés, mais plutôt de la
facilité avec laquelle on peut combiner des programmes simples pour
faire des outils parfaitement adaptés à la situation actuelle.

Le plus souvent, on ne fait même pas un script à proprement parler,
mais on combine plusieurs programmes sur la même ligne de commande. On
peut par exemple recompiler un programme, l'exécuter sur plusieurs
fichiers, vérifier que tout s'est bien passé puis effacer les fichiers
temporaires. Le tout en une seule commande, accessible simplement avec
flèche vers le haut. On trouve même
[ici](https://www.commandlinefu.com/) et
[là](http://www.bashoneliners.com/) des collections de ligne de
commandes shell d'une seule ligne (on appelle ça des *one-liners*).
Certaines sont pratiques, d'autres au mieux anecdotiques. Ces lignes
sont parfois très longues, et toutes sont difficiles à relire et à
comprendre. D'ailleurs, on n'apprend pas des *one-liners* par cœur, on
les reconstruit quand on en a besoin. Voyons maintenant comment faire.

### Combiner des programmes

Pour exécuter deux commandes à la suite, il suffit de les séparer par
``;`` ```touch temporaire; ls temporaire; rm temporaire```
va créer un fichier vide, afficher son nom puis le supprimer.

Parfois, on ne veut lancer la seconde commande que si la
première s'est bien passée. Pour cela, il faut écrire ``&&`` (lu "ET"
logique) entre les deux commandes. Comparez le résultat de
```ls OK && echo "le fichier existe"``` et celui de
```ls GaBuZoMeu && echo "le fichier existe"```, sachant
que le premier existe mais pas le second.

À l'inverse, on peut vouloir ne lancer la seconde commande que si la
première a échoué avec un OU logique. `#!bash ls OK || echo "PROBLÈME!"` ou
```ls GaBuZoMeu || echo "PROBLÈME!"```

On peut même grouper des commandes avec des parenthèses: l'ensemble
s'est bien passé si la dernière se passe bien.
```bash
(ls GaBuZoMeu;ls OK) && echo "le (dernier) fichier existe"
```

*Note pour les plus courageux:* les commandes entre parenthèses s'exécutent
dans un autre contexte, donc ```(cd /)``` ne change pas le
répertoire courant, seulement celui du contexte entre parenthèses.
Demandez à ``pwd`` (print working directory) ainsi si vous n'y croyez
pas: ```(cd / ; echo "changé:"; pwd) ; echo "pas changé:" ; pwd```

### Rediriger l'entrée et la sortie

Il est très facile de capturer les affichages d'un programme dans un
fichier. Par exemple ```date > sortie``` place
l'affichage de la commande à gauche du ``>`` dans un fichier nommé
``sortie`` (voir le contenu du fichier:  ```cat sortie```).
Le symbole ``>`` ne devrait pas se lire "plus grand" mais plutôt
"vers", comme une flèche: l'affichage du programme à gauche est
redirigé dans le fichier à droite.

Si on réexécute la première commande ```date > sortie```,
le contenu du fichier ``sortie`` est réécrit. On peut ajouter à la fin
du fichier au lieu de le remplacer de la façon suivante :
```date >> sortie```.


On peut également faire le contraire, et demander à un programme de
lire son entrée dans un fichier. Par exemple, ce répertoire compte un
petit script permettant de calculer la somme de deux nombres.
Essayez-le: ```./plus.sh``` (l'extension sh signifie qu'il
est écrit en shell). Au lieu de lire depuis le clavier, on peut faire
en sorte que ce script lise depuis un fichier.

```echo 4 6 > fichier``` permet de créer le fichier tandis
que ```./plus.sh < fichier``` lance le script en redirigeant
son entrée standard depuis le fichier.

On peut même rediriger à la fois l'entrée et la sortie d'un programme
de la façon suivante: ```./plus.sh < fichier > sortie```

Les redirections peuvent également être utilisée pour faire taire un
programme un peu trop bavard. Par exemple ```ls -lR /usr```
demande à afficher la liste de beaucoup des fichiers du disque.
C'est beaucoup, et vous voulez probablement faire ``Ctrl-C`` pour
l'interrompre avant la fin. Mais si vous faites
```ls -lR /usr > sortie```, vous ne voyez plus tout cet
affichage agaçant. Si vous voulez juste faire disparaître l'affichage
sans le sauvegarder sur disque, redirigez la sortie vers le fichier
``/dev/null`` qui est une sorte de trou noir où tout ce qui est écrit
est perdu.

Mais si vous faites ```ls GaBuZoMeu > /dev/null``` ou
```echo bla bla > fichier ; ./plus.sh < fichier```, vous
verrez quand même le message d'erreur s'afficher. Comment ce message
a-t-il réussi à s'échapper du trou noir ? C'est qu'en fait, tous les
programmes ont deux flux de sortie sur lesquels ils peuvent écrire: la
sortie standard (nommée ``stdout``) est celle par défaut. Le symbole
``>`` ne redirige que ``stdout`` sans toucher à la sortie d'erreur
(nommée ``stderr``), qui continue donc à atterrir sur l'écran.
Cela permet aux programmes d'indiquer leurs problèmes même quand on a
redirigé leur sortie standard. Si on le souhaite, on peut rediriger
``stderr`` avec ``2>`` : ```ls GaBuZoMeu 2> erreur```
(inspectez  le fichier produit: ```cat erreur``` ). On peut
enfin demander à rediriger ``stderr`` dans ``stdout`` avec ``2>&1`` (le
flux 2 -- stderr -- va dans le flux 1 -- stdout).

Et bien entendu, on peut rediriger l'entrée standard et les deux
sorties tout en combinant des séquences d'opérations. La ligne devient
un peu longue, mais ça ne pose pas de problème.
```ls GaBuZoMeu 2> /dev/null && echo "Le fichier existe" || echo "PROBLÈME!"```
```ls OK 2>&1 >/dev/null && (echo "Le fichier existe. Son contenu:"; cat < OK) || echo "PROBLÈME!"```

Oui, le résultat final n'est ni très lisible ni même très utile, mais
c'est un exemple de commande qu'on construit peu à peu lors d'une
session de travail, pour répondre à un besoin immédiat. Prenez
cependant le temps de comprendre ce qu'il contient et comment les
morceaux sont combinés.

### Tuber des programmes

Faire ```echo 4 > fichier; echo 6 >> fichier ; ./plus.sh < fichier``` devient
vite fastidieux, et en plus ça laisse un fichier sur disque. On peut
faire mieux en branchant directement la sortie d'un programme sur
l'entrée d'un autre, avec le symbole ``|``. On le lit "tube" ou "pipe"
en anglais, et on l'obtient sur un clavier français en faisant
``AltGr+6``.

L'exemple ci-dessus devient ```echo 4 6 | ./plus.sh```, tout
simplement. Et on peut enchaîner les commandes presque à l'infini:
Avec ```echo 4 6 | ./plus.sh | grep [0-9]```, le ``grep``
final filtre les lignes contenant au moins un chiffre, c'est-à-dire
celle de résultat.

**Attention!** ``|`` et ``>`` sont TRÈS différents. Le premier
redirige la sortie d'un programme dans un autre, tandis que le second
écrit dans un fichier. Exécuter ``echo 4 6 > ./plus.sh`` serait une
TRÈS mauvaise idée puisque ça écrirait ``4 6`` **à la place** du
script ``./plus.sh``. Avec ``|`` vous essayez de parler au programme à
droite. Avec ``>`` vous tentez de l'effacer en lui écrivant dessus...

### Ex 7.1

Le fichier ``animaux`` contient une liste d'animaux, mais avec des
doublons. On voudrait utiliser la commande ``uniq`` pour retirer les
lignes en doublon, puis écrire le résultat dans un fichier
``animaux.ok``. Mais malheureusement, ``uniq`` ne supprime que les
doublons que s'il s'agit de lignes consécutives dans le flux. Il
faudra donc utiliser la commande ``sort`` pour trier les animaux avant
de supprimer les doublons.

### Ex 7.2

On voudrait constituer un fichier nommé ``ligne33`` contenant exactement
la ligne 33 du fichier ``animaux.ok``.

*Indication:* vous aurez besoin des commandes ``head`` et ``tail``.
Quand on ne leur précise pas le fichier à lire, ces commandes lisent
leur entrée standard. Par défaut, ``head`` affiche les 10 premières
lignes de ce qu'il lit tandis que ``tail`` en affiche les 10 dernières
lignes. Regardez dans le manuel comment changer le nombre de lignes
affichées.

### Ex 7.3

Combien d'animaux de la liste de départ (pas animaux.ok) ont 3 voyelles successives dans leur nom?


*Indication:* utilisez ``grep``, ``uniq`` et ``sort``, ainsi que la
commande ``wc -l`` qui compte le nombre de lignes de son entrée
standard.


2. Que contient le fichier caché dans 'bbb'?

[reponse2]:<>(find bbb -type f)

