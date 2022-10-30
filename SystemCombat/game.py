import random

from SystemCombat.enemy import Enemy
from SystemCombat.hero import Hero

def afficheSituation():
    print("Deux ennemies apparaissent devant vous un ", enemy1.getName(), " ainsi qu'un ", enemy2.getName())
    print("╔═════════════════════════════════════════╦══════════════╦═══════════╦════════╦═══════╗")
    print("║ Le quel des deux voulez vous attaquez ? ║ Point de vie ║ Puissance ║ Statue ║ Choix ║")
    print("╠═════════════════════════════════════════╬══════════════╬═══════════╬════════╬═══════╣")
    if enemy1.getPV() < 10:
        print("║ Orc                                     ║       ", enemy1.getPV(), "    ║    ", enemy1.getDamage(),"   ║", enemy1.getStatue(), "║   Q   ║")
    elif enemy1.getPV() < 100:
        print("║ Orc                                     ║      ", enemy1.getPV(), "    ║    ", enemy1.getDamage(),"   ║", enemy1.getStatue(), "║   Q   ║")
    else:
        print("║ Orc                                     ║     ", enemy1.getPV(), "    ║    ", enemy1.getDamage(),"   ║", enemy1.getStatue(), "║   Q   ║")
    print("╠═════════════════════════════════════════╬══════════════╬═══════════╬════════╬═══════╣")
    if enemy2.getPV() < 10:
        print("║ Goblin                                  ║       ", enemy2.getPV(), "    ║    ", enemy2.getDamage(), "   ║",enemy2.getStatue(), "║   E   ║")
    elif enemy2.getPV() < 100:
        print("║ Goblin                                  ║      ", enemy2.getPV(), "    ║    ", enemy2.getDamage(), "   ║",enemy2.getStatue(), "║   E   ║")
    else:
        print("║ Goblin                                  ║     ", enemy2.getPV(), "    ║    ", enemy2.getDamage(), "   ║",enemy2.getStatue(), "║   E   ║")
    print("╚═════════════════════════════════════════╩══════════════╩═══════════╩════════╩═══════╝")

def afficheAttaque():
    print("╔═══════════════════════════════════════╦═════════╦════════╗")
    print("║ Quelle attaque vous voulez utiliser ? ║ Basique ║ Ultime ║")
    print("╠═══════════════════════════════════════╬═════════╬════════╣")
    print("║                                       ║ A       ║ D      ║")
    print("╚═══════════════════════════════════════╩═════════╩════════╝")

enemy1 = Enemy("Orc", 150, 30)
enemy2 = Enemy("Goblin", 75, 15)
listEnemy = [enemy1.getName(), enemy2.getName()]
hero = Hero("Bob", 100, 25)

isVictory = False
isGameOver = False

# print("╔═══════════════════════════════════╗")
# print("║ Entrer le nom de votre personnage ║")
# print("╚═══════════════════════════════════╝")
# userName = input()


while (not isVictory) or (not isGameOver):
    if hero.getPV() <= 0:
        isGameOver = True
        print("╔═══════════════════════════════════╗")
        print("║             GAME OVER             ║")
        print("╚═══════════════════════════════════╝")
        break
    elif enemy1.getPV() <= 0 and enemy2.getPV() <= 0:
        isVictory = True
        print("╔═══════════════════════════════════╗")
        print("║             VICTOIRE              ║")
        print("╚═══════════════════════════════════╝")
        break
    else:
        afficheSituation()
        choixEnemy = input()
        if choixEnemy.lower() == "q":
            afficheAttaque()
            choixAttack = input()
            hero.attack(enemy1, choixAttack)

        elif choixEnemy.lower() == "e":
            afficheAttaque()
            choixAttack = input()
            hero.attack(enemy2, choixAttack)

        if enemy1.getPV() <= 0:
            listEnemy = [enemy2.getName()]
        if enemy2.getPV() <= 0:
            listEnemy = [enemy1.getName()]

        choixEnemyAttack = random.choice(listEnemy)
        print(choixEnemyAttack, " vous attaque !")
        if choixEnemyAttack == "Orc":
            choixAttack = random.randint(0, 1)
            enemy1.attack(hero, choixAttack)
        elif choixEnemyAttack == "Goblin":
            hoixAttack = random.randint(0, 1)
            enemy2.attack(hero, choixAttack)
        print("Vos point de vie(s) : ", hero.nbrPV)