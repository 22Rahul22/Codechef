t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if abs(m - n) <= k:
        print(0)
    else:
        print(abs(m - n) - k)