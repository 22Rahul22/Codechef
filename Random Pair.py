t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = []
    for i in range(n):
        for j in range(i + 1, n):
            a.append(arr[i] + arr[j])
    x = max(a)
    c = a.count(x)
    print("%.8f" % (c / len(a)))
