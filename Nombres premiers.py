''' un nombre premier est un nombre qui a exactement 2 diviseurs distincts entiers et positifs'''
liste = []
listepremiers = []
limite=1000
for i in range(limite+1):
    liste.append(i)

for i in liste:
    listetest = []
    ''' vérifier par quoi on peut diviser i.'''
    for j in range(1,i+1):
        test=i/j

        if test.is_integer()==True and i != j:
            '''si j divise i, on l'ajoute à la liste des diviseurs'''
            listetest.append(j)
            if len(listetest)==2:
                break
    if len(listetest) == 1:
        '''si la liste des diviseurs n'a que 2 elements à la fin de la boucle, on rajoute i à la liste'''
        listepremiers.append(i)

print(f"La liste des nombres premiers jusqu'à {limite} est :")
print(*listepremiers, sep='\n')
