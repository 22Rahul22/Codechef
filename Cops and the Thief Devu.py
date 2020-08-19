t = int(input())
for _ in range(t):
    m, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    b = [0]*101
    bc = 0
    fd = 0
    for i in range(len(arr)):
        s = arr[i] + (x * y)
        d = arr[i] - (x * y)
        if d <= 1:
            bc = 1
        else:
            bc = d
        if s >= 100:
            fd = 100
        else:
            fd = s
        for i in range(bc, fd+1):
            b[i] = 1
    count = 0
    for i in b:
        if i == 0:
            count += 1
    print(count - 1)