n, k = map(int, input().split())
a = [0] * n
for i in range(k):
    s = input().split(" ")
    if len(s) == 2:
        if a[int(s[1])-1] == 0:
            a[int(s[1])-1] = 1
        else:
            a[int(s[1])-1] = 0
    else:
        a = [0]*n
    print(a.count(1))
