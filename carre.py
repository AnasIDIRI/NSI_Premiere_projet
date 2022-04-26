from random import randint
from math import sqrt

def Generer():

    """
    générer un nombre afin d'obtenir quelque chose comme x² = a
    """
    
    a = randint(0,25)

    return a


def Calculer(a):

    """
    Calculer la réponse 
    """

    rep = round(sqrt(a), 2)

    return rep

