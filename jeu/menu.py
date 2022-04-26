import pygame
import pygame_menu
from .constants import *
from .game import Game
from .IA.minimax import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jeu de Dames')
Difficulty=0

def set_difficulty(value, difficulty):
    """
    Retourne le niveau de difficulté dans une variable globale.

    :param value: Le niveau de difficulté
    :param difficulty: index du niveau de difficulté ("Facile => 1", "Intermédiaire => 2", "Expert => 3")
    :type value: tuple
    :type difficulty: int
    
    :return: None

        :Example:
        
         >>> set_difficulty((('Facile', 1), 1),1)
          # Pour un jeu facile
         >>> set_difficulty((('Intermédiaire', 2), 2),2)
          # Pour un jeu intermédiaire
    
    """
    global Difficulty
    Difficulty=difficulty

def get_row_col_from_mouse(pos):
    
    """
    Retourne la ligne et la colonne du carré selectionné à partir de la position du souris

    
    :param pos: la position du souris
    :type pos: tuple
    
    :return: retourne la ligne et la colonne du carré.

        :Example:
        
         >>> get_row_col_from_mouse(531, 446)
    
    """

    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def jouerADeux():
    """
    Elle permet de jouer aux dames à deux.
    Elle ne prend pas d'arguments.
    Fait appel à la classe Game du module game pour lancer le jeu.

    :return: None

        :Example:
        
         >>> jouerADeux()
    """
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

def contreIA():
    """
    Elle permet de jouer aux dames contre une IA.
    Elle ne prend pas d'arguments.
    Elle appelle la classe Game du module game pour lancer le jeu.
    Elle appelle la fonction minimax pour utiliser l'IA.
    
    :return: None

        :Example:
        
         >>> contreIA()
    """
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    if Difficulty==0:
        diff=0
        set_menu()
    elif Difficulty==1:
        diff=2
    elif Difficulty==2:
        diff=4
    else:
        diff=8
    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), diff, True, game)
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
    """
    Création du menu du jeu.
    On peut choisir le niveau de difficulté,
    si on veut commencer à jouer ou si on veut quitter le jeu
    :return: None

        :Example:
        
         >>> set_menu()
    """
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
    menu.add.button('1 joueur VS I.A', contreIA)
    
    #Quitter
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    
    #Lancement du menu
    menu.mainloop(surface)