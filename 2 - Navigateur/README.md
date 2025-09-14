# Navigateur | MamieOS

## Firefox

Zorin OS ets livré avec Brave de préinstallé. Je l'ai supprimé au profit de **Firefox**.  
J'ai choisi Firefox pour les raisons suivantes :
* Habitudes : elle l'utilise déjà sur son PC actuel
* Respect de la vie privée : développé par la fondation Mozilla, organisme à but non lucratif, sans modèle économique basé sur la revente de données. Attention nécéssite certaines configurations pour être vraiment respectueux !
* Open source : code transparent, auditable, et soutenu par une large communauté.
* Extensions puissantes : grande liberté de personnalisation avec un écosystème d’extensions riche.
* Performances : moteur moderne (Gecko/Quantum) rapide et optimisé pour limiter la consommation mémoire *(n'est-ce pas Chrome !)*.
* Engagement éthique : soutien de standards web ouverts, lutte contre le monopole des navigateurs dominants.

### Installation

Ne pas installer via le store car flatpack ne permet pas de configurer les politiques de configuration (voir plus bas).

```shell
sudo apt update
sudo apt install firefox
```

### Configuration

* Page d'accueil Firefox
  * Désactiver les articles recommandés & sponsorisés
* Recherche
  * Sélectionner DuckDuckGo (voir prochain paragraphe pour plus d'infos)
  * Désactiver les suggestions de recherches
  * Désactiver les autres moteurs de recherche dans Reccourcis de recherche
* Vie privée
  * Désactiver les remplissages automatique (alternative décrite dans le paragraphe des extentions)
  * Désactivation de toutes les télémétries (sauf le ping à Mozilla)

### Moteur de recherche

Exit Google, bievenue **DuckDuckGO**.  
* Respect de la vie privée : ne collecte ni ne revend d’historique de recherche.
* Pas de traçage publicitaire : résultats sans profilage ni ciblage intrusif.
* Interface simple : proche de Google, donc facile à prendre en main.
* Résultats clairs : mélange de sources (Bing, Wikipédia, etc.) sans sur-optimisation publicitaire.
* Fonctionnalités pratiques : commandes rapides (bangs !w, !yt, etc.) pour accéder directement à d’autres sites. *(Pour info car ne sera surement pas utilisé par une personne agé)*
* Entreprise indépendante : basée aux États-Unis mais engagée publiquement contre la surveillance de masse.

Je ne détail pas, mais un passage dans les paramètres de DuckDuckGo est nécéssaire (désactiver pubs, désactiver fonctionnalité IA, ...).

### Extensions

* uBlock Origin : Supprime les pubs et les trackers.

Web plus agréable, meilleur respect vie privée et améliore la sécurité.
* I dont care about cookies : Refuse automatiquement les cookies non nécéssaires et à défaut accepte automatiquement si refus impossible

Web plus agréable et meilleur respect vie privée.
* BitWarden : Gestionnaire de mot de passe.

La saisie de mot de passe est assez compliqué pour ma grand-mère. Avoir une extention qui se souviens et saisie automatiquement ses mots de passes facilitera énormément son utilisation.  
De plus **tout le monde** devrait utiliser un gestionnaire de mot de passe !

### Configuration avancées

Une fois tout configuré et afin d'éviter d'eventuelles modifications (malicieuses ou accidentelles) j'ai ajouté une politique stricte afin d'empêcher de nombreuses fonctionnalités.

Jouer les commandes suivantes :
```shell
su - admin      # ou le nom de votre compte admin
cd /usr/lib/firefox/distribution
sudo nano policies.json
```

Et mettre le contenu de mon [policies.json](./policies.json).

## La suite

Voir [3 - Mails](../3%20-%20Mails/README.md)
