import pygame
import pygame_menu
from constants import *

def set_difficulty(value, difficulty):
    pass

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def start_the_game():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jeu de Dames')

def set_menu():
    """Création du menu du jeu. On peut choisir le niveau de difficulté, si on veut commencer à jouer ou si on veut quitter le jeu"""
    #Initialisation et Paramètrage de Base
    pygame.init() 
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Bienvenue', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_DARK)
    
    #Paramètrage des Difficultés
    menu.add.selector('Difficulté :', [('Facile', 1),  ('Intermédiaire', 2), ('Expert', 3),], onchange=set_difficulty)
    
    #Jouer
    menu.add.button('Jouer', start_the_game)
    
    #Quitter
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    
    #Lancement du menu
    menu.mainloop(surface)
    
set_menu()