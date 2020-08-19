t = int(input())
for _ in range(t):
    s = input()
    c = 0
    i = 0
    while i < len(s)-1:
        if (s[i] == 'x' and s[i + 1] == 'y') or (s[i] == 'y' and s[i + 1] == 'x'):
            c += 1
            i += 2
        else:
            i += 1
    print(c)