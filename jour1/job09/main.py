nom = "manga"
prix_unitaire = 5
quantite = 35

print("Nous avons " + str(quantite) + " " + (nom) + " au prix de " + str(prix_unitaire) + " €")

quantite += 28

print("Nous avons " + str(quantite) + " " + (nom) + " au prix de " + str(prix_unitaire) + " €")

quantite_desire = input("Combien de " + (nom) + " voulez-vous acheter ? ")
quantite_int = int(quantite_desire)

quantite = quantite - quantite_int

prix_unitaire *= 1.1

print("Nous avons " + str(quantite) + " " + (nom) + " au prix de " + str(prix_unitaire) + " €")
print("Nous avons {} {} au prix de {} €".format(quantite, nom, prix_unitaire))
print(f"Nous avons {quantite} {nom} au prix de {prix_unitaire} €")