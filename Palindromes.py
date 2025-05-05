'''Definition palindrome : dernière lettre = 1ère lettre'''
'''-1 : 0
-2 : 1
-3 : 2
si -2 IS 1 : break
BOB ou ELLE'''
### enlève accents chaine str  ###
def sansaccent(mot) :


    tablo = { 'éèêẽ' : 'e'
            , 'ç'    : 'c'
            , 'àâã'  : 'a'
            , 'ù'    : 'u'
            }
    mot_sans_accents = ''
    for i in mot:
        for key in tablo:
            if i in key:
                i = tablo[key];
                break
        mot_sans_accents += i
        
    return mot_sans_accents

'''input=input("Entrez un mot")'''
input="Tu l'as trop écrasé, César, ce Port-Salut"
mot=sansaccent(input)
mot=mot.replace(" ","")
mot=mot.replace(",","")
mot=mot.replace("'","")
mot=mot.replace("-","")
mot=mot.strip()
mot=mot.upper()

moitie=len(mot)/2
print(moitie)
Pareil = True
moitieatteinte = False
i=0

while moitieatteinte == False:
    for lettre in mot:

        print("Index",mot[mot.index(lettre)], i)
        i+=1
        '''pas besoin de vérifier au delà de la moitié'''
        if i >= moitie:
            moitieatteinte = True
            break

        '''utilisation de la tilde pour trouver l'inverse de l'index d'une lettre'''
        if mot[mot.index(lettre)] != mot[~mot.index(lettre)]:
            Pareil = False

if Pareil == True:
    print(f"{input} est un palindrome")
else:
    print(f"{input} n'est pas un palindrome")
