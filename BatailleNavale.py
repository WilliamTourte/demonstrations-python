Touche=False

#Création de plateau de 4 cases
def crea_plateau() :
    plateau=dict()
    plateau[1]={1:"?",2:"?",3:"?",4:"?"}
    plateau[2]={1:"?",2:"?",3:"?",4:"?"}
    plateau[3]={1:"?",2:"?",3:"?",4:"?"}
    plateau[4]={1:"?",2:"?",3:"?",4:"?"}
    return plateau

#Affichage plateau de 4*4 cases
def afficher() :
    for i in range(1,5):
            affichage=plateau[i].values()
            print(*affichage)
#############################################################################
plateau=crea_plateau()

#Mise en place d'un bateau en ligne 2, colonne 3
coord_bateau=(2,3)

afficher()

#Recueil coordonnées missile
def demande() :
    lignetir=int(input("Entrez la ligne du tir, entre 1 et 4\n"))
    colonnetir=int(input("Entrez la colonne du tir, entre 1 et 4\n"))
    return lignetir, colonnetir

#Tir sur grille
while Touche == False:
    tir=demande()
    if tir == coord_bateau:
        plateau[tir[0]][tir[1]] = "X"
        print("Touché")
        afficher()
        Touche=True
    else:
        plateau[tir[0]][tir[1]] = "~"
        afficher()
