typev=str(input("Quel type de viande ? 1: boeuf, 2: agneau, 3: canard\n"))
cuisson=str(input("Quel type de cuisson ? 1: bleu/rosé, 2: saignant, 3: à point\n"))
poids=float(input("Quel poids en grammes ?\n"))
boeufbleu=10/500
boeufpoint=17/500
boeufcuit=25/500
agneaubleu=15/400
agneaupoint=25/400
agneaucuit=40/400
canardrosé=20/450
canardpoint=25/450
canardcuit=30/450

match typev:
    case "1":
        match cuisson:
            case "1":
                temps=str(poids*boeufbleu)
            case "2":
                temps = str(poids * boeufpoint)
            case "3":
                temps = str(poids * boeufcuit)
    case "2":
        match cuisson:
            case "1":
                temps=str(poids*agneaubleu)
            case "2":
                temps = str(poids * agneaupoint)
            case "3":
                temps = str(poids * agneaucuit)
    case "3":
        match cuisson:
            case "1":
                temps=str(poids*canardrosé)
            case "2":
                temps = str(poids * canardpoint)
            case "3":
                temps = str(poids * canardcuit)

temps=round(float(temps))
temps=str(temps)
réponse=("Le temps de cuisson est de " + temps +" minutes")
print(réponse)
                
