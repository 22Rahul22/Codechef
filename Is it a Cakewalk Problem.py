t = int(input())
for _ in range(t):
    c = 0
    for i in range(10):
        a = list(map(int, input().split()))
        for i in a:
            if i <= 30:
                c += 1
    if c >= 60:
        print('yes')
    else:
        print('no')