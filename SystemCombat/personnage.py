from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self, name, nbrPV, damage):
        self.name = name
        self.nbrPV = nbrPV
        self.nbrTotalPV = nbrPV
        self.damage = damage

    @abstractmethod
    def attack(self, nameEnemy, attackChoice):
        pass

    def getName(self):
        return self.name

    def getPV(self):
        return self.nbrPV

    def getDamage(self):
        return self.damage

    def getStatue(self):
        if self.nbrPV >= 1:
            return "Vivant"
        else:
            return " Mort "