t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a = arr[:n // 2]
    b = arr[n//2:]
    b.sort(reverse=True)
    s = 0
    for i in range(len(a)):
        s += abs(a[i] - b[i])
    print(s)