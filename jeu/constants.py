from screeninfo import get_monitors
import pygame

screen = get_monitors()[0]
FPS = 60
HEIGHT,WIDTH=800, 800
#HEIGHT,WIDTH=screen.height - 70, screen.width  #j'ai besoin de modifier ça un peu ça marche pas pour le moment 

#Nombre de Lignes et de Colonnes
ROWS, COLS = 8, 8

#Longueur de la case
SQUARE_SIZE=WIDTH//COLS

#Représentation des couleurs
RED = (255, 8, 0)
WHITE = (255, 255, 255)
BLACK = (36, 36, 36)
BLUE = (115, 194, 251)
GREY = (128,128,128)

#La couronne quand une pièce atteint le territoire de l'adversaire ?
COURONNE= pygame.transform.scale(pygame.image.load('divers/couronne.png'), (44, 25))