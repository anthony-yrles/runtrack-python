def calcule(num1: int, operator: str, num2: int):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division par zéro impossible")
            return None
        else:
            return num1 / num2
    elif operator == "%":
        if num2 == 0:
            print("Modulo par zéro impossible")
            return None
        else:
            return num1 % num2
    else:
        print("Opération non reconnue")
        return None

resultat_addition = calcule(5, "+", 3)
print("Addition:", resultat_addition)

resultat_soustraction = calcule(10, "-", 4)
print("Soustraction:", resultat_soustraction)

resultat_multiplication = calcule(6, "*", 7)
print("Multiplication:", resultat_multiplication)

resultat_division_zero = calcule(8, "/", 0)
print("Division par zéro:", resultat_division_zero)

resultat_division = calcule(15, "/", 3)
print("Division:", resultat_division)

resultat_modulo_zero = calcule(10, "%", 0)
print("Modulo par zéro:", resultat_modulo_zero)

resultat_modulo = calcule(17, "%", 5)
print("Modulo:", resultat_modulo)
