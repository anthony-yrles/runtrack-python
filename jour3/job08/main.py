def seasonFruit(type, saison):
    if type.lower() == "fruits":
        if saison.lower() == "hiver":
            print("orange, mandarine et kiwi")
        elif saison.lower() == "ete":
            print("Poire, fraise, cassis")
        else:
            print("biiiiipppp")
    if type.lower() == "legume":
        if saison.lower() == "hiver":
            print("carotte, topinambour, endive")
        elif saison.lower() == "ete":
            print("artichaut, aubergine, navet")
        else:
            print("biiiiipppp")


seasonFruit("Fruits", "Hiver")

seasonFruit("fruits", "Ete")

seasonFruit("Legume", "hiver")

seasonFruit("legume", "ete")

seasonFruit("Poisson", "ete")

seasonFruit("Fruits", "Automne")

