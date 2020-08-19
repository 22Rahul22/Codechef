t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            c += 1
        else:
            if a[i] == '?' or b[i] == '?':
                c += 1
            else:
                print('No')
                break
    if c == len(a):
        print('Yes')