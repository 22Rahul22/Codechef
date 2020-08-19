t = int(input())
for _ in range(t):
    s = input()
    a = 0
    b = 0
    f = 0
    for i in range(len(s)):
        if s[i] == '0':
            a += 1
            if a == 11 and f == 0:
                print('WIN')
                break
            if f == 1 and a - b == 2:
                print('WIN')
                break
        else:
            b += 1
            if b == 11 and f == 0:
                print('LOSE')
                break
            if f == 1 and b - a == 2:
                print('LOSE')
                break
        if a == 10 and b == 10:
            f = 1
