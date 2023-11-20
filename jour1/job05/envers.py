import random

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet_inverse = alphabet[::-1]
print(alphabet_inverse)

# Boulot supplementaire demandé par Alicia

# Première mouture

# Suppression des espaces
alphabet_sans_espace = alphabet.replace(" ","")

# Création d'un tableau
abc = list(alphabet_sans_espace)

# Taille du tableau
abc_nombre = len(abc)

# Nouveau tableau vide
alphabet_envers = []

# Remplissage du tableau a l'envers
for i in range(abc_nombre - 1, -1, -1):
    alphabet_envers.append(abc[i])

# Transformation du tableau en une variable
alphabet_envers_str = ''.join(alphabet_envers)

# Ajout des espaces et print
alphabet_envers_str = alphabet_envers_str.replace(""," ")
print("Alphabet envers :", alphabet_envers_str)


# Deuxieme version simplifié avec une variable au lieu d'un tableau et l'ajout automatique des espaces
alphabet_envers = ""
for i in range(abc_nombre -1, -1, -1):
    alphabet_envers += abc[i] + " "
print("Alphabet envers :", alphabet_envers)

# Formule la plus courte possible avec calcul de la taille directement dans la boucle + gap de 2 a chaque itération de la boucle

alphabet_envers = ""
for i in range(len(alphabet.replace(" ","")) -1, -1, -2):
    alphabet_envers += alphabet.replace(" ","")[i] + " "
print("Alphabet envers :", alphabet_envers)

# Boulot supplementaire demandé par Celine

# On commence par mélanger la liste

# Commencons par utiliser le .shuffle pour mélanger la liste

random.shuffle(abc)
print("Liste random :", abc)

# Création d'un tableau de tuple avec chaque lettre et sa valeur ASCII grace a ord

abc_ascii = [(c, ord(c)) for c in abc]

# Fonction qui boucle à partir de la fin et qui vérifie si la valeur ASCII a gauche est supérieur, si c'est le cas échange les deux valeurs

def tri_bulles(abc_ascii):
    n = len(abc_ascii)
    for i in range(n):
        trie = True
        for j in range(0, n-i-1):
            if abc_ascii[j] > abc_ascii[j+1]:
                abc_ascii[j], abc_ascii[j+1] = abc_ascii[j+1], abc_ascii[j]
                trie = False
        if trie:
            break

# Appel de la fonction

tri_bulles(abc_ascii)

# Création d'une variable qui ne garde que la valeur de l'emplacement 0 du tableau de Tuple

abc_trie = ' '.join([t[0] for t in abc_ascii])
print("Alphabet trié sans les valeurs ASCII :", abc_trie)
