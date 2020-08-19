t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().split(" ")
    f = 0
    i = 0
    while i < k:
        if s[n - i - 1] == 'H':
            f = 1
        else:
            f = 0
        i += 1
    a = s[:n-k]
    if f == 0:
        print(a.count('H'))
    else:
        print(a.count('T'))