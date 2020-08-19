t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    b = []
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
            b.append(arr.count(i))
    sum = 0
    c = [0]*len(b)
    for i in range(len(b)):
        sum += b[i]
        c[i] = n - sum
    for i in range(n):
        print(c[a.index(arr[i])], end=" ")
    print()
