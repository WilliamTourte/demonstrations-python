from random import randrange # import de la méthode randrange(debut, fin_non_inclue)
nb_aleatoire = lambda limite=99999: randrange(-1 * limite, limite + 1) # nb_aleatoire()



def max (nb1, nb2):
    if nb1 > nb2:
        return nb1
    else:
        return nb2

'''Écrire une seconde fonction prenant également deux valeurs numériques en paramètre, mais qui retourne une des valeurs suivantes :

0 : si les deux valeurs sont égales
1 : si la première valeur est la plus grande
-1 : sinon (la seconde valeur est la plus grande)'''
def compare(nb1, nb2):
    if nb1 == nb2:
        return 0
    if nb1 > nb2:
        return 1
    else:
        return -1


nb1=input("Saisissez un premier nombre")
nb2=input("Saisissez un deuxième nombre")

def test(nb1,nb2):
    print("Test max")
    print(max(nb1, nb2))
    print("Test compare")
    print(compare(nb1,nb2))

test(nb1,nb2)
