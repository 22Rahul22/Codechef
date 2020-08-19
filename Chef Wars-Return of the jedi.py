t = int(input())
for _ in range(t):
    h, p = map(int, input().split())
    while h > 0 and p > 0:
        h -= p
        p = p // 2
    if h > 0:
        print(0)
    else:
        print(1)