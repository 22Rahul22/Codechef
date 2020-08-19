t = int(input())
for _ in range(t):
    s = input()
    x = s.count('1')
    c = 0
    if x == 0:
        print('NO')
    else:
        for i in range(s.index('1'), len(s)):
            if s[i] != '0':
                c += 1
            else:
                break
        if c == x:
            print('YES')
        else:
            print('NO')