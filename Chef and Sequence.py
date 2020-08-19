t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    x = arr.count(1)
    if x + k >= n:
        print('YES')
    else:
        print('NO')