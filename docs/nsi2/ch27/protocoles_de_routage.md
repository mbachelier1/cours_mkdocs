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

![topo1](../img/topo1.svg){width=100%}


??? note "Explications sur les paires (sous-réseau/masque)"

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
 
 Le réseau comprenant R1 et R3 a pour adresse 10.0.1.0/30 : il ne reste donc que 2 bits libres pour adresser les 
 machines, soit 4 possibilités.

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
 
??? note "Principe"

    À intervalles de temps régulieur, chaque routeur envoie à ses voisins 
    
    - les adresses de ses propres voisins;
    - les adresses qu'il a reçues par d'autres routeurs
    
    Pour chaque adresse, il indique également combien de sauts sont nécessaires pour l'atteindre, c'est à dire par combien
    de routeurs (y compris lui-même) il faut passer.
    
    Lorsqu'un routeur reçoit les informations d'un routeur voisin, 4 cas peuvent survenir :
    
    1. Une route vers un nouveau sous-réseau lui est présentée : il l'ajoute à sa table de routage.
    2. Une route vers un sous-réseau déjà connue lui est présentée, mais plus courte que la précédente. Dans
        ce cas l'ancienne est remplacée par celle-ci.
    3. Une nouvelle route plus longue lui est transmise : il l'ignore. 
    4. Une route existante, passant par le même voisin, mais plus longue que celle de la table de routage lui est
        présentée. Cela veut dire qu'un problème est survenu sur l'ancienne route. Celle-ci est donc effacée et remplacée 
        par la plus longue.


Pour éviter les boucles, les distances doivent être au maximum de 15 (sinon elles sont ignorées). 
RIP fonctionne donc sur des réseaux de taille modeste.

### Étape 1 : initialisation

Reprenons le réseau précédent et intéressons-nous uniquement aux routeurs R1 et R3.

Au début de la mise en service du réseau voici la table de routage de R1 :
 
|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|

Elle indique que le sous-réseau local 192.168.1.0/24 est immédiatement accessible *via* l'interface *WiFi* wlan0 depuis
ce propre routeur R1. Elle est donc à distance 1 de R1. De même l'autre sous-réseau est accessible *via* un port *Ethernet*
du routeur nommé eth0 et est également à distance 1 de R1.

Voici celle de R3 :

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.1.1.0/30     |            	|    eth1    	| 1        	|
|   10.1.2.0/30     |            	|    eth2    	| 1        	|
|   10.1.3.0/30     |            	|    eth3    	| 1        	|
|   10.1.4.0/30     |            	|    eth0    	| 1        	|

C'est la même chose : R3 est initialisé avec ses voisins directs. Notez que les noms des interfaces sont relatifs à R3, 
c'est pourquoi, par exemple, R1 et R3 sont reliés par *Ethernet* sur le port eth0 de R1 et eth1 de R2. Ces ports peuvent
avoir le même nom ou pas, peu importe car ces noms n'existent que relativement au routeur concerné.

### Étape 2 : première itération de RIP

Chaque routeur envoie ses informations à ses voisins. La table de R1 devient

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|
|   10.0.2.0/30     |    10.1.1.2       	|    eth0  	| 2        	|
|   10.0.3.0/30     |    10.1.1.2        	|    eth0    	| 2        	|
|   10.0.4.0/30     |    10.1.1.2        	|    eth0    	| 2        	|

Ainsi R1 sait qu'il peut atteindre les machines du sous-réseau 10.1.2.0/30 *via* la passerelle 10.1.1.2 (IP de R2) sur
le sous-réseau 10.1.1.0/30 sur lequel R1 et R2 figurent. L'interface est eth0 et la distance est 2.


Voici la table de R3 :

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.1.1.0/30     |            	|    eth1    	| 1        	|
|   192.168.1.0/24  |  10.1.1.1     |    eth1    	| 2       	|
|   10.1.2.0/30     |            	|    eth2    	| 1        	|
|   10.1.3.0/30     |            	|    eth3    	| 1        	|
|   10.1.4.0/30     |            	|    eth0    	| 1        	|
|   10.1.7.0/30     |  10.1.4.2     |    eth0    	| 2       	|

    
### Étape 3 : convergence après quelques itérations

Dans notre cas, après 2 autres itérations, les informations se stabilisent, on dit qu'il y a *convergence* et chaque 
routeur connaît le chemin à emprunter pour accéder à n'importe quel sous-réseau.

En particulier la table de R1 est la suivante :

|   destination  	| passerelle 	| interface 	| distance 	|
|:--------------:	|:----------:	|:---------:	|:----------:	|
|   10.0.1.0/30     |            	|    eth0   	| 1        	|
| 192.168.1.0/24 	|            	| wlan0     	| 1        	|
|   10.0.2.0/30     |    10.1.1.2       	|    eth0  	| 2        	|
|   10.0.3.0/30     |    10.1.1.2        	|    eth0    	| 2        	|
|   10.0.7.0/30     |    10.1.1.2        	|    eth0    	| 3        	|
|   192.162.6.0/30     |    10.1.1.2        	|    eth0    	| 4        	|


## Le protocole OSPF

à venir
 