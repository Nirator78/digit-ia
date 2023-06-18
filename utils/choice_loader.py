# Fonction principale
def choice_loader():
    # Affichage du menu
    print("Choisissez de charger :")
    print("1. Image base: 42 000 images")
    print("2. Image decalle: 210 000 images")
    print("3. Image decalle PLUS: 546 000 images")
    print("4. Image decalle BANGER: 1 050 000 images")

    # Lecture du choix
    while True:
        choix = input("Entrez le numéro de votre choix : ")
        if choix.isdigit() and 1 <= int(choix) <= 4:
            choix = int(choix)
            break
        print("Choix invalide. Veuillez réessayer.")

    # Mapping entre les choix et les loaders
    loaders = {
        1: 'train-image',
        2: 'train-image-decalle',
        3: 'train-image-decalle-plus',
        4: 'train-image-decalle-banger'
    }

    loader_choisie = loaders[choix]
    print("Vous avez choisi de charger :", loader_choisie)

    return loader_choisie