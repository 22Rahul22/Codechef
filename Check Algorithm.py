t = int(input())
for _ in range(t):
    s = input()
    a = ""
    c = 0
    if len(s) == 1:
        a += s
        a += '1'
    else:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
            else:
                a += s[i]
                a += str(c+1)
                c = 0
        a += s[i+1]
        a += str(c+1)
    if len(s) > len(a):
        print('YES')
    else:
        print('NO')