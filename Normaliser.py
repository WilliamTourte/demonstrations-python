def normaliser_chaine_de_caracteres(chaine_de_caracteres):
    """
    Normalise une chaîne de caractères en supprimant les accents, les ligatures, les espaces et les caractères spéciaux
    :param chaine_de_caracteres: La chaîne de caractères à normaliser
    :return: La chaîne de caractères normalisée
    """
    chaine_normalisee = str(chaine_de_caracteres).strip().lower()
    transformation = str.maketrans(
        "àäâéèëêïîöôùüûÿŷç", # Caractère à modifier
        "aaaeeeeiioouuuyyc", # Caractères à remplacer
        "(&#~-_.…?,;:!) '’\"\t\n") # Caractères à supprimer (à compléter en fonction)
    chaine_normalisee = chaine_normalisee.translate(transformation)
    ligatures = str.maketrans({'Æ': "Ae", 'æ': "ae", 'Œ': "Oe", 'œ': "oe"})
    chaine_normalisee = chaine_normalisee.translate(ligatures)
    return chaine_normalisee

print(normaliser_chaine_de_caracteres("çè'-è('_è('y_è('-('è_-y('('"""))

## git tu me vois ?