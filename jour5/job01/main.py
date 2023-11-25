def return_name (prenom):
    print(f"Hello {prenom} !")

prenom = input("Quel est votre prénom ? ")

if any(char in prenom for char in ";,&><"):#[';', '&', '|', '>', '<']):
    print("Prénom invalide.")
else:
    return_name(prenom)