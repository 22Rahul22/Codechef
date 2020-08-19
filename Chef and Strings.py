t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = 0
    for i in range(1, n):
        s += abs(arr[i] - arr[i-1]) - 1
    print(s)