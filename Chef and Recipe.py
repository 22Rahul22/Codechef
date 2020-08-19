t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = []
    f = 0
    for i in arr:
        if i not in a:
            a.append(i)
    b = []
    for i in a:
        b.append(arr.count(i))
    count = 1
    c = []
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            c.append(count)
            count = 1
    c.append(count)
    if len(c) != len(b):
        print('NO')
        f = 1
    else:
        for i in range(len(b)):
            if b.count(b[i]) >= 2:
                print('NO')
                f = 1
                break
    if f == 0:
        print('YES')