from random import randint 

def générer_affine():

    """
    
    Cette fonction permet de generer une fonction affine 

    """

    # Tout d'abord on definit 2 variables a et b :

    a=randint(-10,10)
    b=randint(-10,10)
    
    # Ensuite on créer une boucle de gestion d'erreur , en effet si a=0 lors de la résolution
    # de l'équation nous serons forcer de faire une division par zéro.

    while a==0:
        a=randint(0,10)

    # je retourne les 2 nombres généré

    return a,b


def rs_affine(a,b):

    """
    
    Cette fonction calcul la valeur de x dans une fonction affine
    
    """

    x = -b/a
    x = round(x, 2) # Encore une fois, on arrondit au centième près

    return x


def afficher(b):

    """
    
    Fonction qui permet l'affichage de la fonction 
    
    elle sert a éviter d'obtenir quelque chose comme 
    
    2x + -5
    ou
    2x 6

    et à obtenir quelque comme 2x - 5 ou 2x + 6

    """

    if b>=0:
        return f"+ {b}"
    else:
        return f"{b}"
