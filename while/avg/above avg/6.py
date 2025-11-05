n=int(input("Enter the total number of input="))

min=9999
i=0
while(i<n):
    a=int(input("Enter the number="))
    if(min>a):
        min=a
    i+=1

print(min)
    