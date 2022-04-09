import pygame
import pygame_menu
from constants import *
from game import Game
from IA.minimax import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jeu de Dames')

def set_difficulty(value, difficulty):
    pass

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def jouerADeux():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

def start_the_game():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

def set_menu():
    """Création du menu du jeu. On peut choisir le niveau de difficulté, si on veut commencer à jouer ou si on veut quitter le jeu"""
    #Initialisation et Paramètrage de Base
    pygame.init() 
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Bienvenue', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_DARK)
        
    #Jouer à deux
    menu.add.button('2 joueurs', jouerADeux)
    
    #Paramètrage des Difficultés
    menu.add.selector('Difficulté :', [('Niveau', 0) ,('Facile', 1),  ('Intermédiaire', 2), ('Expert', 3),], onchange=set_difficulty)
    
    #Jouer contre une IA
    menu.add.button('1 joueur VS I.A', start_the_game)
    
    #Quitter
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    
    #Lancement du menu
    menu.mainloop(surface)
    
set_menu()