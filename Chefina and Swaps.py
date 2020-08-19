t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if a == b:
        print(0)
    else:
        i = 0
        j = 0
        x = 0
        y = 0
        f = 0
        a1 = []
        b1 = []
        c1 = []
        c2 = []
        while i < len(a) - 1 and j < len(b) - 1:
            if a[i] == a[i + 1]:
                x += 1
            else:
                a1.append(a[i])
                c1.append(x + 1)
                x = 0
            if b[j] == b[j + 1]:
                y += 1
            else:
                b1.append(b[j])
                c2.append(y + 1)
                y = 0
            i += 1
            j += 1
        p = []
        q = []
        a1.append(a[len(a) - 1])
        b1.append(b[len(b) - 1])
        c1.append(x + 1)
        c2.append(y + 1)
        i = j = 0
        while i < len(a1) and j < len(b1):
            if a1[i] == b1[j]:
                if abs(c1[i] - c2[j]) % 2 == 0:
                    if c1[i] > c2[j]:
                        for k in range((c1[i] - c2[j]) // 2):
                            p.append(a1[i])
                    elif c1[i] < c2[j]:
                        for k in range((c2[j] - c1[i]) // 2):
                            q.append(b1[j])
                else:
                    f = 1
                    break
                i += 1
                j += 1
            else:
                if a1[i] < b1[j]:
                    if c1[i] % 2 == 0:
                        for k in range(c1[i] // 2):
                            p.append(a1[i])
                    else:
                        f = 1
                        break
                    i += 1
                else:
                    if c2[j] % 2 == 0:
                        for k in range(c2[j] // 2):
                            q.append(b1[j])
                    else:
                        f = 1
                        break
                    j += 1
        if i != len(a1):
            while i < len(a1):
                for k in range(c1[i] // 2):
                    p.append(a1[i])

                i += 1
        if j != len(b1):
            while j < len(b1):
                for k in range(c2[j] // 2):
                    q.append(b1[j])
                j += 1
        if f == 1:
            print(-1)
        else:
            x = min(a[0], b[0])*2
            c = 0
            i = 0
            j = len(q) - 1
            while i < len(p) or j > -1:
                if x == min(x, p[i], q[j]):
                    c += x
                elif p[i] == min(x, p[i], q[j]):
                    c += p[i]
                else:
                    c += q[j]
                i += 1
                j -= 1
            print(c)
