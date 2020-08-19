t = int(input())
for _ in range(t):
    s = input()
    a = 0
    b = 0
    c = 0
    f = 0
    for i in range(len(s)):
        if s[i] == 'C' and b == 0 and c == 0:
            a = 1
        elif s[i] == 'E' and c == 0:
            b = 1
        elif s[i] == 'S':
            c = 1
        else:
            f = 1
            break
    if f == 0 or len(s) == 1:
        print('yes')
    else:
        print('no')