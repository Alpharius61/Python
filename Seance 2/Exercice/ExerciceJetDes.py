# Simuler un jeu de dés
# Demander combien de joueur
# Stocker leur noms 
# Pour chaque joueur, tirer 2D6 et additionner le résultat ( le(s) gagnant(s) a/ont le plus haut score )
# Afficher le(s) gagnant avec leur score
# Proposer de recommencer le jeu (si oui, on recommence, si non dire "au revoir")

# coding in utf-8

# Besoin :
# module random, boucle (2 for et 1 while), une liste

import random

def main() :
    playAgain = "Yes"
    while playAgain.upper() != "N" and playAgain.upper() != "NO" :
        jetDés()
        playAgain = input("Voulez-vous rejouer (Yes/No) ? \n")
    
    print("Au revoir")
    



def jetDés() :
    score = []
    nomDesJoueurs = []
    result = []
    # Demande du nombre de joueur 
    while True :
        try :
            nbJoueur = int(input("Quel est le nombre de joueur ? \n"))
            break
        except :
            print("Il faut rentrer un nombre (1,2,3 c'est machin là en gros)")
    
    # Demande du nombre de face du dés
    while True :
        try :
            diceFaces = int(input("Quel est le nombre de face du dés ? \n"))
            break
        except :
            print("Il faut rentrer un nombre (1,2,3 c'est machin là en gros)")

    # Demande du nombre de tirage du dés
    while True :
        try :
            numberOfTry = int(input("Combien de tirage de dés ? \n"))
            break
        except :
            print("Il faut rentrer un nombre (1,2,3 c'est machin là en gros)")

    # Création de la liste de joueur
    for i in range (nbJoueur) :
        joueurs = input(f"Nom du joueur {i+1} : ")
        nomDesJoueurs.append(joueurs)
    
    # Jet de dés pour chaque joueur : le premier for permet d 'initialiser le second le nombre de fois
    #  qu'il y a de joueur.
    #  Le second for permet de tirer les dés le nombre de fois qu'il y a de tirage.
    for i in range (len(nomDesJoueurs)) : 
        resultTemp = [] 
        scoreTemp = []
        for t in range (numberOfTry) :
            fDice = random.randint(1,diceFaces)
            sDice = random.randint(1,diceFaces)
            resultTemp.append(fDice + sDice)
            scoreTemp = sum(resultTemp)                  
           
        score.append(scoreTemp)
          
         


    winnersList = []
    bestScore = 0

    # Triage des résultats de jet de dés et création de la liste du/des gagnant(e)(s) 
    # ainsi que stockage du score gagnant 
    for index in range (len(nomDesJoueurs)) :
        if score[index] > bestScore :
            bestScore = score[index]
            winnersList = []
            winnersList.append(nomDesJoueurs[index]) 
        
        elif score[index] == bestScore :
            winnersList.append(nomDesJoueurs[index]) 
    
    
    # Affichage du/des gagnant(e)(s) ainsi que du score
    if len(winnersList) > 1 :
        print(f"Les gagnant sont {', '.join(winnersList)} avec {bestScore}. ")
    else :
        print (f"Le gagnant est {winnersList[0]} avec {bestScore}.\n")
    




if __name__ == "__main__" :
    main()