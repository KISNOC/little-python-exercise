import random


def numbers_to_strings(argument):
    switcher = {
        0: "Pierre",
        1: "Papier",
        2: "Ciseaux",
    }
    return switcher.get(argument, "Entrer un nombre entre [0;2]")


def strings_to_numbers(argument):
    switcher = {
        "Pierre": 0,
        "Papier": 1,
        "Ciseaux": 2,
    }
    return switcher.get(argument, "Nothing")


def equiality():
    print("Égaliter")


def victory():
    print("Vous avez gagné !")


def defeat():
    print("Vous avez perdu :(")


print("╔═══════════════════════════════╗")
print("║ Jeux Pierre Papier Ciseaux    ║")
print("╠═══════╦═══════════════════════╣")
print("║ Taper ║                       ║")
print("╠═══════╬═══════════════════════╣")
print("║     0 ║ Pierre                ║")
print("║     1 ║ Papier                ║")
print("║     2 ║ Ciseaux               ║")
print("║     X ║ Pour arrêter de jouer ║")
print("╚═══════╩═══════════════════════╝")

list = ["Pierre", "Papier", "Ciseaux"]

while (True):
    print("La partie commence !!!")
    userChoice = input()
    if userChoice.lower() == "x":
        break
    else:
        userChoice = int(userChoice)
        cumputerChoice = random.choice(list)
        print("User : ", numbers_to_strings(userChoice))
        print("Cumputer : ", cumputerChoice)
        if userChoice == 0:
            if strings_to_numbers(cumputerChoice) == 0:
                equiality()
            elif strings_to_numbers(cumputerChoice) == 1:
                defeat()
            elif strings_to_numbers(cumputerChoice) == 2:
                victory()
        elif userChoice == 1:
            if strings_to_numbers(cumputerChoice) == 0:
                victory()
            elif strings_to_numbers(cumputerChoice) == 1:
                equiality()
            elif strings_to_numbers(cumputerChoice) == 2:
                defeat()
        elif userChoice == 2:
            if strings_to_numbers(cumputerChoice) == 0:
                defeat()
            elif strings_to_numbers(cumputerChoice) == 1:
                victory()
            elif strings_to_numbers(cumputerChoice) == 2:
                equiality()
import main