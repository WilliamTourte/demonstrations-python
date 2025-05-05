stock = {}
for piece in (200, 100, 50, 20, 10, 5):
    stock[piece] = 1


cafe = float(60)
solde = float(0)

def afficher_monnaie(m):
    d = "€"
    affichage = "%.2f%s" % (m/100, d) # Permet d'afficher la monnaie
    return affichage

print("Pièces acceptées : 2€ 1€ 0.50€ 0.20€ 0.10€ 0.05€")
print("Café : ", afficher_monnaie(cafe))

while solde < cafe:
    une_piece = input("Introduire une pièce : ")
    une_piece=une_piece.replace(",",".")          # remplacer virgule par point pour convertir en float
    une_piece=int(100 * float(une_piece)) # Valeur en centimes d'euro
    if une_piece in (200, 100, 50, 20, 10, 5):
        stock[une_piece] += 1
        solde += une_piece
    else:
        print("Pièce non acceptée")
print("Total inséré :")
afficher_monnaie(solde)


solde -= cafe
if solde >= 0:
    print("Voici votre café")

    for piece in stock.keys():
        while solde > 0  and stock[piece] > 0 and piece <= solde:
            print("Pièce rendue : ", afficher_monnaie(piece))
            solde -= piece
            print("Reste à rendre : ", afficher_monnaie(solde))
            stock[piece] -= 1

        if piece > solde:
                continue
        else :
            continue
else:
    print("Solde insuffisant")
