# Importation des fonctions définies dans Utilitaire.py
from Utilitaire import Laby
import random

# Alias de types :
join = list[tuple[int, int]]
Cjoin = list[join]
wall = tuple[int, int, int]

# création d'un labyrinthe complétement fermé avec une entrée et une sortie :
def CreatLaby(n : int) -> (Laby, Cjoin) :
    """Precondition : n > 1"""
    
    # Création du labyrinthe complétement fermé :
    laby : Laby = [[[False, False, False, False, ""] for _ in range(n)] for _ in range(n)]
    
    # Création de l'entrée :
    if (random.random() < 0.5) :
        if (random.random() < 0.5) :
            laby[0][int(random.random() * n)] = [False, False, False, False, "ENTREE"]
        else :
            laby[n - 1][int(random.random() * n)] = [False, False, False, False, "ENTREE"]
    else :
        if (random.random() < 0.5) :
            laby[int(random.random() * n)][0] = [False, False, False, False, "ENTREE"]
        else :
            laby[int(random.random() * n)][n - 1] = [False, False, False, False, "ENTREE"]

    # Création de la sortie :      
    if (random.random() < 0.5) :
        if (random.random() < 0.5) :
            i : int = int(random.random() * n) 
            while (laby[0][i] == [False, False, False, False, "ENTREE"]) :
                i = int(random.random() * n) 
            laby[0][i] = [False, False, False, False, "SORTIE"]
        else :
            i : int = int(random.random() * n) 
            while (laby[n - 1][i] == [False, False, False, False, "ENTREE"]) :
                i = int(random.random() * n) 
            laby[n - 1][i] = [False, False, False, False, "SORTIE"]
    else :
        if (random.random() < 0.5) :
            i : int = int(random.random() * n) 
            while (laby[i][0] == [False, False, False, False, "ENTREE"]) :
                i = int(random.random() * n) 
            laby[i][0] = [False, False, False, False, "SORTIE"]
        else :
            i : int = int(random.random() * n) 
            while (laby[i][n - 1] == [False, False, False, False, "ENTREE"]) :
                i = int(random.random() * n) 
            laby[i][n - 1] = [False, False, False, False, "SORTIE"]
    
    # Création des classes de joignabilité :
    cl : Cjoin = [[(i, j)] for i in range(n) for j in range(n)]

    return (laby, cl)

# tirer un mur aléatoire dans le labyrinthe :
def draw_wall(laby : Laby) -> wall :
    i : int = (int)(random.random() * len(laby))
    j : int = (int)(random.random() * len(laby))
    d : int

    if (i == 0) :
        if(j == 0) :
            d = (int)(random.random() * 2)
        elif(j == len(laby) - 1) :
            d = (int)(random.random() * 2) + 1           
        else :
            d = int(random.random() * 3)
    elif (i == len(laby) - 1) :
        if(j == 0) :
            d = 0 if random.random() < 0.5 else 3
        elif(j == len(laby) - 1) :
            d = (int)(random.random() * 2) + 2
        else :
            d = int(random.random() * 3) + 1
            d = 0 if(d == 1) else d
    elif (j == 0) :
        d = int(random.random() * 3)
        d = 3 if (d == 2) else d
    elif (j == len(laby) - 1) :
        d = int(random.random() * 3) + 1
    else :
        d = int(random.random() * 4)
    return (i, j, d)

# getjoin, c'est une fonction qui renvoie la classe de joignabilité de la case :
def getjoin(cl : Cjoin, i : int, j : int) -> join :
    """Precondition : i >= 0 and j >= 0"""
    return [c for c in cl if (i, j) in c][0]

# uni_join :
def uni_join(cl : Cjoin, c1 : join, c2 : join) -> Cjoin :
    return [c1 + c2] + [c for c in cl if (c != c1 and c != c2)]

# test_join, c'est une fonction qui teste si les deux cases situées de part et d'autre du mur sont joignable :
def test_join(cl : Cjoin, w : wall) -> bool :
    (i, j, d) = w
    return (getjoin(cl, i, j) == getjoin(cl, i, j + 1)) if (d == 0) else \
    (getjoin(cl, i, j) == getjoin(cl, i + 1, j)) if (d == 1) else \
    (getjoin(cl, i, j) == getjoin(cl, i, j - 1)) if (d == 2) else \
    (getjoin(cl, i, j) == getjoin(cl, i - 1, j))

# break_wall, c'est une fonction qui casse le mur passé en argument :
def break_wall(laby : Laby, w : wall) -> Laby :
    (i, j, d) = w
    if (d == 0) :
        n1, e1, s1, o1, t1 = laby[i][j]
        n2, e2, s2, o2, t2 = laby[i][j + 1]
        laby[i][j] = True, e1, s1, o1, t1
        laby[i][j + 1] = n2, e2, True, o2, t2   
    elif (d == 1) :
        n1, e1, s1, o1, t1 = laby[i][j]
        n2, e2, s2, o2, t2 = laby[i + 1][j]
        laby[i][j] = n1, True, s1, o1, t1
        laby[i + 1][j] = n2, e2, s2, True, t2    
    elif (d == 2) :
        n1, e1, s1, o1, t1 = laby[i][j]
        n2, e2, s2, o2, t2 = laby[i][j - 1]
        laby[i][j] = n1, e1, True, o1, t1
        laby[i][j - 1] = True, e2, s2, o2, t2   
    else :
        n1, e1, s1, o1, t1 = laby[i][j]
        n2, e2, s2, o2, t2 = laby[i - 1][j]
        laby[i][j] = n1, e1, s1, True, t1
        laby[i - 1][j] = n2, True, s2, o2, t2
    return laby

# Génération finale du labyrinthe :
def Generator(n : int) -> Laby :
    """Precondition : n > 1"""
    (laby, cl) = CreatLaby(n)
    while(len(cl) > 1) :
        w : wall = draw_wall(laby)
        if(not test_join(cl, w)) :
            break_wall(laby, w)
            # union des classes :
            (i, j, d) = w
            if(d == 0) :
                cl = uni_join(cl, getjoin(cl, i, j), getjoin(cl, i, j + 1))
            elif(d == 1) :
                cl = uni_join(cl, getjoin(cl, i, j), getjoin(cl, i + 1, j))
            elif(d == 2) :
                cl = uni_join(cl, getjoin(cl, i, j), getjoin(cl, i, j - 1))
            else :
                cl = uni_join(cl, getjoin(cl, i, j), getjoin(cl, i - 1, j))

    return laby

    