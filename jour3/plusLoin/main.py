def reverse(word):
    for i in range(len(word.replace(" ","")) -1, -1, -2):
        reversedWord += word.replace(" ","")[i] + " "
        print(f"Mot à l'envers : {reversedWord}")

reverse("nikana")