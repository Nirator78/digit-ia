# Fonction principale
def choice_epoch():
    # Affichage du menu
    print("Choisissez de faire :")
    print("1. 20 epochs")
    print("2. 30 epochs")

    # Lecture du choix
    while True:
        choix = input("Entrez le numéro de votre choix : ")
        if choix.isdigit() and 1 <= int(choix) <= 2:
            choix = int(choix)
            break
        print("Choix invalide. Veuillez réessayer.")

    # Mapping entre les choix et les loaders
    loaders = {
        1: 20,
        2: 30,
    }

    loader_choisie = loaders[choix]
    print("Vous avez choisi de faire :", loader_choisie, "epochs")

    return loader_choisie