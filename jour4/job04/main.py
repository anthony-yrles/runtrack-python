# Ajouter

def returnFruit(nouveau):
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, nouveau)
    print(fruits)

returnFruit("Mangue")

# Remplacer

def returnFruit(nouveau):
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits[2] = nouveau
    print(fruits)

returnFruit("Mangue")