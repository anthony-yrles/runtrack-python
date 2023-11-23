L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def intNumber(x: float) -> int:
    if x < int(x) + 0.5:
        return int(x)
    else:
        return int(x + 1)
    
def intList(L: list) -> list:
    result = []
    for i in L:
        result = result + [intNumber(i)]
    return result

def myLen(L: list) -> int:
    my_Len = 0
    for i in L:
        my_Len += 1
    return my_Len

def sort(L):
    n = myLen(L)
    for i in range(n):
        sort = True
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                sort = False
        if sort:
            break

result = intList(L)
sort(result)
print(result)
