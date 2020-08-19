t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    u = input()
    i = 0
    c = 0
    while i < n:
        if u[i] == 'N':
            i += 1
        elif u[i] != s[i]:
            i += 2
        else:
            c += 1
            i += 1
    print(c)