t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    arr = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        a = list(map(int, input().split()))
        arr[i] = a
    f = 1
    for i in range(r):
        for j in range(c):
            count = 4
            if i == 0 or i == r - 1:
                count -= 1
            if j == 0 or j == c - 1:
                count -= 1
            if count <= arr[i][j]:
                f = 0
                break
    if f == 1:
        print('Stable')
    else:
        print('Unstable')