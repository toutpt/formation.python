Programmation Orienté Objet
===========================

Vocabulaire
-----------

* classe
* attribut
* méthode
* comportement
* responsabilité

Introduction
------------

L'objet a été créé dans le but d'aider les développeurs à organiser leur code,
à le réutiliser, à pouvoir étendre les possibilités sans tout re-écrire.

Le principe d'un développement orienté objet est de modéliser l'environnement
manipulé par l'application ("un carnet d'adresse contient des contacts").

Les phases d'un développement d'une application:

* Modélisation
* Prototypage
* Tests
* Implémentation
* Itération sur les deux précédentes -> Livraison
* Recette (validation de l'application)

Application carnet d'adresses
-----------------------------

Dans le cadre de la réalisation d'une application nous devons donc ici modéliser
les éléments qui seront manipulé dans notre application.

Un Contact, c'est avant tout un nom et un prénom.
Une classe Contact se définit donc avec les attributs 'nom' et 'prénom'.
Mais nous aurons besoin également de pouvoir ajouter plusieurs 'numéro de téléphone'

::

    class Contact(object):
        """Documentation du contact"""
        def __init__(self, nom, prenom):
            self.nom = nom
            self.prenom = prenom
            self.tel = []

Ici nous avons créé la classe 'Contact' qui nécessite pour sa construction
un nom et un prénom. la valeur du téléphone devra être précisée après
la construction.

Quelques phrases qui se disent entre développeurs:

* '__init__' est le constructeur de la classe Contact
* le 'nom' self.nom est un attribut de la classe Contact

Il est donc maintenant possible de manipuler notre contact::

    >>> c1 = Contact("François", "Jean-Michel")
    >>> c1.tel.append("00 00 00 00 00")
    >>> print c1.nom
    "François"
