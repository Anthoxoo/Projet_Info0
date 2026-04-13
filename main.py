# Constante, valeur qui ne changera pas, nous donne la valeur de la colonne en fonction de la lettre.
LETTRE_VALEUR = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
}


def creer_grille_debut_partie() -> list[list]:
    return [
        [" ", "n", " ", "n", " ", "n", " ", "n"],
        ["n", " ", "n", " ", "n", " ", "n", " "],
        [" ", "n", " ", "n", " ", "n", " ", "n"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["b", " ", "b", " ", "b", " ", "b", " "],
        [" ", "b", " ", "b", " ", "b", " ", "b"],
        ["b", " ", "b", " ", "b", " ", "b", " "],
    ]


def creer_grille_milieu_partie() -> list[list]:
    return [
        [" ", "n", " ", " ", " ", "n", " ", "n"],
        [" ", " ", "n", " ", "n", " ", " ", " "],
        [" ", " ", " ", "n", " ", " ", " ", "n"],
        [" ", " ", " ", " ", "b", " ", " ", " "],
        [" ", "n", " ", "b", " ", " ", " ", " "],
        ["b", " ", " ", " ", "b", " ", "b", " "],
        [" ", " ", " ", "b", " ", " ", " ", "b"],
        ["b", " ", "b", " ", " ", " ", "b", " "],
    ]


def creer_grille_fin_partie() -> list[list]:
    return [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "n", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "b", " ", "n", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "b", " ", " ", " ", "b", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
    ]


def est_dans_grille(ligne: str, colonne: int, grille: list[list]):

    # Dictionnaire qui associe chaque lettre autorisée dans le damier à la valeur de la colonne donc A première colonne -> "A": 1, B deuxieme colonne donc "B": 2 etc

    # Si la ligne donnée par l'utilisateur n'est pas dans le dictionnaire (= lettres autorisées)
    if ligne not in LETTRE_VALEUR.keys():
        return False

    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    # Prend la valeur associée a la lettre donnée par l'utilisateur
    valeur_lettre = LETTRE_VALEUR[ligne]

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


def saisie_coordonnees(grille: list[list]) -> tuple:

    while True:  # Boucle tant que l'utilisateur n'a pas rentré une information valide qui menerait à un return -> sortie de fonction
        reponse_utilisateur = str(input("Veuillez entrez des coordonnées : ")).upper()

        if not est_au_bon_format(reponse_utilisateur):
            print("Format invalide : [A-H][1-8]")
            continue  # Recommence la boucle au début (passe tout le code suivant)

        ligne = reponse_utilisateur[0]
        colonne = reponse_utilisateur[1]

        if est_dans_grille(ligne, int(colonne), grille):
            return (LETTRE_VALEUR[ligne] - 1, int(colonne) - 1)

        else:
            print("La position n'est pas dans la grille.")


def deplacer_pion(grille: list[list], tour_de_jeu: str) -> int:

    LETTRE_COULEUR = tour_de_jeu[0]

    print("Quel pion souhaitez-vous déplacer ?")
    pion_joueur_actif, ligne_base, colonne_base = demander_saisie_pion_a_deplacer(
        grille
    )

    while not est_meme_couleur(LETTRE_COULEUR, pion_joueur_actif):
        print("Ce pion ne vous appartient pas.")
        pion_joueur_actif, ligne_base, colonne_base = demander_saisie_pion_a_deplacer(
            grille
        )

    print("Où souhaitez-vous le déplacer ?")

    while True:
        case_position_finale, ligne_finale, colonne_finale = (
            demander_saisie_pion_a_deplacer(grille)
        )

        # On calcule les distances
        diff_lignes = abs(ligne_finale - ligne_base)
        diff_colonnes = abs(colonne_finale - colonne_base)

        # 1. Le déplacement doit être une diagonale stricte de 1 ou 2 cases
        if diff_lignes != diff_colonnes or diff_lignes not in [1, 2]:
            print("Déplacement incorrect. Diagonale de 1 ou 2 cases uniquement.")
            continue  # Échec : on recommence la boucle pour demander une nouvelle case

        # 2. La case d'arrivée doit TOUJOURS être vide
        if case_position_finale != " ":
            print("Mouvement impossible : la case d'arrivée est occupée.")
            continue  # Échec : on recommence la boucle

        # --- CAS N°1 : Déplacement simple (1 case) ---
        if diff_lignes == 1:
            grille[ligne_finale][colonne_finale] = pion_joueur_actif
            grille[ligne_base][colonne_base] = " "
            return 0  # 0 pion mangé

        # --- CAS N°2 : Capture (2 cases) ---
        if diff_lignes == 2:
            # On calcule les coordonnées de la case du milieu
            ligne_milieu = (ligne_base + ligne_finale) // 2
            colonne_milieu = (colonne_base + colonne_finale) // 2
            pion_saute = grille[ligne_milieu][colonne_milieu]

            # On vérifie que la case sautée contient bien un adversaire
            if pion_saute == " " or pion_saute == LETTRE_COULEUR:
                print("Saut invalide : vous devez sauter par-dessus un pion adverse !")
                continue  # Échec : on recommence la boucle

            # Si toutes les vérifications sont bonnes, on applique les changements
            grille[ligne_finale][colonne_finale] = pion_joueur_actif
            grille[ligne_base][colonne_base] = " "
            grille[ligne_milieu][colonne_milieu] = " "  # On efface le pion mangé

            return 1  # 1 pion mangé


def est_meme_couleur(couleur_case_base: str, couleur_case_finale: str):
    if couleur_case_base == couleur_case_finale:
        return True
    else:
        return False


def est_diagonale(
    ligne_base: int, colonne_base: int, ligne_finale: int, colonne_finale: int
) -> bool:

    # On calcule la distance absolue parcourue
    diff_lignes = abs(ligne_finale - ligne_base)
    diff_colonnes = abs(colonne_finale - colonne_base)

    # C'est une diagonale d'une seule case si la différence est de 1 sur les deux axes
    if diff_lignes == 1 and diff_colonnes == 1:
        return True
    return False


def demander_saisie_pion_a_deplacer(
    grille: list[list],
) -> tuple[str, int, int]:

    coordonnees = saisie_coordonnees(grille)
    ligne, colonne = coordonnees
    pion_joueur_actif = grille[ligne][colonne]

    return pion_joueur_actif, ligne, colonne


def afficher_grille(
    grille: list[list],
    tour_de_jeu: str,
    nb_pions_captures_noirs: int,
    nb_pions_captures_blancs: int,
):
    # print(f"...") permet de mettre une variable dans un print et d'éviter de faire print("..." + variable + "...")

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

    print(
        f"Les noirs ont capturés {nb_pions_captures_noirs} pièces.\nLes blancs ont capturés {nb_pions_captures_blancs} pièces.\n "
    )
    print(f"C'est au tour des {tour_de_jeu} de jouer.\n")


def jeu(grille: list[list], tour_de_jeu: str):
    nb_pions_captures_par_noirs = 0
    nb_pions_captures_par_blancs = 0

    afficher_grille(
        grille, tour_de_jeu, nb_pions_captures_par_noirs, nb_pions_captures_par_blancs
    )

    while True:
        afficher_grille(
            grille,
            tour_de_jeu,
            nb_pions_captures_par_noirs,
            nb_pions_captures_par_blancs,
        )
        nb_pions_mange = deplacer_pion(grille, tour_de_jeu)

        if tour_de_jeu == "blancs":
            nb_pions_captures_par_blancs += nb_pions_mange
            tour_de_jeu = "noirs"
        else:
            nb_pions_captures_par_noirs += nb_pions_mange
            tour_de_jeu = "blancs"

        if nb_pions_captures_par_blancs == 12:
            print(
                "Les blancs ont remportés la victoire, ils ont capturés tous les pions adverses."
            )
            break

        elif nb_pions_captures_par_noirs == 12:
            print(
                "Les noirs ont remportés la victoire, ils ont capturés tous les pions adverses."
            )
            break


def main():
    # Fonction principale, appelle les autres fonctions et stocke les variables ici.

    # On teste d'abord si le code tourne sinon le programme s'arrete
    test()

    tour_de_jeu = "blancs"
    grille = creer_grille_debut_partie()
    # grille = creer_grille_milieu_partie()
    # grille = creer_grille_fin_partie()

    jeu(grille, tour_de_jeu)


###### TESTS #######


def test():  # Fonction de test principale, appelle chacune des petites fonctions de test et effectue un test global

    def test_est_au_bon_format():

        assert est_au_bon_format("A8")
        assert not est_au_bon_format("AA")
        assert not est_au_bon_format("55")
        assert not est_au_bon_format("A12")
        assert not est_au_bon_format("")
        assert est_au_bon_format("Z9")

    def test_est_dans_grille():

        grille = creer_grille_debut_partie()
        assert est_dans_grille("A", 3, grille)
        assert not est_dans_grille("M", 2, grille)
        assert not est_dans_grille("B", 9, grille)
        assert not est_dans_grille("", 3, grille)
        assert not est_dans_grille("", 0, grille)

    def test_est_diagonale():

        assert est_diagonale(3, 3, 4, 4)  # Diagonale Bas-Droite
        assert est_diagonale(3, 3, 2, 2)  # Diagonale Haut-Gauche
        assert est_diagonale(3, 3, 4, 2)  # Diagonale Bas-Gauche
        assert est_diagonale(3, 3, 2, 4)  # Diagonale Haut-Droite
        assert not est_diagonale(3, 3, 3, 3)  # Aucun mouvement (reste sur la même case)
        assert not est_diagonale(3, 3, 5, 5)  # Diagonale de 2 cases
        assert not est_diagonale(1, 1, 8, 8)  # Diagonale de bout en bout du plateau
        assert not est_diagonale(3, 3, 5, 4)  # +2 lignes, +1 colonne
        assert not est_diagonale(3, 3, 2, 5)  # -1 ligne, +2 colonnes

    test_est_au_bon_format()
    test_est_dans_grille()
    test_est_diagonale()

    print(" TESTS OK")


main()
