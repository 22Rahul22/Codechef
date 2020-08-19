t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = str(m)
    if a.count('9') != len(a):
        b = len(a) - 1
    else:
        b = len(a)
    ans1 = n * b
    print(ans1, n)
