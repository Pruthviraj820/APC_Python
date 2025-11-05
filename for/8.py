n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(ord('A')+j),end = '')
    print()
