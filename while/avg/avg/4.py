last = 1
last_sec = 0

#n = int(input("ENter a number"))
n = 5
cnt = 0

while cnt <= n:
    print(last_sec ,' ',end='')
    temp = last
    last = last + last_sec
    last_sec = temp
    cnt += 1
