#-*- coding: utf-8 -*-

class Voiture(object):
    """Cette CLASSE définie une voiture."""
    
    def __init__(self):
        """ceci est le CONSTRUCTEUR de ma classe voiture"""
        self.roues = 4
        self.couleur = None
        self.marque = None
        self.plaque = None
        self.moteur = Moteur()
        self.cle = None
        self.puissance = puissance

    def demarrer(self, cle):
        """demarrer la voiture, si c'est la bonne cle"""
        if cle == self.cle:
            self.moteur.demarrer()

    def arreter(self):
        """arrete la voiture, coupe le moteur, ..."""
        pass

    def accelerer(self, nb):
        """augmente la vitesse du moteur"""
        pass

    def freiner(self, nb):
        """freine les roues de la voiture"""
        pass

    def changer_vitesse(self, vitesse):
        """change la vitesse de la boite de vitesse"""
        pass


class Remorque(object):
    def __init__(self):
        pass

    def freiner(self, nb):
        """freine les roues de la remorque"""
        pass

    def charger(self, chargement):
        pass

class Camion(Voiture):#, Remorque):
    def __init__(self):
        Voiture.__init__(self)
#        Remorque.__init__(self)
        self.remorque = Remorque()

    def freiner(self, nb):
        Voiture.freiner(self, nb)
#        Remorque.freiner(self, nb)
        self.remorque.freiner(nb)


class Moteur(object):
    def __init__(self):
        self.puissance = 200
        self.consomation = 5
        self.demarre = False

    def demarrer(self):
        """lance le démarreur electrique"""
        self.demarre = True

    def arreter(self):
        self.demarre = False

    def is_demarre(self):
        """ -> True si le moteur est demarré"""
        return self.demarre

if __name__ == '__main__':
    c3 = Voiture()
    c3.marque = "citroen"
    c3.puissance = 80
    c3.cle = "à2('àçé'é'(é'())"
    c3.demarrer("test")
    if c3.moteur.demarre:
        print "c est la bonne cle" 