import random
from math import *


def rechercheDichotomique(nbrChercher, tableauCible):
    startIndex = 0
    endIndex = len(tableauCible) - 1

    while startIndex <= endIndex:
        mediumSupIndex = ceil((startIndex + endIndex) / 2)
        if tableauCible[mediumSupIndex] == nbrChercher:
            return mediumSupIndex
        elif tableauCible[mediumSupIndex] > nbrChercher:
            print("Plus petit (", mediumSupIndex, ")")
            endIndex = mediumSupIndex - 1
        elif tableauCible[mediumSupIndex] < nbrChercher:
            print("Plus grand (", mediumSupIndex, ")")
            startIndex = mediumSupIndex + 1

#      0   1   2   3   4   5   6   7   8   9  10
tab = [6, 16, 27, 33, 42, 46, 50, 62, 68, 79, 94]
nbr = random.choice(tab)

print("NBR : ", nbr)
print("Le nombre ", nbr, " se trouve dans l'index ", rechercheDichotomique(nbr, tab))
