t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    f = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            f = 1
            break
    if f == 1:
        print("NO")
    else:
        print("YES")