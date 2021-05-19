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

    Une *paire (sous-réseau/masque)* est composée
    
    - de l'adresse IP du réseau, notée sur 4 octets, soit 32 bits;
    - du nombres de bits qui correspondent à la partie fixe des IP du réseau.
    
    Par exemple, le réseau local du client est 192.168.1.0/24 ce qui veut dire que :
    
    - l'adresse IP du réseau est 192.168.1.0;
    - les 24 bits (dans le sens de la lecture) sont fixes.
    
    Puisque qu'une adresse IP est codée sur 32 octets, cela veut dire que seuls les 8 derniers bits (c'est-à-dire le 
    dernier octet) peuvent varier. L'ensemble des IP de ce réseau est donc 
    - 192.168.1.0 : l'IP du réseau même;
    - 192.168.1.x : l'IP des machines du réseaux, avec $1\leqslant x\leqslant 254$ (soit 254 machines au total;
    - 192.168.1.255 : l'IP du réseau dédiée à la diffusion en masse (*broadcast*).
 
 Le réseau comprenant R1 et R3 a pour adresse 10.0.1.0/30 : il ne reste donc que 2 bits libres pour adresser les machines.
 Si on enlève l'adresse réseau 10.0.1.0 et l'adresse *broadcast* 10.0.1.3 il reste 2 IP, une pour chaque routeur.
 Ajoutons que R1 possède aussi une IP dans le réseau local du client et réalise ainsi une *passerelle*.
 
 Ainsi par exemple Dans ce réseau R1 peut avoir l'IP 10.0.1.1 et R3 10.0.1.2 (ou l'inverse).
 
 Lorsqu'un paquet doit transiter du client au serveur, il doit obligatoirement passer la passerelle R1 et là encore il
 n'y a pas le choix, il passera par R3.
 
 Mais ensuite ? Comment la route à emprunter est-elle déterminée ? Est-ce la même tout le temps ?
 
 En fait, chaque routeur possède une *table de routage* qui associe les IP de destination à des routeurs particuliers.
 Ces tables ne sont pas fixes et *a priori* tous les routeurs ont le même statut (il n'y a pas de routeur privilégié).
 
 Les méthodes qui permettent de gérer ces tables de routage sont appelés des *protocoles de routage*.
 
## Le protocole RIP
 
!!! note "Principe"

    À intervalles de temps régulieur, chaque routeur envoie à ses voisins 
    
    - les adresses de ses propres voisins;
    - les adresses qu'il a reçues par d'autres routeurs
    
    Pour chaque adresse, il indique également combien de sauts sont nécessaires pour l'atteindre, c'est à dire par combien
    de routeurs (y compris lui-même) il faut passer.
    
    Lorsqu'un routeur reçoit les informations d'un routeur voisin, 4 cas peuvent survenir :
    
    1. dodod
    2. erofi
    3. zefiezio
    4. eoiefoi


Et voilà !

 
|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|


|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth1    	| 1        	|
|   10.0.2.0/30     |            	|    eth3    	| 1        	|
|   10.0.3.0/30     |            	|    eth1    	| 1        	|
|   10.0.4.0/30     |            	|    eth0    	| 1        	|

---

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|
|   10.0.2.0/30     |    10.0.1.2       	|    eth0  	| 2        	|
|   10.0.3.0/30     |    10.0.1.2        	|    eth0    	| 2        	|
|   10.0.4.0/30     |    10.0.1.2        	|    eth0    	| 2        	|

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth1    	| 1        	|
|   10.0.2.0/30     |            	|    eth3    	| 1        	|
|   10.0.3.0/30     |            	|    eth1    	| 1        	|
|   10.0.4.0/30     |            	|    eth0    	| 1        	|
|   10.0.7.0/30     |  10.0.4.2     |    eth0    	| 2       	|

---


|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|
|   10.0.2.0/30     |    10.0.1.2       	|    eth0  	| 2        	|
|   10.0.3.0/30     |    10.0.1.2        	|    eth0    	| 2        	|
|   10.0.4.0/30     |    10.0.1.2        	|    eth0    	| 2        	|



|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth1    	| 1        	|
|   10.0.2.0/30     |            	|    eth3    	| 1        	|
|   10.0.3.0/30     |            	|    eth1    	| 1        	|
|   10.0.4.0/30     |            	|    eth0    	| 1        	|
|   10.0.7.0/30     |  10.0.4.2     |    eth0    	| 2       	|


## Le protocole OSPF
 