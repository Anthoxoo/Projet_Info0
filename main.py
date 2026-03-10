def creer_grille() -> list[list]:

    grille = []

    # on appelle par convention _ une variable non utilisée.
    for _ in range(8):
        ligne = []

        for _ in range(8):
            ligne.append(" ")

        grille.append(ligne)

    ajouter_noirs_grille(grille)
    ajouter_blancs_grille(grille)

    return grille


def ajouter_noirs_grille(grille: list[list]):

    for j in range(1, 8, 2):
        grille[0][j] = "n"  # 1ere rangée
        grille[2][j] = "n"  # 3eme rangée

    for j in range(0, 8, 2):
        grille[1][j] = "n"  # 2eme rangée


def ajouter_blancs_grille(grille: list[list]):

    for j in range(1, 8, 2):
        grille[7][j] = "b"
        grille[5][j] = "b"

    for j in range(0, 8, 2):
        grille[6][j] = "b"


def est_dans_grille(ligne: str, colonne: int, grille: list[list]):

    lettre_valeur = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
    }

    if (
        ligne not in lettre_valeur.keys()
    ):  # Si la ligne donnée par l'utilisateur n'est pas dans les lettres autorisées
        return False

    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    valeur_lettre = lettre_valeur[ligne]

    if (0 < valeur_lettre <= nb_lignes) and (0 < colonne <= nb_colonnes):
        return True
    else:
        return False


def est_au_bon_format(message: str) -> bool:

    if len(message) != 2:
        return False

    lettre = message[0]
    chiffre = message[1]

    # Si le code ascii de lettre n'est pas compris entre le code ascii de A et Z inclus
    if not (65 <= ord(lettre) <= 90):
        return False

    # Si le code ascii de chiffre n'est pas compris entre le code ascii de 0 et 9 inclus
    if not (48 <= ord(chiffre) <= 57):
        return False

    return True


def saisie_coordonnées(grille: list[list]) -> tuple:

    while True:
        reponse_utilisateur = input("Veuillez entrez des coordonnées : ")

        if not est_au_bon_format(reponse_utilisateur):
            print("Format invalide : [A-H][1-8]")
            continue  # Recommence la boucle au début (passe tout le code suivant)

        ligne = reponse_utilisateur[0]
        colonne = reponse_utilisateur[1]

        if est_dans_grille(ligne, int(colonne), grille):
            return (ligne, colonne)

        else:
            print("La position n'est pas dans la grille.")


# print(f"...") permet de mettre une variable dans un print et d'éviter de faire print("..." + variable + "...")
def afficher_grille(grille: list[list], tour_de_jeu: str):

    lettres = ["H", "G", "F", "E", "D", "C", "B", "A"]
    # Permet d'afficher les lettres sur le coté, a chaque itération on pop le tableau (= on enleve le dernier element et on l'affiche).

    print("""
--------------------------------------
| x |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
--------------------------------------""")

    for ligne in grille:
        print(f"| {lettres.pop()} | ", end="")

        for element in ligne:
            print(f" {element} |", end="")

        print("")

    print("--------------------------------------")

    print(f"C'est au tour des pions {tour_de_jeu} de jouer.")


def main():

    grille = creer_grille()
    afficher_grille(grille, "noirs")
    saisie_coordonnées(grille)


def test():

    def test_est_au_bon_format():

        assert est_au_bon_format("A8")
        assert not est_au_bon_format("AA")
        assert not est_au_bon_format("55")
        assert not est_au_bon_format("A12")
        assert not est_au_bon_format("")
        assert est_au_bon_format("Z9")

    def test_est_dans_grille():

        grille = creer_grille()
        assert est_dans_grille("A", 3, grille)
        assert not est_dans_grille("M", 2, grille)
        assert not est_dans_grille("B", 9, grille)
        assert not est_dans_grille("", 3, grille)
        assert not est_dans_grille("", 0, grille)

    test_est_au_bon_format()
    test_est_dans_grille()


test()
main()
