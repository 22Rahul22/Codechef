def count3(a):
    c = 0
    while a > 0:
        if a % 10 == 3:
            c += 1
        a = a // 10
    return c


t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    if temp < 333:
        print(333)
    else:
        for i in range(1, 10000):
            n = n + 1
            r = count3(n)
            if r >= 3:
                print(n)
                break
            else:
                continue
