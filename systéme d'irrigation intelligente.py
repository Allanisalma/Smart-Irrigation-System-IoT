seuil = 40
print("Systéme d'irrigation intelligente")
humidite = float(input("Entrez le pourcentage d'humidité du sol : "))
if humidite < 0 or humidite > 100:
    print("Erreur: le pourcentage d'humidité doit être compris entre 0 et 100.")
elif humidite < seuil:
    print("Le sol est sec. Activation du système d'irrigation.")
else:
    print("Le sol est suffisamment humide.")