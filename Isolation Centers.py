t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input()
    temp = s
    b = []
    a = []
    p = 0
    i = 0
    while p == 0:
        if len(temp) == 0:
            break
        else:
            b.append(temp[0])
            a.append(s.count(b[i]))
            temp = temp.replace(temp[0], '')
            i += 1
    for v in range(q):
        c = int(input())
        ct = 0
        for i in a:
            if i > c:
                ct += abs(i - c)
        print(ct)