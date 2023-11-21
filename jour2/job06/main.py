# Version 1

for n in range(2, 1001):
    prime = True
    for i in range (2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        print(n)

# Version évolué par cyril
    
for n in range(2, 1001):
    prime = True
    for i in range (2, n):
        if not (n % i) :
            prime = False
            break
    if prime == True:
        print(n)
        
# Version de Kevin plus simple

for n in range (2, 1001) :
    for i in range (2, n) :
        if n % i == 0:
            break
        else:
            print(n)
        
# Version évoluer max

for num in range(2,1001):
    if all(num%i!=0 for i in range(2,num)):
       print (num)