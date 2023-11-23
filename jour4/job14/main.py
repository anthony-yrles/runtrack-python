def my_long_word(chiffre, phrase):
    newphrase = []
    mot = ""
    temp_list = []
    lettre = 0
    phrasebis = ""

    for i in phrase:
        if i != " " and i != ",":
            mot = mot + i
            lettre += 1
        else:
            if lettre > chiffre:
                temp_list += [mot]
            mot = ""
            lettre = 0

    if lettre > chiffre:
        temp_list += [mot]

    newphrase += temp_list

    for j in newphrase:
        phrasebis = phrasebis + j + " "

    return phrasebis


test = my_long_word(
    3,
    "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance",
)
print(test)
