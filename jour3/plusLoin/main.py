def reverse(word):
    reversedWord = ""
    for i in range(len(word) -1, -1, -1):
        reversedWord += word[i]
    print(f"Mot à l'envers : {reversedWord}")

reverse("ressaser")
reverse("elu par cette crapule")