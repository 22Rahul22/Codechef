t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = [0]
    arr[0] = 1
    c = 1
    for i in range(n-k, n+1):
        print(i, end=" ")
    for i in range(1, n-k):
        print(i, end=" ")
    print()