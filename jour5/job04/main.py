def tapis(n):
    tapis = n
    vide = 0
    rectangle = ""
    for i in range(n + 3):
        if i == 0 or i == n + 2:
            rectangle = ('+' + ('-' * (n + 1)) + '+')
        else:
            rectangle = ('|' + '#' * tapis + ' ' + '#' * vide + '|')
            tapis -= 1
            vide += 1
        print(rectangle)

tapis(100)