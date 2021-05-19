# Protocoles de routages

## Situation

Lors d'une communication *via* un réseau, une machine appelée *client* doit envoyer une information à une autre machine 
appelée *serveur*. Les termes client et serveur sont très larges et peuvent en fait

- désigner une machine aussi bien qu'une *application* s'exécutant sur cette machine;
- alterner au cours du temps (le client devient serveur et vice-versa).

On a [vu en classe de première](../../../../nsi1/ch18/reseaux/#un-modele-informatique-tcpip) que l'information va être découpée en de multiples paquets de petite taille, et ces paquets doivent arriver à destination.

Le troisième élément de la communication sont les [routeurs](../../../../nsi1/ch18/reseaux/#couche-reseau). Ils peuvent
être de deux types

- *routeurs d'accès* lorsqu'ils sont en *bordure de réseau*, c'est à dire qu'ils sont directement interfacés avec un réseau 
  *local*.
  
- *internes* sinon.

Voici un schéma qui montre la *topologie* d'un réseau, c'est à dire son architecture :

![topo1](../img/topo1.svg){width=75%}


!!! note "Explications sur les paires (sous-réseau/masque)"

    