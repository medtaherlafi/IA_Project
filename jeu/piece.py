from .constants import *
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        """Initialisation"""
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Calculer la position"""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """Rendre roi"""
        self.king = True
    
    def draw(self, win):
        """Dessine une pièce"""
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(COURONNE, (self.x - COURONNE.get_width()//2, self.y - COURONNE.get_height()//2))

    def move(self, row, col):
        """Déplacer une pièce"""
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)