t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split(" ")
    f = 1
    for i in range(n-1):
        if s[i] == 'cookie' and s[i+1] != 'milk':
            f = 0
            break
    if s[n-1] == 'cookie':
        f = 0
    if f == 1:
        print('YES')
    else:
        print('NO')