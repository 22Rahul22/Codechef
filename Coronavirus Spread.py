t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    a = []
    c = 0
    j = 0
    flag = 1
    for i in range(len(x)-1):
        if 0 <= abs(x[i+1] - x[i]) <= 2:
            c += 1
            flag = 0
        elif (x[i+1] - x[i]) >= 3:
            a.append(c)
            flag = 1
            c = 0
    if flag == 0:
        a.append(c)
    else:
        a.append(0)
    if a == []:
        a.append(0)
    mini = min(a) + 1
    m = max(a) + 1
    print(mini, m)