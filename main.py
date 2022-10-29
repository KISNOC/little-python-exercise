import random

print("Devinez le juste prix ! Le prix est compris entre 0 et 10 inclus.")

secretNumber = random.randint(0, 10)
userNumber = -1
trials = 0

while (True):
    try:
        userNumber = input()
        userNumber = int(userNumber)
        trials+=1
        if userNumber < secretNumber:
            print("Le juste prix est plus haut")
        if userNumber > secretNumber:
            print("Le juste prix est plus bas")
        if userNumber == secretNumber:
            print("Félicitations, vous avez trouvé le juste prix ", secretNumber, " en ", trials, " essais !")
            print("Partie terminée")
            break
    except ValueError:
        print("Entrer un nombre entier !")
