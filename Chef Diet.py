t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    stored = 0
    flag = 0
    for i in range(len(a)):
        a[i] += stored
        if a[i] >= k:
            stored = a[i] - k
        else:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO "+str(i+1))