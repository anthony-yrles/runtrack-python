L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

minimum = L[0]

maximum = L[0]

for i in L:
    if i < minimum:
        minimum = i
    elif i > maximum:
        maximum = i

print(f"Le minimum est {minimum} et le maximum est {maximum}")