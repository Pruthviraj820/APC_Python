with open("demo.txt","w") as f:
    f.write("everything is deleted")

with open("demo.txt","r") as f:
    print(f.read())