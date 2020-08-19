t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0 for i in range(n)] for j in range(n)]
    i = 0
    s = 1
    while i < n:
        j = 0
        k = i
        while j <= i and k >= 0:
            arr[j][k] = s
            s += 1
            j += 1
            k -= 1
        i += 1
    i = n-1
    while i > 0:
        j = n - i
        k = n-1
        while j <= n and k >= n - i:
            arr[j][k] = s
            s += 1
            j += 1
            k -= 1
        i -= 1
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()