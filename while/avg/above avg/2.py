a=int(input("Enter the number"))
res=0

while(a>0):
    mod=a%10
    res=res+mod
    a=a//10

print(res)