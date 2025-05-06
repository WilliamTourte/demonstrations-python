numero=1
montant=0
liste={ }
while numero != 0:
    numero=int(input("Saisissez le numéro du chèque\n"))
    if numero == 0:
        break
    montant=float(input("Saisissez le montant du chèque\n"))
    liste[numero]=montant

nb_cheques=len(liste.keys())
print("Nombre de chèques :")
print(nb_cheques)

somme=sum(liste.values())
print("Montant total des chèques")
print(somme)

if nb_cheques != 0:
    moyenne=somme/nb_cheques
    print("Moyenne des montants")
    print(moyenne)

"""Le nombre de chèques dont le montant est inférieur à 200€, avec le total de leurs montants."""
nbfaible = 0
sommefaible = 0
nbfort = 0
sommeforte = 0

for cheque in liste.values():
    if cheque < 200:
        nbfaible = nbfaible + 1
        sommefaible = sommefaible + cheque
    if cheque >= 200:
        nbfort = nbfort + 1
        sommeforte = sommeforte + cheque

print(f"Il y a {nbfaible} chèque(s) inférieurs à 200e pour un montant total de {sommefaible}")
print(f"Il y a {nbfort} chèque(s) supérieurs ou égaux à 200e pour un montant total de {sommeforte}")

mini=min(liste.values())
nummini = [key for key, val in liste.items() if val == mini]
print(f"Le numéro du plus petit chèque est : {nummini} et son montant est : {mini}")

maxi=max(liste.values())
nummaxi = [key for key, val in liste.items() if val == maxi]
print(f"Le numéro du plus petit chèque est : {nummaxi} et son montant est : {maxi}")


#test pour changement branche
:
