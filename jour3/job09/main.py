def moyenne(a, b, c):
    return int((a + b + c) / 3)

noteA = int(input("Quel est ta note en math? :"))
noteB = int(input("Quel est ta note en français? :"))
noteC = int(input("Quel est ta note en histoire? :"))

if noteA > 20 or noteA < 0:
    notaA = int(input("Note A non valide: "))
if noteB > 20 or noteB < 0:
    notaB = int(input("Note B non valide: "))
if noteC > 20 or noteC < 0:
    notaC = int(input("Note C non valide: "))

moyenne_etudiant = moyenne(noteA, noteB, noteC)
if moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
elif moyenne_etudiant <= 10:
    print("Élève moyen")
elif moyenne_etudiant <= 14:
    print("Bon élève")
else:
    print("Très bon élève")
