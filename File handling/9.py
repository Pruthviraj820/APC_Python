import os
if os.path.exists("hi there.txt"):
    os.remove("hi there.txt")
else:
    print("file not present")