import random

def linéaireGen():
    
    """
    
    Fonction qui génere deux nombre aléatoire
    a doit toujours etre supérieur a 0
    donc nous effectuons un do while

    """
    
    a = 0
    while a == 0:
        a = random.randint(-25, 25)

    question = random.randint(-20,20)

    # on aura donc quelque chose comme ax = question 

    return a,question


def Reponse(a, question):
    
    """calculer la réponse d'une fonction linéaire"""

    x = question / a

    return round(x, 2) # Arrondir au centième
