t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    f = 0
    for i in arr:
        if i >= x:
            print("YES")
            f = 1
            break
    if f == 0:
        print('NO')