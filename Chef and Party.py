t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    for i in range(len(arr)):
        if c >= arr[i]:
            c += 1
    print(c)