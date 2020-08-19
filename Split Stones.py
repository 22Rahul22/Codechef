t = int(input())
for _ in range(t):
    a, b, c, x, y = map(int, input().split())
    s = a + b + c
    s1 = x + y
    if s == s1 and min(a, b, c) <= min(x, y):
        print("YES")
    else:
        print('NO')
