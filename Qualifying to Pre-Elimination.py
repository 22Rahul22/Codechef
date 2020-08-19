t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    c = k
    for i in range(k, n):
        if arr[i] == arr[k-1]:
            c += 1
        else:
            break
    print(c)