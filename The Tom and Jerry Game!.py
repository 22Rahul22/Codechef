import math
t = int(input())
for _ in range(t):
    ts = int(input())
    s = str(bin(ts).replace("0b", ""))
    if ts % 2 != 0:
        print(ts // 2)
    elif math.log2(ts) == int(math.log2(ts)):
        print(0)
    else:
        x = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                x += 1
            else:
                break
        a = ""
        for i in range(len(s)-x-1):
            a += s[i]
        a = int(a, 2)
        print(a)