# 1 Partie guidée : Chemins et Labyrinthes

# Alias de types :
Coord = tuple[int , int]
Case = tuple[bool ,bool ,bool ,bool ,str]
Laby = list[list[Case]]

# Variables globales (Utiles pour les tests) :
laby1 : Laby = [[( True , True , False , False , ""), (False , False , True , False , "ENTREE")],
                [( True , False , False , True , ""), (False , False , True , False , "SORTIE")]]

# la fonction deplace :
def deplace(c : Coord, d : str) -> Coord :
    """ Precondition : (d == "N") || (d == "E") || (d == "S") || (d == "W") """
    x,y = c
    
    if (d == "N") :
        return (x, y + 1)
    if (d == "E") :
        return (x + 1, y)
    if (d == "S") :
        return (x, y - 1)
    if (d == "O") :
        return (x - 1, y)
# tests de la fonction deplace :
assert deplace ((0, 0) , "N") == (0, 1)
assert deplace ((3, 3) , "E") == (4, 3)
assert deplace ((deplace ((3, 3) , "N")), "S") == (3, 3)

# la fonction deplace_chemin :
def deplace_chemin(c : Coord, ch : list[str]) -> Coord :
    if (ch == []) :
        return c
    else :
        return deplace_chemin(deplace(c, ch[0]), ch[1:])
# tests de la fonction deplace_chemin :
assert deplace_chemin ((0, 0) , ["N", "N"]) == (0, 2)
assert deplace_chemin ((0, 0) , ["N", "E", "S", "O"]) == (0, 0)
assert deplace_chemin ((0, 0), []) == (0, 0)

# la fonction deplace_possible :
def deplace_possible(la : Laby, c : Coord, d : str) -> bool :
    """ Precondition : (d == "N") || (d == "E") || (d == "S") || (d == "W") """
    x, y = c
    if (d == "N") :
        r, _, _, _, _ = la[x][y]
        return r
    if (d == "E") :
        _, r, _, _, _ = la[x][y]
        return r
    if (d == "S") :
        _, _, r, _, _ = la[x][y]
        return r
    if (d == "O") :
        _, _, _, r, _ = la[x][y]
        return r
# tests de la fonction deplace_possible :
assert deplace_possible (laby1 , (0, 1), "S")
assert not deplace_possible (laby1 , (0, 1), "N")
assert not deplace_possible (laby1 , (0, 1), "E")

# la fonction chemin_possible :
def chemin_possible(la : Laby, c : Coord, ch : list [str]) -> bool :
    if (ch == []) :
        return True
    else :
        return deplace_possible(la, c, ch[0]) and chemin_possible(la, deplace(c, ch[0]), ch[1:])
    
# tests de la fonction chemin_possible :
assert chemin_possible (laby1 , (0, 1), ["S", "E", "N"])
assert chemin_possible (laby1 , (0, 1), ["S", "N", "S", "E", "N"])
assert not chemin_possible (laby1 , (0, 1), ["S", "O"])
assert not chemin_possible (laby1 , (0, 1), ["S", "E", "N", "O"])

# la fonction est_solution :
def est_solution(la : Laby, c : Coord, ch : list[str]) -> bool :
    x, y = c
    _, _, _, _, nat = la[x][y]
    if (nat != "ENTREE") :
        return False
    
    if (not chemin_possible(la, c, ch)) :
        return False
    
    x, y = deplace_chemin(c, ch)
    _, _, _, _, nat = la[x][y]
    if (nat != "SORTIE") :
        return False
    
    return True
# tests de la fonction est_solution :
assert est_solution (laby1 , (0, 1), ["S", "E", "N"])
assert est_solution (laby1 , (0, 1), ["S", "E", "O", "E", "N"])
assert not est_solution (laby1 , (0, 0), ["E", "N"])
assert not est_solution (laby1 , (0, 1), ["S", "E"])
assert not est_solution (laby1 , (0, 1), ["E"])
    