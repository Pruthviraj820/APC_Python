import os
#prints current Working dir
print("Present Working Dir: ",os.getcwd())

#it makes new diretory
os.mkdir("newdir")
print("------newdir created Successfully---")

#for remove dir
os.rmdir("newdir")
print("------newdir Removed Successfully---")

#create list of dir contents
filenames = os.listdir("..")
print(filenames)

#cheks the it is dir or not
print(os.path.isdir("XYZ"))

print(os.path.exists("/etc"))

#it changes current working dir of a process
os.chdir("../anuj")
print("chdir successful now PWD: ",os.getcwd())

os.chdir("../TEMP")
abs_path = os.path.abspath("my_package/rectangle.py")
print("absolute path:"+abs_path)