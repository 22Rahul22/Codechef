t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    for i in arr:
        if i > k:
            s += k
        else:
            s += i
    print(sum(arr) - s)