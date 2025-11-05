with open("demo.txt","a") as f:
    f.write("now file has more content")

with open("demo.txt","r") as f:
    print(f.read())