## Un exemple bien connu

Nous commençons à bien connaître la suite de Fibonacci


$$F_n=\begin{cases}1 & \mbox{si } n=0\mbox{ ou }n=1\\ F_{n-1}+F_{n-2} &\mbox{sinon}\end{cases}$$

Si on la programme *naïvement* de manière récursive, voici ce qu'on obtient :

{{py("fibo_naif")}}

Or, voici l'arbre des appels récursifs lors de l'exécution de `fibo(4)` :

![fibo_4](../img/fibo_4.svg){width=75%}

Et pour `fibo(5)` on obtient :

![fibo_5](../img/fibo_5.svg){width=75%}

Lors de cet appel, `fibo(3)` est appelée 2 fois, `fibo(2)` 3 fois, `fibo(1)` 5 fois et `fibo(0)` 3 fois !

Il n'est donc pas étonnant que `fibo(40)` prenne quelques secondes. Quant à `fibo(100)`, ce n'est même pas la peine d'y 
penser !

Notre stratégie, de type « diviser pour régner », décompose le calcul de `fibo(n)` en 2 calculs plus simples, mais *ces
problèmes ne sont pas indépendants* , comme l'illustre le graphe suivant, obtenu à partir du schéma précédent.

![fibo_5](../img/fibo_5_graphe.svg){width=40%}

## La mémoïsation 

!!! info "Définition : mémoïsation"
    
    C'est le fait de garder en mémoire les solutions des sous-problèmes pour pouvoir les réutiliser sans avoir à les 
    déterminer de nouveau.
    
    Cela veut dire qu'avant de renvoyer un résultat, la fonction le stocke (dans une liste ou un dictionnaire). 

Ce qui est fort agréable, c'est que les listes et les dictionnaires sont de *type mutable*, ce qui nous permet d'écrire ceci :

{{py("fibo_dyn")}}

Et là, on peut calculer rapidement que $F_{40}=165\,580\,141$, et même que

$\scriptsize F_{500}=225\,591\,516\,161\,936\,330\,872\,512\,695\,036\,072\,072\,046\,011\,324\,913\,758\,190\,588\,638\,866\,418\,474\,627\,738\,686\,883\,405\,015\,987\,052\,796\,968\,498\,626$
    
Le fait d'utiliser la mémoïsation rend les choses bien plus rapides !

!!! note "Exercice : programmation dynamique de la  suite de Fibonacci"

    En s'inspirant du script précédent, écrire la fonction `fibo_dyn2` qui mémoïse les solutions à l'aide d'un
    dictionnaire (vide au départ).

??? note "Solution"

    {{py_admo("fibo_dict")}}

!!! danger "Comparaison de l'efficacité des 2 méthodes"

    [L'activité est à faire ici](https://capytale2.ac-paris.fr/web/c-auth/list?returnto=/web/code/89a4-17353).


