def creer_grille() -> list[list]:
    plateau = []

    for i in range(8):
        ligne = []

        for j in range(8):
            ligne.append(" ")

        plateau.append(ligne)

    ajouter_noirs_grille(plateau)
    ajouter_blancs_grille(plateau)

    afficher_plateau(plateau, "noirs")

    return plateau


def ajouter_noirs_grille(plateau: list[list]):
    for j in range(1, 8, 2):
        plateau[0][j] = "n"  # 1ere rangée
        plateau[2][j] = "n"  # 3eme rangée

    for j in range(0, 8, 2):
        plateau[1][j] = "n"  # 2eme rangée


def ajouter_blancs_grille(plateau: list[list]):
    for j in range(1, 8, 2):
        plateau[7][j] = "b"
        plateau[5][j] = "b"

    for j in range(0, 8, 2):
        plateau[6][j] = "b"


def est_dans_grille(plateau: list[list]):
    pass


def est_au_bon_format(plateau: list[list]):
    pass


# print(f"...") permet de mettre une variable dans un print et d'éviter de faire print("..." + variable + "...")
def afficher_plateau(plateau: list[list], tour_de_jeu: str):
    lettres = ["H", "G", "F", "E", "D", "C", "B", "A"]
    # Permet d'afficher les lettres sur le coté, a chaque itération on pop le tableau.

    print("""
--------------------------------------
  x |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
--------------------------------------""")

    for ligne in plateau:
        print(f"| {lettres.pop()} | ", end="")

        for colonne in ligne:
            print(f" {colonne} |", end="")

        print("")

    print("--------------------------------------")
    print(f"C'est au tour des pions {tour_de_jeu} de jouer.")


creer_grille()
