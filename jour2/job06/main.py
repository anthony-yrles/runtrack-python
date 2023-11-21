for n in range(2, 1001):
    prime = True
    for i in range (2, n):
        if n % i not in [1, n] == 0:
            prime = False
    if prime == True:
        print(n)
        
# Version évoluer max

for num in range(2,1001):
    if all(num%i!=0 for i in range(2,num)):
       print (num)