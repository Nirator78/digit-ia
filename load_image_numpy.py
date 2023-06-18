import os
import numpy as np
from keras.utils import load_img, img_to_array
from utils.choice_loader import choice_loader

# Chemin du dossier numpy-array
path_numpy = "numpy-array"
# Nom du dossier à parcourir
path_to_compile = choice_loader()
# Nom des fichiers à sauvegarder
x_file_name = "X_numpy_array"
y_file_name = "Y_numpy_array"
# Classes à parcourir
classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Taille des images
img_rows = 28 
img_cols = 28

X = []
Y = []

for classe in classes:
    path_classe = os.path.join(path_to_compile, classe)
    for file in os.listdir(path_classe):
        print("Image de la classe : " + classe + " fichier : " + file)
        path_image = os.path.join(path_classe, file)
        img = load_img(path_image, target_size=(img_rows, img_cols), color_mode = "grayscale")
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x /= 255.
        X.append(np.array(x))
        Y.append(classes.index(classe))
        
X = np.array(X)
Y = np.array(Y)  

# Suppression des fichiers s'ils existent
if os.path.exists(f"{path_numpy}{path_to_compile}{x_file_name}.npy"):
    os.remove(f"{path_numpy}{path_to_compile}{x_file_name}.npy")
if os.path.exists(f"{path_numpy}{path_to_compile}{y_file_name}.npy"):
    os.remove(f"{path_numpy}{path_to_compile}{y_file_name}.npy")

# Création des dossiers s'ils n'existent pas
if not os.path.exists(path_numpy):
    os.mkdir(path_numpy)

path_to_save_full = os.path.join(path_numpy, path_to_compile)
if not os.path.exists(path_to_save_full):
    os.mkdir(path_to_save_full)

# Chemin des fichiers à sauvegarder
x_file_path = os.path.join(path_to_save_full, x_file_name)
y_file_path = os.path.join(path_to_save_full, y_file_name)

# Sauvegarde des fichiers
np.save(x_file_path, X)
np.save(y_file_path, Y)