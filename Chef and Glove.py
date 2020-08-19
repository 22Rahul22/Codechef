t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    g = list(map(int, input().split()))
    i = 0
    j = 0
    f1 = 0
    f2 = 0
    while i < n and j < n:
        if l[i] > g[j]:
            f1 = 1
            break
        else:
            i += 1
            j += 1
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if l[i] > g[j]:
            f2 = 1
            break
        else:
            i += 1
            j -= 1
    if f1 == 0 and f2 == 0:
        print("both")
    elif f1 == 0 and f2 != 0:
        print("front")
    elif f1 != 0 and f2 == 0:
        print("back")
    else:
        print("none")