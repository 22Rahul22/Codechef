t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    o = 0
    f = 0
    for i in range(n):
        if arr[i] == 1:
            o += 1
        if arr[i] == 0:
            o -= 1
        if o < 0:
            f = 1
            break
    if f == 0:
        print('Valid')
    else:
        print('Invalid')