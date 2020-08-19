t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = a.index(max(a))
    y = b.index(max(b))
    sa = 0
    sb = 0
    for i in range(n):
        if i != x:
            sa += a[i]
        if i != y:
            sb += b[i]
    if sa < sb:
        print("Alice")
    elif sa > sb:
        print("Bob")
    else:
        print("Draw")