t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    neg = 0
    pos = 0
    for i in a:
        if i < 0:
            neg += 1
        else:
            pos += 1
    x = max(pos, neg)
    y = min(pos, neg)
    if y == 0:
        y = x
    print(x, y)