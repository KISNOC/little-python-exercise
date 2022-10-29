print("╔═══════════════════════════════════════════════════════════════╗")
print("║              Quelque exercice voulez-vous lancer ?            ║")
print("╠════╦══════════════════════════════════════════════════════════╣")
print("║  1 ║ The Right Price                                          ║")
print("║  2 ║ Pierre Papier Ciseaux                                    ║")
print("╚════╩══════════════════════════════════════════════════════════╝")


choix = int(input())
if choix == 1:
    from theRightPrice import theRightPrice
if choix == 2:
    from pierrePapierCiseaux import pierrePapierCiseaux
