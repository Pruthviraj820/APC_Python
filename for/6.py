def fact(n):
    if n==0:
        return 1
    fact = 1
    while n>0:
        fact = fact * n
        n-=1
    return fact

sum = 0
x = int(input("Enter x: "))
n = int(input("Enter n: "))
for i in range(0,n+1):
    sum += (((-1)**i)*(x**(2*i)))/fact(2*i)
