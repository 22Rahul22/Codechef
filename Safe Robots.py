t = int(input())
for _ in range(t):
    s = input()
    a = s.index('A')
    b = s.index('B')
    sa, sb = map(int, input().split())
    f = 0
    while a < len(s) and b > 0:
        a += sa
        b -= sb
        if a == b:
            f = 1
            break
    if f == 0:
        print('safe')
    else:
        print('unsafe')