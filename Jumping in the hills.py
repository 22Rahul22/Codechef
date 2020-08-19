t = int(input())
for _ in range(t):
    n, u, d = map(int, input().split())
    arr = list(map(int, input().split()))
    f = 1
    c = 0
    for i in range(n-1):
        x = arr[i + 1] - arr[i]
        if 0 <= x <= u:
            c += 1
        elif x < 0 and abs(x) <= d:
            c += 1
        elif x < 0 and f == 1:
            c += 1
            f = 0
        else:
            break
    print(c + 1)