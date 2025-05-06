Touche=False
taille=int(input("Rentrez la taille voulue du plateau en nombre de cases\n"))+1

#Création de plateau de [taille] cases
def crea_plateau() :

    plateau=dict()
    for i in range(1,taille) :
        plateau[i]=dict()
        for j in range(1,taille) :
            plateau[i][j]="?"
    return plateau

#Affichage plateau de 4*4 cases
def afficher() :
    for i in range(1,taille):
            affichage=plateau[i].values()
            print(*affichage)
#############################################################################
plateau=crea_plateau()

#Mise en place d'un bateau aléatoire
from random import randrange

lignebateau=randrange(1,taille)
colonnebateau=randrange(1,taille)
print("lignebateau = ", lignebateau, "colonnebateau = ", colonnebateau)
coord_bateau=(lignebateau,colonnebateau)

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
