t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = min(m, n)
    odd = 2*x - 1
    first = x - 1
    ans = first + odd * (max(n, m)-1)
    print(ans)