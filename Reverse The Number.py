t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    rev = 0
    c = 0
    while temp > 0:
        temp = temp // 10
        c += 1
    c -= 1
    temp = n
    while temp > 0:
        r = temp % 10
        rev += r * pow(10, c)
        c -= 1
        temp = temp // 10
    print(rev)