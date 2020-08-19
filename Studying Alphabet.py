s = input()
n = int(input())
for _ in range(n):
    w = input()
    f = 0
    for i in range(len(w)):
        if w[i] not in s:
            f = 1
    if f == 0:
        print('Yes')
    else:
        print('No')