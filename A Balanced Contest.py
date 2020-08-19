t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    x = p // 2
    y = p //10
    c1 = 0
    c2 = 0
    for i in range(n):
        if arr[i] <= y:
            c1 += 1
        elif arr[i] >= x:
            c2 += 1
    if c1 == 2 and c2 == 1:
        print('yes')
    else:
        print('no')