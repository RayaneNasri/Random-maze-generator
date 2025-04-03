# Importation des fonctions définies dans Utilitaire.py
from Utilitaire import Case, Laby
import pygame
import sys

# initialisation de Pygame :
pygame.init()

# stop, qui arrête le programme afin de visualiser la fenêtre graphique : 
def stop() :
    while True :
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

# draw_case :
def draw_case(fenetre, i : int, j : int, c : Case, u : int) :
    """Precondition : i >= 0 and j >= 0 and u > 0"""
    (n, e, s, o, t) = c
    if(not s) :
        pygame.draw.line(fenetre, (0, 0, 0), (i, j + u), (i + u, j + u))
    if(not e) :
        pygame.draw.line(fenetre, (0, 0, 0), (i + u, j), (i + u, j + u))
    if(not n) :
        pygame.draw.line(fenetre, (0, 0, 0), (i, j), (i + u, j))
    if(not o) :
        pygame.draw.line(fenetre, (0, 0, 0), (i, j), (i, j + u))
    
    if(t == "ENTREE") :
        pygame.draw.circle(fenetre, (255, 0, 0), ((i + u // 2), (j + (u // 2))), u / 4)
    if(t == "SORTIE") :
        pygame.draw.circle(fenetre, (0, 255, 0), ((i + u // 2), (j + (u // 2))), u / 4, 2)

# draw_laby :
def draw_laby(laby : Laby) :
    n : int = len(laby)

    fenetre = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("GLabyrinthe")
    fenetre.fill((255, 255, 255))

    u : int = 500 // n
    for i in range(n) :
        for j in range(n) :
            draw_case(fenetre, u*i, u*j, laby[i][n - j - 1], u)
    pygame.image.save(fenetre, "Labyrinthe.png")
    stop()
