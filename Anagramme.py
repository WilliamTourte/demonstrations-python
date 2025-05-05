def sanitize(mot):
    tablo = {'éèêẽ': 'e'
        , 'ç': 'c'
        , 'àâã': 'a'
        , 'ù': 'u'
             }
    mot_sans_accents = ''
    for i in mot:
        for key in tablo:
            if i in key:
                i = tablo[key];
                break
        mot_sans_accents += i

    mot = mot_sans_accents.replace(" ", "")
    mot = mot.replace(",", "")
    mot = mot.replace("'", "")
    mot = mot.replace("-", "")
    mot = mot.strip()
    mot = mot.upper()
    return mot
premiermot="Alain Chabat"
deuxièmemot="Habita Canal"
mot1=sanitize(premiermot)
mot2=sanitize(deuxièmemot)
copie=list(mot2)
anagram=True

for lettre in mot1:
    '''si la lettre n'est pas dans le mot 2, ça ne peut pas être des anagrammes'''
    if lettre not in copie:
        print(lettre, "pas dans ", copie)
        anagram = False
        break
    else:
        print(lettre, "est dans ", copie)
        copie.remove(lettre)

'''si "not copie", cela veut dire que copie est vide et donc que toutes les lettres correspondent '''
if anagram==True and not copie:
    print(f"{premiermot} et {deuxièmemot} sont des anagrammes")
else:
    print(f"{premiermot} et {deuxièmemot} ne sont pas des anagrammes")