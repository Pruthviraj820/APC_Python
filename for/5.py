def fact(n):
    if n==0:
        return 1
    fact = 1
    for i in range(2,n+1):
        fact = fact * i    
    return fact

sum = 0
for i in range(0,int(input())+1):
    sum += 1/fact(i)

print(sum)