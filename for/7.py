import math
def prime(n):
    factors = False
    i= 2
    while i<n:
        if n%i == 0:
            factors = True

        i+=1
    return not factors

if prime(int(math.sqrt(int(input("Enter a number: "))))):
    print(True)