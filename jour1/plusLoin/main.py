chaine = input("Entrez une chaîne de caractères : ")

if 'e' in chaine:
    nombre_occurrences = chaine.count('e')
    print("La chaîne contient le caractère 'e'.")
    print("Nombre d'occurrences du caractère 'e' dans la chaîne :", nombre_occurrences)
else:
    print("La chaîne ne contient pas le caractère 'e'.")
