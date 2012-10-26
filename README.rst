Formation Python
================

Ce package contient une série d'exemples de code, ainsi que de la documentation
autour de python.

Comment installer ce package::

    python bootstrap.py
    bin/buildout

Comment executer les tests du package::

    bin/tests

Nous prenons dans tous nos exemples la notion de carnet d'adresses comme besoin.

Pour reconstuire la documentation:

    sphinx-build -b html -d docs/build/doctrees   docs/source docs/build/html
