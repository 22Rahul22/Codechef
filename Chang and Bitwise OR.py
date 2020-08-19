t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    for i in range(n-1):
        s = s | arr[i]
    print(s)