# les imports
from Utilitaire import Case, Laby
from Generateur import *
from IGraphique import *

def main() :
    # saisie de la taille du labyrinthe :
    n = 0
    while(1 >= n) :
        entree = input("Veuillez saisir une taille supérieure à 1 pour le labyrinthe : ")
        try :
            n = (int)(entree)
        except ValueError:
            print("Echec ! Ce que vous avez saisi n'est pas un entier valide.")

    # création et affichage du labyrinthe :
    draw_laby(Generator(n))

# Execution du programme :
main()