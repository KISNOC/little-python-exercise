print("╔═══════════════════════════════════════════════════════════════╗")
print("║              Quelque exercice voulez-vous lancer ?            ║")
print("╠════╦══════════════════════════════════════════════════════════╣")
print("║  1 ║ The Right Price                                          ║")
print("║  2 ║ Pierre Papier Ciseaux                                    ║")
print("║  3 ║ Recherche Dichotomique                                   ║")
print("╚════╩══════════════════════════════════════════════════════════╝")

#choix = int(input())
choix = 3

if choix == 1:
    from theRightPrice import theRightPrice
elif choix == 2:
    from pierrePapierCiseaux import pierrePapierCiseaux
elif choix == 3:
    from rechercheDichotomique import rechercheDichotomique
