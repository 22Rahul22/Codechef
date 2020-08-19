t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    p = arr[5]
    arr = arr[:5]
    for i in range(len(arr)):
        arr[i] *= p
    s2 = sum(arr)
    if s2 > 120:
        print('Yes')
    else:
        print('No')
