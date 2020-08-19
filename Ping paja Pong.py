t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    s = x + y
    r = s // k
    if r % 2 == 0:
        print('Chef')
    else:
        print('Paja')