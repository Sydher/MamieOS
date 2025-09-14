# Ordinateur et OS | MamieOS

## L'ordinateur

Je suis partie sur un nouvel ordinateur car l'actuel était vraiment vieux et fatigué, de plus il me fallait du temps pour réaliser la nouvelle configuration et je n'habite pas dans la même ville que ma grand mère.

Les conditions de choix du PC était les suivantes :
* Mini PC pour ne pas prendre trop de place sur son bureau
* Couleur claire, elle n’apprécie pas les boitiers noirs car ils prennent trop la poussière
* Nouvel écran (car sont ancien était un PC intégré à l’écran, donc non réutilisable)
* Pas d’accessoires supplémentaires
    * Pas d'enceintes, le son de l'écran suffit pour ce qu'elle fait
    * Pas de claviers / souris, les actuels suffisent
* Un PC plutôt puissant, elle n'a effectivement pas besoin d'une machine de guerre pour son utilisation très basique mais :
    * Je souhaite que ce PC dure longtemps
    * Moins puissant est trop souvent égale à moins de qualité
    * Le PC pourra être réutilisé dans un autre contexte plus tard
    * Le respect de toutes les autres conditions limite les choix possibles

Mon choix c'est donc porté sur :
* PC [Geekom A8](https://amzn.eu/d/57b58WE) à 799€
* Ecran [Philips 241V8AW](https://amzn.eu/d/bOZZYxW) à 86,72€

## Le système d'exploitation (OS)

### Choix de l'OS

Déjà, pas de Windows.  
Le système change trop souvent, chaque nouvelle version ajoute des complexités inutiles, ce qui n’est pas adapté aux personnes âgées ou à celles qui veulent de la stabilité.  
Depuis Windows 10 *(et encore plus Windows 11)*, le système est devenu intrusif : collecte de données, publicités intégrées, mises à jour forcées...  
À cela s’ajoute une plus grande exposition aux virus, moins de possibilités de personnalisation et de configuration fine.

Mon choix s’est donc naturellement tourné vers Linux.  
Après quelques recherches et tests (Ubuntu, Mint), j’ai choisi **Zorin OS**.

Pourquoi Zorin OS ?  
* Interface familière : possibilité de choisir une apparence proche des anciens Windows, ce qui facilite la transition et ne perturbe pas les habitudes.
* Pensé pour débutants : installation simple, ergonomie claire, logiciels essentiels déjà préinstallés. Cela facilitera grandement mon travail.
* Performances : fluide même sur du matériel ancien, optimisé pour prolonger la vie des ordinateurs *(pas forcément utile dans mon cas, mais le sera pour d'autres cas d'usages)*.
* Stabilité : basé sur Ubuntu LTS, avec des mises à jour fiables et une maintenance de long terme.
* Compatibilité logicielle : prise en charge facile de nombreux logiciels, possibilité d’utiliser Wine pour exécuter certaines applications Windows (au besoin).
* Vie privée respectée : aucune collecte de données intrusive par défaut.
* Développé en Europe : créé par une entreprise irlandaise, Zorin OS est soumis aux réglementations européennes plus strictes en matière de protection des données et de respect de la vie privée.

En résumé, Zorin OS combine la stabilité de Linux, la simplicité d’Ubuntu, et une interface rassurante pour les nouveaux venus. C’est un excellent compromis entre liberté, sécurité et facilité d’utilisation.

### Configuration de l'OS

L'installation dans un premier temps est très simple, il suffit de suivre le guide sur le [site officiel](https://help.zorin.com/docs/getting-started/install-zorin-os/).  
Il faut avoir un ordinateur et une clé USB de 4GO minimum.

Une fois installé, la configuration est assez simple (menus clairs), je ne la détaillerais pas ici.

Je recommande toutefois plusieurs configurations :
* Création de 2 utilisateurs :
    * 1 admin pour vous
    * 1 utilisateur normal (restreint) pour la personne agée qui va l'utiliser.

*Cela permettra de fortement limité les actions de l'utilisateur et donc d'éviter des bétises (toucher à quelque chose qu'il ne fallait pas des les paramètres avancés) ou des failles de sécurité (installation de logiciels malveillants).*
* Sur la session de l'utilisateur cible, masquer les raccourcis vers les paramètres dans le menu démarrer
TODO image
* Augmenter la taille de la police et des icones du bureau
TODO image

## La suite

Voir [2 - Navigateur](../2%20-%20Navigateur/README.md)
