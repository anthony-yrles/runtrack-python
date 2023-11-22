def evenOrOdd(number):
    if isinstance(number, int) and number > 0:
        if number % 2 == 0:
            print("C'est un nombre pair")
        else:
            print("C'est un nombre impair")
    else:
        print("Ce n'est pas un entier positif")


evenOrOdd(574)
evenOrOdd(1877)
evenOrOdd(-422)
evenOrOdd(765.54)
