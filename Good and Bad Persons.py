t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    sm = 0
    l = 0
    for i in s:
        if 'A' <= i <= 'Z':
            l += 1
        else:
            sm += 1
    if l <= k and sm <= k:
        print('both')
    else:
        if l <= k:
            print('chef')
        elif sm <= k:
            print('brother')
        else:
            print('none')
