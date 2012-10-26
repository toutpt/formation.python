Debugger son code
=================

Débugger son code, c'est l'art de comprendre les erreurs et de les corriger.

Les erreurs (Exception)
-----------------------

Il existe différents types d'erreurs qui donnent des indications sur le problème
qu'à rencontré l'interpreteur Python lors de l'execution:

* ValueError
* TypeError
* IOError
* SyntaxError
* AttributeError

Lorsque Python rencontre une erreur il soulève cette erreur sous forme d'exception
qui se présente de la manière suivante::

  >>> class Contact
    File "<stdin>", line 1
      class Contact
                  ^
  SyntaxError: invalid syntax

Les informations que vous avez dans une trace python:

* l'ensemble des fichiers parcourus durant l'execution
* les appelles des méthodes qui se sont enchainés
* la ligne à laquelle l'erreur ou l'appel a eu lieu dans le fichier
* le type d'erreur rencontré
* une message censé donné une information supplémentaire sur l'erreur

Avec tout ça vous devez pouvoir comprendre rapidement ce qui se passe.
Ici l'erreur est une erreur de syntaxe. 
En effet nous n'avons pas mis ':' juste après la définition de la classe 'Contact'.

Donc un conseil, regardé d'abord le type de l'erreur affichée
dans la console ou dans les log.

La gestion des exceptions
-------------------------

Avec Python vous pouvez gérer les exceptions avec la syntaxe suivante::

  try:
      mon_objet.ma_methode(argument)
  except ValueError, message:
      print "une erreur correspondant à la valeur de "argument" est survenu."

Donc ce code, en cas d'une erreur sur l'argument va se contenter de faire un print.
ce qui signifie que la méthode / fonction appelant ce code ne laissera aucune
trace au appelant suppérieur. On parle de "chaine de responsabilité". 

Il faut donc répondre à la question: "Qui gère les problèmes et comment ?".
On s'accorde sur ce point à dire qu'il faut que l'erreur puisse parler à l'utilisateur
et donc que l'erreur doit être géré le plus haut possible ?

Cas d'utilisation: L'entrée utilisateur pour le numéro de téléphone est une 
chaine de caractère, seulement notre interface utilisateur à transformer cette
valeur en un entier. Que se passe t'il dans la suite ? Au moment de l'enregistrement,
nous risquons quelques erreurs.