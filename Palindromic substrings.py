t = int(input())
for _ in range(t):
    a = input()
    b = input()
    f = 0
    for i in a:
        if i in b:
            f = 1
            break
    if f == 0:
        print('No')
    else:
        print('Yes')