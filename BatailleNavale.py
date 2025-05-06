import string
from random import randrange

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


lignebateau=randrange(1,taille)
colonnebateau=randrange(1,taille)
print("lignebateau = ", lignebateau, "colonnebateau = ", colonnebateau)
coord_bateau=(lignebateau,colonnebateau)

afficher()

#Recueil coordonnées missile
def demande() :
    alphabet = string.ascii_uppercase


    coordotir = str(input("Entrez coordonnées du tir, ex : C2\n"))
    lettre = coordotir[0]
    chiffre = coordotir[1]

    lignetir=int(alphabet.index(lettre)+1)
    print("lignetir", lignetir)

    colonnetir=int(chiffre)
    print("colonnetir", colonnetir)
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
