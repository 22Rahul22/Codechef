t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    f = 0
    if a == b and c == d:
        f = 1
    elif a == c and b == d:
        f = 1
    elif a == d and b == c:
        f = 1
    if f == 1:
        print('YES')
    else:
        print('NO')