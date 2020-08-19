t = int(input())
for _ in range(t):
    n = int(input())
    if n < 1500:
        s = n + n/10 + 9*n/10
    else:
        s = n + 500 + 98*n/100
    print('%.2f'%s)