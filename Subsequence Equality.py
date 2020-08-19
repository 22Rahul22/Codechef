t = int(input())
for _ in range(t):
    s = input()
    b = []
    a = []
    for i in s:
        if i not in b:
            b.append(i)
            a.append(s.count(i))
    c = 0
    f = 0
    for i in a:
        if i >= 2:
            print('yes')
            f = 1
            break
    if f == 0:
        print('no')