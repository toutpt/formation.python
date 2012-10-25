Packaging
=========

Vocabulaire
-----------

* egg
* module
* buildout
* virtualenv
* distutils
* pypi


Principe
--------

Développer c'est bien, savoir installer c'est mieux. Nous allons ici
parler de packaging pour faciliter le déploiement de nos développements.

Le contenu d'un package python:

* un setup.py (description du package, technologie 'distutils_ + setuptools_')

Réalisation d'un package
------------------------

C'est avec l'outil PasteScript_ (script 'paster') que nous allons pouvoir
réaliser un package rapidement. Son utilisation se résume à::

    paster create monprojet

Vous pouvez demander la traduction de la documentation à Google:
http://goo.gl/6jmf9

Le principe est simple, la commande paster prend un 'template' en paramètre.
Ce template correspond à l'arborescence qui sera générée. Vous pouvez également
installer des modules qui propose de nouveau squelette ou encore les créer
vous même.

Par défaut paster propose un template qui permet de créer un package
'setuptools enabled' c'est à dire qui utilise setuptools pour l'installation.

Installation d'un package
-------------------------

Pour installer un package on a pas mal de choix. Il faut d'abord répondre 
à question suivante: "Ou installer mon package"

* dans mon système (nécessite donc les droits administrateur)
* dans mon projet (sans les droits administrateur)
* sur mon serveur (avec mon administrateur)

Au sens distuils, installer un package python c'est faire::

    wget http://example.com/monpackage
    cd monpackage
    python setup.py install

Au sens setuptools, installer un package python c'est faire::

    easy_install monpackage

Le problème de cette approche est qu'elle installe le package dans le python
qui execute la commande, donc par défaut sur le système.

Inconvénient:

* impossible d'installer deux versions différentes du même package
* nécessite les droits administrateur
* impossible de développer / modifier le package

Il y a deux alternatives pour éviter ça:

* virtualenv_
* zc.buildout_

zc.buildout
-----------

Buildout est un excellent outil qui permet de déployer des applications python
simplement. Il suffit de disposer de deux fichiers pour bénéficier de buildout:

* un fichier bootstrap.py http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py
* un fichier buildout.cfg (qui décrit la configuration du projet)

Dans l'execution::

    python bootstrap.py
    bin/buildout

Plus d'information sur la documentation suivante:
http://plone.fr/documentation/documentation-integrateur/presentation_buildout.html

.. _PasteScript: http://pythonpaste.org/script/
.. _distutils: http://docs.python.org/distutils/index.html
.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _distribute: http://packages.python.org/distribute/setuptools.html
