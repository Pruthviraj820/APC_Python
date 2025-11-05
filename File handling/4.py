with open("example1.txt", "w") as f:
    f.write("Python is fun!\n")
    f.write("File handling is easy.\n")


with open("example1.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)
