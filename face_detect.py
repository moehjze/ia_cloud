#!/usr/bin/python

import cv2
import sys

if len(sys.argv) != 2:
    print("Syntax error\nSyntax:", sys.argv[0], "[IMAGE PATH]")
    exit(1)

# On charge la cascade (pré-traitement pour reconnaitre des visages)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread(sys.argv[1])  # On charge l'image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Conversion niveaux de gris

# On détecte les visages avec la cascade
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# On dessine les rectanges autour des visages
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)  # On affiche la sortie
cv2.waitKey()  # On attend une touche pour fermer