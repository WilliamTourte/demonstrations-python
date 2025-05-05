
from tabulate import tabulate
riz=1
case=1
total=0
lignesnom=range(8)
colonnesnom=range(8)
'''Construction de l'échiquier : liste dans liste'''

echiquier= [ [ [] for i in lignesnom] for i in colonnesnom]


for ligne in lignesnom:
    for caseligne in colonnesnom:

        echiquier[ligne][caseligne]=riz
        total=total+riz
        riz = riz*2

print(tabulate(echiquier, tablefmt='psql'))
print("Total : ",total)


