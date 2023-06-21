import os
import cv2
import numpy as np

# Chemin du dossier d'origine contenant les images
input_folder = 'train-image-decalle-banger'

# Chemin du dossier de destination pour les images décalées
output_folder = 'train-image-decalle-banger-2'

# Vérification et création du dossier de destination s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Liste des sous-dossiers correspondant aux chiffres
classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Parcours des sous-dossiers
for classe in classes:
    input_subfolder = os.path.join(input_folder, classe)
    output_subfolder = os.path.join(output_folder, classe)
    
    # Vérification et création du sous-dossier de destination pour le chiffre s'il n'existe pas
    if not os.path.exists(output_subfolder):
        os.makedirs(output_subfolder)
    
    # Parcours des images dans le sous-dossier
    for filename in os.listdir(input_subfolder):
        print("Image de la classe : " + classe + " fichier : " + filename)
        image_path = os.path.join(input_subfolder, filename)
        output_path = os.path.join(output_subfolder, filename)
        
        # Lecture de l'image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Sauvegarde de l'image d'origine
        cv2.imwrite(os.path.join(output_subfolder, f"original_{filename}"), image)

        # Rotation de l'image de 15° vers la gauche et vers la droite
        # Obtenir les dimensions de l'image
        height, width = image.shape[:2]

        # Créer une matrice de rotation pour une rotation de 15 degrés
        rotation_matrix_left = cv2.getRotationMatrix2D((width/2, height/2), 15, 1)
        rotation_matrix_right = cv2.getRotationMatrix2D((width/2, height/2), -15, 1)

        # Effectuer la rotation de 15 degrés à gauche
        rotated_image_left = cv2.warpAffine(image, rotation_matrix_left, (width, height))

        # Effectuer la rotation de 15 degrés à droite
        rotated_image_right = cv2.warpAffine(image, rotation_matrix_right, (width, height))

        # Convertir les images en tableaux numpy de type float32
        image = image.astype(np.float32) / 255.
        rotated_image_left = rotated_image_left.astype(np.float32) / 255.
        rotated_image_right = rotated_image_right.astype(np.float32) / 255.

        # Sauvegarder les images résultantes
        cv2.imwrite(os.path.join(output_subfolder, f"rotate_15_left_{filename}"), (rotated_image_left * 255).astype(np.uint8))
        cv2.imwrite(os.path.join(output_subfolder, f"rotate_15_right_{filename}"), (rotated_image_right * 255).astype(np.uint8))
