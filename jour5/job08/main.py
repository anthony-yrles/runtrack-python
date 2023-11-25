L = notes = [85.73, 92.55, 60.24, 78.88, 45.72, 88.11, 70.35, 95.59, 33.26, 72.61, 88.87, 67.13, 50.52, 95.92, 40.67, 78.54, 90.45, 55.49, 81.58, 62.97]

def my_sort(L) -> list:

    # Afin de pouvoir compter le nombre de tour de boucle on initialise un compteur à 0
    turn_number = 0

    # Il faut d'abord boucler dans la liste
    for i in range(len(L)):

        # Puis dans chaque itération de la liste
        for j in range(0, len(L) - i - 1):

            # Ici nous allons vérifier si ce que contient l iteration est supérieur a ce que contiens l iteration suivante
            if L[j] > L[j + 1]:

                # Si oui alors on échange les places des deux
                L[j], L[j + 1] = L[j + 1], L[j]

            # A chaque tour de boucle j on augmente le nombre de tour
            turn_number += 1
    
    # A la fin on print le nombre de tours et on retourn la liste triée
    print(f"Nombre total de coups necessaire pour trier la liste : {turn_number}")
    return(L)

L_tri = my_sort(L)
print(f"Liste triée : {L_tri}")