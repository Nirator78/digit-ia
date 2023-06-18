import os
import matplotlib.pyplot as plt
from utils.choice_loader import choice_loader

# Chemin du dossier contenant les sous-dossiers d'images
dossier_parent = choice_loader()

# Liste des sous-dossiers
sous_dossiers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Initialisation des listes pour les données du graphique
noms_categories = []
nombres_images = []

# Parcours des sous-dossiers
for sous_dossier in sous_dossiers:
    chemin_sous_dossier = os.path.join(dossier_parent, sous_dossier)
    if os.path.isdir(chemin_sous_dossier):
        # Comptage du nombre d'images dans chaque sous-dossier
        images = os.listdir(chemin_sous_dossier)
        nombre_images = len(images)
        noms_categories.append(sous_dossier)
        nombres_images.append(nombre_images)

# Création du graphique en barres
plt.bar(noms_categories, nombres_images)

# Ajout d'une légende
plt.xlabel("Catégories")
plt.ylabel("Nombre d'images")
plt.title("Nombre d'images par catégorie")
filename = "distribution_" + dossier_parent.replace("-", "_") + ".png"
path = os.path.join("stat", filename)
plt.savefig(path)
