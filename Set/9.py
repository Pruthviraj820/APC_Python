with open("practice.txt","r") as f:
    data=f.read()

    it=data.replace("java","python")
    print(it)
f.close()


with open("practice.txt","w") as f:
   f.write(it)
f.close()


with open("practice.txt","r") as f:
    data=f.read()
    word="hvasx"
    if(data.find(word)!=-1):
        print("true")
    else:
        print("false")
f.close()