a=int(input("Enter the number="))
t=a
res=0

while(a>0):
    mod=a%10
    res=mod+res*10
    a=a//10

if(res==t):
    print("Palindrome number")
else:
    print("Not a Palindrome number")