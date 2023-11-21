chaine = "abcdefghijklmnopqrstuvwxyz" * 10

pyramide = ""
for i in range(0, len(chaine)):
    pyramide += chaine[i]
    if i % 2 == 0:
        pyra = pyramide
        print(pyra)