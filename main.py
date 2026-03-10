def creer_grille():
    plateau = []

    for i in range(8):
        ligne = []

        for j in range(8):
            ligne.append(" ")

        plateau.append(ligne)

    ajouter_noirs_grille(plateau)
    ajouter_blancs_grille(plateau)

    afficher_plateau(plateau)


def ajouter_noirs_grille(plateau):
    for j in range(1, 8, 2):
        plateau[0][j] = "n"  # 1ere rangée
        plateau[2][j] = "n"  # 3eme rangée

    for j in range(0, 8, 2):
        plateau[1][j] = "n"  # 2eme rangée


def ajouter_blancs_grille(plateau):
    for j in range(1, 8, 2):
        plateau[7][j] = "b"
        plateau[5][j] = "b"

    for j in range(0, 8, 2):
        plateau[6][j] = "b"


def est_dans_grille(plateau):
    pass


def est_au_bon_format(plateau):
    pass


def afficher_plateau(plateau):
    print("""
--------------------------------
 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
--------------------------------""")

    for i in plateau:
        for j in i:
            print(f" {j} |", end="")
        print("")

    # TODO: mettre les lettres a coté et faire en sorte que l'on puisse savoir a quel tour c'est.


creer_grille()
