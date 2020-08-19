t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = []
    c = 0
    arr.append(a[0])
    for i in range(n-1):
        arr.append(a[i+1]-a[i])
        if arr[i] >= b[i]:
            c += 1
    if arr[n-1] >= b[n-1]:
        c += 1
    print(c)