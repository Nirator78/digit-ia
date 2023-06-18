import os
import numpy as np
from keras.utils import load_img, img_to_array
from utils.choice_loader import choice_loader

# Nom du dossier à parcourir
path_to_compile = choice_loader()
# Classes à parcourir
classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Taille des images
img_rows = 28
img_cols = 28

def check_duplicate_images(images):
    num_images = len(images)
    for i in range(num_images):
        for j in range(i + 1, num_images):
            if np.array_equal(images[i], images[j]):
                return True
    return False

def load_images_from_folder(folder):
    images = []
    for file in os.listdir(folder):
        print("Image de la classe : " + folder + " fichier : " + file)
        path_image = os.path.join(folder, file)
        img = load_img(path_image, target_size=(img_rows, img_cols), color_mode="grayscale")
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x /= 255.
        images.append(x)
    return np.array(images)

duplicates_found = False

for classe in classes:
    path_classe = os.path.join(path_to_compile, classe)
    images = load_images_from_folder(path_classe)
    if check_duplicate_images(images):
        duplicates_found = True
        print("Des images identiques ont été trouvées dans la classe", classe)

if not duplicates_found:
    print("Aucune image identique trouvée dans le dossier.")