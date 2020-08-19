t = int(input())
for _ in range(t):
    k = int(input())
    s = 0
    arr = [['.' for i in range(8)] for j in range(8)]
    arr1 = [[0 for i in range(8)] for j in range(8)]
    i = 1
    if k <= 36:
        while s < k:
            s += i
            i += 1
        n = i-1
        for i in range(8):
            for j in range(1, 9):
                if j <= n and k > 0:
                    arr1[i][j-1] = 1
                    k -= 1
                else:
                    arr1[i][j-1] = 2
            n -= 1
    else:
        a = k - 36
        n = 8
        for i in range(8):
            for j in range(1, 9):
                if j <= n:
                    arr1[i][j-1] = 1
                elif a > 0:
                    arr1[i][j-1] = 1
                    a -= 1
                else:
                    arr1[i][j-1] = 2
            n -= 1
    arr[0][0] = 'O'
    for i in range(7):
        for j in range(7):
            if arr1[i][j] == 1:
                if arr1[i+1][j] != 1:
                    arr[i + 1][j] = 'X'
                if arr1[i+1][j+1] != 1:
                    arr[i+1][j+1] = 'X'
                if arr1[i][j+1] != 1:
                    arr[i][j+1] = 'X'
    for i in range(8):
        for j in range(8):
            print(arr[i][j], end="")
        print()
