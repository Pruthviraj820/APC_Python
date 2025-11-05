a=int(input("Enter the number"))

res=0

while(a>0):
    mod=a%10
    res=mod+res*10
    a=a//10

print(res)