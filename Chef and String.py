t = int(input())
for _ in range(t):
    s = input()
    if len(s) <= 2:
        print('YES')
    else:
        l = ""
        r = ""
        r += s[len(s) - 1]
        for i in range(len(s)-1):
            r += s[i]
            if i >= 1:
                l += s[i]
        l += s[len(s)-1]
        l += s[0]
        if l == r:
            print('YES')
        else:
            print('NO')