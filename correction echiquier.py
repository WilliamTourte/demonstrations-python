# TP05 - Max et Compare
print("____Echiquier de Sissa v2____")
print("""La légende se situe 3 000 ans av. J.C. :
Le roi Belkib (Indes) promit une récompense fabuleuse à qui lui proposerait une distraction qui le satisferait.
Lorsque le sage Sissa, fils du Brahmine Dahir, lui présenta le jeu d'échecs,
 le souverain demanda à Sissa ce que celui-ci souhaitait en échange de ce cadeau extraordinaire.
Sissa demanda au prince de déposer un grain de riz sur la première case, deux sur la deuxième,
 quatre sur la troisième, et ainsi de suite pour remplir l'échiquier en doublant la quantité de grain à chaque case.
Le prince accorda immédiatement cette récompense sans se douter de ce qui allait suivre.
Son conseiller lui expliqua qu'il venait de précipiter le royaume dans la ruine…""")
input("______________________________________________________________Appuyer sur la touche 'Entrée' pour continuer")
def echiquier_Sissa(nb_ligne=8, nb_colonne=8):
    # Initialisation de l'échiquier
    nb_grains_case = 1
    nb_grains_echiquier = nb_grains_case
    print("Echiquier de", nb_colonne, "par", nb_ligne,":")
    for ligne in range(nb_ligne):
        for colonne in range(nb_colonne):
            print(" • Case n°", ligne + 1, "x", colonne + 1, ": Nb. Grains de riz =", nb_grains_case, "total : ", nb_grains_echiquier)
            nb_grains_case *= 2
            print(ligne,colonne)
            '''Pour ne pas doubler la dernièree ligne'''
            if ligne==dimension-1 and colonne==dimension-1:
                break
            else:
                nb_grains_echiquier += nb_grains_case

        print("- - - - - - - - - - - - - - - - - - Changement de ligne - - - - - - - - - - - - - - - - - -")


    return nb_grains_echiquier
dimension = int(input("Indiquer la dimension de l'échiquier (par exemple entre 8 et 64) : "))
print("=> Il y a au total", echiquier_Sissa(dimension, dimension), "grains de riz sur l'échiquier de", dimension, "par", dimension, "!")
print("_________________________Fin du programme")