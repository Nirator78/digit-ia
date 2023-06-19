import os

# Liste des noms de dossiers à créer
dossier_liste = [
    "train-image",
    "train-image-decalle", 
    "train-image-decalle-plus", 
    "train-image-decalle-banger", 
    "train-image-decalle-banger-2", 
    "retrain-image", 
    "test-image", 
    "temp-image", 
    "to-validate-image",
    "numpy-array"
]

# Parcours de la liste
for dossier in dossier_liste:
    # Vérifie si le dossier existe
    if not os.path.exists(dossier):
        # Crée le dossier s'il n'existe pas
        print(f"Création du dossier {dossier}")
        os.makedirs(dossier)

# Liste des noms des dossier à créer dans le dossier api
dossier_liste_api = [
    "temp"
]

# Parcours de la liste
for dossier in dossier_liste_api:
    # Vérifie si le dossier existe
    if not os.path.exists("api/" + dossier):
        # Crée le dossier s'il n'existe pas
        print(f"Création du dossier {dossier}")
        os.makedirs("api/" + dossier)
