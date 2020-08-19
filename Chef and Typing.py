t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    c = 0
    for i in range(n):
        a = input()
        s.append(a)
        su = 2
        for j in range(1, len(a)):
            if a[j] == 'f' or a[j] == 'd':
                if a[j-1] == 'f' or a[j-1] == 'd':
                    su += 4
                else:
                    su += 2
            else:
                if a[j-1] == 'f' or a[j-1] == 'd':
                    su += 2
                else:
                    su += 4
        if s.count(a) > 1:
            su = su // 2
        c += su
    print(c)