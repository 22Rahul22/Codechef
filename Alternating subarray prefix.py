t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = []
    cp = 0
    cn = 0
    for i in range(n - 1):
        if arr[i] >= 0 and arr[i + 1] < 0:
            cn = 0
            cp += 1
            i += 1
        elif arr[i] < 0 and arr[i + 1] >= 0:
            cp = 0
            cn += 1
            i += 1
        else:
            cp = 0
            cn = 0
            a.append(1)
        if cp == 0 and cn != 0:
            a.append(cn)
        elif cn == 0 and cp != 0:
            a.append(cp)
    print(a)