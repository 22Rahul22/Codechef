t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    x = abs(l - r) + 1
    if x == 1:
        print(x)
    else:
        print(k)