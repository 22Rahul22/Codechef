t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a = list(map(int, input().split()))
        arr[i] = a
    ans = 0
    k = n
    while k > 0:
        i = 0
        j = n - k
        b = 0
        while i < k and j < n:
            b += arr[i][j]
            i += 1
            j += 1
        if b > ans:
            ans = b
        if n != k:
            m = n - k
            p = 0
            b = 0
            while m < n and p < k:
                b += arr[m][p]
                m += 1
                p += 1
        if b > ans:
            ans = b
        k -= 1
    print(ans)