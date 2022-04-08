from screeninfo import get_monitors
import pygame

screen = get_monitors()[0]
FPS = 60
HEIGHT,WIDTH=screen.height - 70, screen.width
ROWS, COLS = 8, 8
SQUARE_SIZE=WIDTH//COLS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
COURONNE= pygame.transform.scale(pygame.image.load('divers/couronne.png'), (44, 25))