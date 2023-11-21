while True:
    multiple = input("Quelle table de multiplication voulez-vous? ")
    if multiple.isdigit():
        multiple_int = int(multiple)
        
        if multiple_int > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    else:
        print("Veuillez entrer un nombre entier valide.")

for i in range(1, multiple_int + 1):
    print(f"Table de multiplication de {i}: ")
    for j in range(1, 11):
        print(f"{j} x {i} = {j * i}")
    i += 1
