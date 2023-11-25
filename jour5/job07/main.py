notes = [85.73, 92.55, 60.24, 78.88, 45.72, 88.11, 70.35, 95.59, 33.26, 72.61, 88.87, 67.13, 50.52, 95.92, 40.67, 78.54, 90.45, 55.49, 81.58, 62.97]

def luck_marche_ciel(notes: list) -> list:
    for i in range(len(notes)):
        remainder = notes[i] % 5
        if remainder > 0 and (5 - remainder) < 3:
            notes[i] = notes[i] - remainder + 5
    return notes

new_notes = luck_marche_ciel(notes)
print(new_notes)