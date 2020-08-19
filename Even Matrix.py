t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0 for i in range(n)] for j in range(n)]
    sr = 0
    er = n
    sc = 0
    ec = n
    z = 0
    num = 1
    if n % 2 == 0:
        x = n // 2
    else:
        x = 1 + (n // 2)
    while z != x:
        j = sc
        while j < ec:
            arr[sr][j] = num
            num += 1
            j += 1
        sr += 1
        i = sr
        while i < er:
            arr[i][ec - 1] = num
            num += 1
            i += 1
        ec -= 1
        j = ec - 1
        while j >= sc:
            arr[er - 1][j] = num
            num += 1
            j -= 1
        er -= 1
        i = er - 1
        while i >= sr:
            arr[i][sc] = num
            num += 1
            i -= 1
        sc += 1
        z += 1
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()