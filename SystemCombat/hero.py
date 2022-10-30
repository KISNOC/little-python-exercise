import random

from SystemCombat.personnage import Personnage

class Hero(Personnage):
    def attack(self, enemy, attackChoice):
        if attackChoice.lower() == "a":
            enemy.nbrPV -= self.damage

        elif attackChoice.lower() == "d":
            luck = random.randint(0,1)
            if luck == 1:
                enemy.nbrPV -= (self.damage * 2)
                print("Attaque réussi")
            else:
                print("Attaque échouer")