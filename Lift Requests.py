t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    c = 0
    lst = 0
    for i in range(q):
        a, b = map(int, input().split())
        c += abs(lst - a)
        c += abs(a - b)
        lst = b
    print(c)