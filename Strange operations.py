t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    j = n
    f = 0
    for i in range(k):
        arr.append(s+1)
        s = sum(arr)
        if arr[j] % 2 == 0:
            f = 1
            break
        else:
            j += 1
    if f == 0:
        print('odd')
    else:
        print('even')