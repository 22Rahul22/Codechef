t = int(input())
for _ in range(t):
    s = input()
    u = 0
    d = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i+1] == 'D':
            u += 1
        elif s[i] != s[i+1] and s[i+1] == 'U':
            d +=1
    if s[len(s)-1] == 'U':
        u += 1
    else:
        d += 1
    if d < u:
        print(d)
    elif d > u:
        print(u)
    else:
        print(d)