t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    a = arr[:3]
    c = arr[3:7]
    f = 0
    if (a[0] == a[1] and c[0] == c[1]) or (a[0] < a[1] and c[0] < c[1]) or (a[0] > a[1] and c[0] > c[1]):
        f += 1
    if (a[0] == a[2] and c[0] == c[2]) or (a[0] < a[2] and c[0] < c[2]) or (a[0] > a[2] and c[0] > c[2]):
        f += 1
    if (a[1] == a[2] and c[1] == c[2]) or (a[1] < a[2] and c[1] < c[2]) or (a[1] > a[2] and c[1] > c[2]):
        f += 1
    if f == 3:
        print('FAIR')
    else:
        print('NOT FAIR')