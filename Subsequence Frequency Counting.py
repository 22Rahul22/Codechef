mod = pow(10,9) + 7

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            a = min(arr[i:j])
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
    for i in range(len(arr)):
        print(d[arr[i]]%mod,end=" ")
    print()