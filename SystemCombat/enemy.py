import random

from SystemCombat.personnage import Personnage

class Enemy(Personnage):
    def caclulPourcentage(self, totalPV, actuelPV):
        pourcentagePV = (100*actuelPV)/totalPV
        return pourcentagePV

    def attack(self, enemy, attackChoice):
        ##choixAttack = random.randint(0,1)
        if attackChoice == 0:
            print("Attaque basique de l'enemie")
            enemy.nbrPV -= self.damage
        else:
            if self.caclulPourcentage(self.nbrTotalPV , self.getPV()) < 50:
                enemy.nbrPV -= (self.damage*2)
                print("Attaque spécial réussi x2")
            elif self.caclulPourcentage(self.nbrTotalPV , self.getPV()) < 25:
                enemy.nbrPV -= (self.damage * 3)
                print("Attaque spécial réussi x3")
            else:
                print("Attaque spécial échouer")