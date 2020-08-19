t = int(input())
for _ in range(t):
    d = int(input())
    day = []
    prob = []
    for i in range(d):
        a, b = map(int, input().split())
        day.append(a)
        prob.append(b)
    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        s = 0
        for j in range(d):
            if a < day[j]:
                break
            else:
                s += prob[j]
        if s >= b:
            print('Go Camp')
        else:
            print('Go Sleep')