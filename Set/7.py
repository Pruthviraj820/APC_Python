'''
f=open("sample.txt","w")

f.write("hi there pussy")

f.close()


with open("sample.txt","r") as f:

    data=f.read()
    print(data)
f.close()


f=open("sample.txt","a")

f.write("\ni am batman")

f.close()
'''