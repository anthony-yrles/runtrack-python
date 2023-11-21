i = 0

for i in range(101):
    if i == 26:
        i += 1
    elif i == 37:
        i += 1
    elif i == 88:
        i += 1
    else:
        print(i)
        
for i in range(101):
    if i == 26 or i == 37 or i == 88:
        i += 1
    else:
        print(i)
        
for i in range(101):
    if i not in [26, 37, 88]:
        print(i)