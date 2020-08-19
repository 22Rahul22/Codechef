t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    if x >= y:
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    arr[i][j] = y
                else:
                    arr[i][j] = 0
    if x < y:
        if x <= y//2:
            for i in range(n):
                for j in range(m):
                    arr[i][j] = x
        else:
            for i in range(n):
                for j in range(m):
                    if (i+j) % 2 == 0:
                        arr[i][j] = x
                    else:
                        arr[i][j] = y-x
    s = 0
    for i in range(n):
        s += sum(arr[i])
    print(s)