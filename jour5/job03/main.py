def draw_triangle():
    ligne = input("Merci de préciser le nombre de ligne: ")

    if ligne.isdigit():
        space = int(ligne) * 2 + 1
        space_begin = space
        space_middle = 0
        for i  in range (space):
            if i == 0:
                forme = (' ' * space_begin) + '/\x5c'
            elif i == space - 1:
                forme = (' ' * space_begin) + '/' + ('_' * space_middle) + '\x5c'
            elif i % 2 != 0:
                forme = ' '
            else:
                forme = (' ' * space_begin) + '/' + (' ' * space_middle) + '\x5c'
            space_middle += 2
            space_begin -= 1
            print(forme)
    else:
        ligne = input("Nombre invalide. Merci de le ressaisir: ")

draw_triangle()
