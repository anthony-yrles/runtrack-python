a = int(input("Taille de a: "))
b = int(input("Taille de b: "))
c = int(input("Taille de c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Merci de mettre des valeurs supérieur ou égal à 0")
    a = int(input("Taille de a: "))
    b = int(input("Taille de b: "))
    c = int(input("Taille de c: "))

if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Il s'agit d'un triangle rectangle")
    if a == b != c or a == c !=b or c == b != a:
        print("Il s'agit d'un triangle isocèle")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 and a == b != c or a == c != b or c == b != a:
        print("Il s'agit d'un triangle rectangle et isocèle")
    if a == b and a == c:
        print("Il s'agit d'un triangle equilatéral")
    print("Il s'agit bien d'un triangle")
else:
    print("Les valeurs données ne permettent pas de former un triangle")