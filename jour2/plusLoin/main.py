a = int(input("Taille de a: "))
b = int(input("Taille de b: "))
c = int(input("Taille de c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Triangle impossible mettre des valeurs supérieur ou égal a 0")
else:
    ("Il s'agit bien d'un triangle")

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Il s'agit d'un triangle rectangle")
        
if a == b or a == c or c == b:
    print("Il s'agit d'un triangle isocèle")

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 and a == b or a == c or c == b:
    print("Il s'agit d'un triangle rectangle isocèle")
    
if a == b and a == c:
    print("Il s'agit d'un triangle equilatéral")