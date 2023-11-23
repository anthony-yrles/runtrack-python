def myLen(L: list) -> int:
    my_Len = 0
    for i in L:
        my_Len += 1
    return my_Len

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

result = []

for i in L:
    if i not in result:
        result += [i]

n = myLen(result)

for i in range(n):
    for j in range(0, n - i - 1):
        if result[j] > result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]

print(result)

