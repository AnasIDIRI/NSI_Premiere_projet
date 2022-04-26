#!/usr/bin/env python3

# Import de quelques librairies externes 
from sys import platform
from os import system as cmd
from random import randint
from datetime import datetime
from termcolor import colored

# Import de nos autres fichiers :
import polynome
import lineaire
import affine
import carre

# Fonctions :

def clear():
    
    """Clear la command line en prenant en compte l'os utilisé """
    
    if platform == "win32":
        cmd("cls")
    else:
        cmd("clear")

def VoidAfficher(question, result ,reponse, var):

    """
    Afficher la question, la réponse de la question et la réponse de l'utilisateur
    """

    # CRLF
    print("\r\n")

    # Status :
    if var == True:

        # Quand une réponse est juste on affiche Bonne réponse en vert
        print(colored("Bonne réponse !", 'green'))

    elif var == False:
        # Sinon on affiche en rouge
        print(colored("Mauvaise réponse !", "red"))
    print("")

    # Question / Réponse
    print(f"Question : {question}")
    print(f"Réponse : {result}")
        
    # Réponse Utilisateur 
    print(f"Votre réponse : {reponse}")
        
        


# Affichons le texte informatif 
print("""
Quizz de mathématiques 
4 types de question peuvent vous être posé :

    1  :  polynomes
    2  :  affine                
    3  :  linéaire
    4  :  fonction carré

Bonne chance !\r\n""")

input("Pour continuer, tapez entrer ...")

# enregitsrons l'heure à laquelle le quizz a commencé
debut = datetime.now()

# Initialisation du nombre de bonnes/mauvaises rep
nbTrue, nbFalse = 0,0

# Effacons l'écran
clear()


for i in range(0,10): # Il y aura 10 questions dans le quizz, donc une boule allant jusqu'à 10

    get_int = False # Pour la gestion d erreur
    question = randint(1,4)  #  On tire un nombre au hasard pour la question qui sera posée


# 

# ---------------------------------------- Polynôme ----------------------------------------------------------------------------------

# Question sur les polynome

    if question==1: 


        """
        Grâce au module polynome, on crée un polynome en s'assurant qu'il ai une/des réponse(s) dans R
        On calcul son delat et sa/ses racine(s)
        
        """

        polynom = polynome.GenerationPolynome()     
        delta  = polynome.CalculerDelta(polynom)    
        result = polynome.CalculerRacines(polynom)  


        # On demande à l'utilisateur 

        print(f"Calculez les solutions dans R de : {polynome.Afficher(polynom)}") # A l'aide de la fonction affichage
                                                                                      # on affiche proprement notre polynome
        
        print("utilisez des \".\" et non des \",\" et séparez vos racines par un espace \n") 


        # Basique boucle de gestion d'erreur
        get_int = False 
        rcs = "On force l'entrée dans la boucle"

        while get_int is False and rcs != "" :     # On s'assure que la ValueError ne soit pas causé 
                                                   # par un utilisateur n'ayant rien entré

            rcs = input("Entrez le/les racines : ")
        
            # On split la réponse pour (dans le cas ou il y a 2 racines) créer un tableau
            # contenant les racines

            rcs = rcs.split()

            try:
                for i in range(len(rcs)):
                    rcs[i] = float(rcs[i]) 
                get_int = True 

            except ValueError:
                print("Un int était attendu !")
                get_int = False


        if rcs == "":
            
            # Si l'utilisateur n'entre rien, c'est faux
            
            nbFalse += 1
            VoidAfficher(polynome.Afficher(polynom), result, rcs, False)
  


        elif len(result)==2 and len(rcs)==2: # Il y a 2 racines et l'utilisateur en a donné 2 :
            
            if rcs[0] == result[0] and rcs[1] == result[1] or rcs[0] == result[1] and rcs[1] == result[0]: 

            # On test bien toute le spossibilité : les racines doivent pouvoir être donné dans l'ordre que l'utilisateur souhaite 
                nbTrue+=1            
                VoidAfficher(polynome.Afficher(polynom), result, False)
            
            else:
                # Il y a 2 racines, l'utilisateur en a donné 2 mais elles sont fausses
                nbFalse+=1
                VoidAfficher(polynome.Afficher(polynom), result, False)

        elif len(result)==1 and len(rcs)==1: # Il y a 1 racine, l'utilisateur en a donné 1

                if result[0] == rcs[0]:
                    nbTrue += 1
                    VoidAfficher(polynome.Afficher(polynom), result, rcs, True)
                else:
                    nbFalse += 1
                    VoidAfficher(polynome.Afficher(polynom), result, rcs, False)

        else:
            # Trop/Pas assez de racines donnée par l'utilisateur, c'est donc faux
            nbFalse+=1
            VoidAfficher(polynome.Afficher(polynom), result, rcs, False)

        

        

# -----------------------------------------------------------------------------------------------------------------------------------
# Question sur les fonctions affines :


    elif question == 2:

        """
        On génère une fonction affine et son résultat
        """

        a,b = affine.générer_affine()
        solution = affine.rs_affine(a,b) 
        affine_equ = f"{a}x {affine.afficher(b)}"

        # Demande a l'utilisateur
        
        print(f"Calculez la solution de : {affine_equ} = 0") 
        print("""utilisez des "." et non des "," \n""") 


        get_int = False
        rs = "Un do-while en python3"
        
        while get_int is False and rs != "" :  # Encore une fois, on s'assure que la value error n'est pas causé par 
                                               # un string vide

            rs = input("Veuillez entrer votre réponse arrondi au centième : ")

            try:
                rs = float(rs)
                get_int = True
            except ValueError:
                print("Vous devez entrer un nombre")
                get_int = False

            # N'est pas un nombre


        if rs == "":
            nbFalse += 1
            VoidAfficher(affine_equ, solution, rs, True) 
        
        elif rs == solution:
            nbTrue+=1
            VoidAfficher(affine_equ, solution, rs, True)
            
        else:
            nbFalse+=1
            VoidAfficher(affine_equ, solution, rs, False)

        
        

# -----------------------------------------------------------------------------------------------------------------------------------
# Question sur les fonctions linéaire :

    elif question == 3:

        linéaire,question = lineaire.linéaireGen()
        rsp_linéaire = lineaire.Reponse(linéaire, question)
        equati = f"{linéaire}x = {question}"

        print(f"Résoudre : {equati} (arrondi au centième) ")
        print("""utilisez des "." et non des "," \n""") 


        get_int = False
        rep = "quelquechose"
        
        while get_int is False and rep != "":

            rep = input(" : ")

            try:
                rep = float(rep)
                get_int = True
            except ValueError:
                print("Vous devez entrer un int !")
                get_int = False

        if rep == "": # si l'utilisateur n'entre rien c'est qu'il considère qu'il n y a pas de solution, ce qui est faux
            nbFalse += 1
            VoidAfficher(equati, rsp_linéaire, rep, False)

        elif rep == rsp_linéaire: # bonne réponse
            nbTrue += 1
            VoidAfficher(equati, rsp_linéaire, rep, True)       
        else: # Mauvaise reponse
            nbFalse += 1
            VoidAfficher(equati, rsp_linéaire, rep, False)





# -----------------------------------------------------------------------------------------------------------------------------------
# Question sur les fonctions carré :

    elif question == 4:

        # Generer une question
        EquationCarré = carre.Generer()
        rsps = carre.Calculer(EquationCarré)

        # Prompt user
        print(f"Résoudre : x² = {EquationCarré} (arrondi au centième) ")
        print("""utilisez des "." et non des "," \n""") 


        # Gestion d'erreur

        get_int = False
        rep_carré = "ceci"

        while get_int is False and rep_carré != "":

            rep_carré = input(" : ")

            try:
                rep_carré=float(rep_carré)
                get_int = True

            except ValueError:
                get_int = False
                print("Vous devez entrer un nombre !")

            
            
        if rep_carré == "":    
            nbFalse += 1
            VoidAfficher(f"x² = {EquationCarré}", rsps, rep_carré, False)

        elif rep_carré == rsps:
            nbTrue += 1 
            VoidAfficher(f"x² = {EquationCarré}", rsps, rep_carré, True)    
        else:
            nbFalse += 1
            VoidAfficher(f"x² = {EquationCarré}", rsps, rep_carré, False)


# -----------------------------------------------------------------------------------------------------------------------------------
# esthétique :

    input("\r\n \r\ntapez entrer ...")
    # On clear a la fin de chaque question / réponse
    clear()


# Enregistrons l'heure actuelle 
fin = datetime.now()


# Calculer une note sur 20
nbTruesur20 = nbTrue * 2


# Affichage

print(f"""
Commencé à     :   {debut.strftime("%H")}h {debut.strftime("%M")}m {debut.strftime("%S")}s
État           :   Terminé
Terminé à      :   {fin.strftime("%H")}h {fin.strftime("%M")}m {fin.strftime("%S")}s
Note           :   {nbTruesur20} sur 20 ({nbTruesur20*5}%)
""")
