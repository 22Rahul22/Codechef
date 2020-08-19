def digit(x):
    s = 0
    while x > 0:
        r = x % 10
        s += r
        x = x // 10
    return s


t = int(input())
for _ in range(t):
    n = int(input())
    chef = 0
    morty = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum1 = digit(a)
        sum2 = digit(b)
        if sum1 > sum2:
            chef += 1
        elif sum1 < sum2:
            morty += 1
        else:
            chef += 1
            morty += 1
    if chef > morty:
        print(0, chef)
    elif chef < morty:
        print(1, morty)
    else:
        print(2, chef)