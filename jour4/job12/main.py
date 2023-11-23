L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

x = 0

def myLen(L: list) -> int:
    my_Len = 0
    for i in L:
        my_Len += 1
    return my_Len

def tri(liste):
    n = myLen(L)
    for i in range(n):
        for x in range (0, n-i-1):
            if liste[x] > liste[x + 1]:
                liste[x], liste[x + 1] = liste[x + 1], liste[x]
    print(L)

tri(L)
