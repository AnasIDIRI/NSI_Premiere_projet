from random import randint
from math import sqrt

def GenerationPolynome():

    """
    Cette fonction permet de générer un polynome avec un delta supérieur à 0 
    afin qu'il ai des solutions dans R.
    """

    a,b,c=0,0,0         # Notre polynome sera une liste contenant 
    polynome = [a,b,c]  # 3 nombres : a, b et c
    
    u = False # On force l'entrée dans la boucle
     
    while u==False:

        """
        Cette boucle permet de génerer 3 nombres aléatoires entre -10 et 10 pour a, b et c 
        il vérifie également que le polynome possède des solutions dans R. 
        
        """

        for i in range(0,3):
            polynome[i] = randint(-10,10) # Génération des 3 nombres, qu'on place dans le tableau


        if CalculerDelta(polynome) >= 0 and ( polynome[0] > 0 or polynome[0] < 0 ) :
            u = True
        else:
            u= False # On s'assure que le polynome à des solutions dans R et qu'il est calculable 

    return(polynome)


def CalculerDelta(polynome): 

    """
    Cette fonction permet de calculer le discriminant d'un polynome
    en s'appuyant sur la formule apprise en seconde : b²-4ac
    """

    delta = (polynome[1] ** 2 ) - ( 4 * polynome[0] * polynome[2] )
    
    return delta

def CalculerRacines(polynome): 

    """
    Cette fonction vérifie combien de solutions possède notre polynome
    et calcul ces dérnières : si le discrimnant > 0 il y a 2 solutions, sinon
    il n y en a qu'une. 
    
    """
    
    delta = CalculerDelta(polynome)

    if delta>0:
        
        # J'utilise -1 * variable afin de la rendre négative comme l'exige la formule
        
        
        s1 = round(( -1 *  polynome[1] +    sqrt(delta)) /  (2 * polynome[0]), 2) 
        s2 = round(( -1 *  polynome[1] -1 * sqrt(delta)) /  (2 * polynome[0]), 2)
        # On utilise la fonction round() avec comme second paramètre "2" pour arrondir a la centième
        
        resultat = [s1,s2]


    elif delta==0:
        s1 = -1 * polynome[1] / 2 * polynome[0]
        resultat = [s1] 

    return resultat

def Afficher(polynome):

    """
    Cette fonction permet d'afficher le polynome , en effet celui ci n'est qu'une liste de 3 nombres.
    Il nous faut donc procéder à quelque opérations complexe afin de l'afficher correctement.
    
    """
    
    affichage = f"{polynome[0]}x²" # Tout d'abord on prends "a" et on place x² juste après afin d'obtenir ax²
        
    if polynome[1] >= 0:
        affichage += f" + {polynome[1]}x" # Pour éviter un polynome de type 8x² 20x 5, nous ajoutons les "+" manuellement
    else:                                 
        affichage += f" {polynome[1]}x"   
                                          # SI notre nombre est positif : afficher +
    if polynome[2] >= 0:                  # SINON ne rien faire: le "-" sera afficher automatiquement
        affichage += f" + {polynome[2]}"  # Autrement nous obtiendrions 2x² +- 1x +- 4
    else:                                 #
        affichage += f" {polynome[2]}"

    return affichage


