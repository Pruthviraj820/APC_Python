n=int(input("Enter the total number of input="))

max=0
i=0
while(i<n):
    a=int(input("Enter the number="))
    if(max<a):
        max=a
    i+=1

print(max)