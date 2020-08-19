import math
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    c = arr[0]
    for i in range(1, len(arr)):
        c = math.gcd(c, arr[i])
    for i in range(len(arr)):
        arr[i] = arr[i] // c
        print(arr[i],end=" ")
    print()