t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = [0]*len(arr)
    b = []
    c = []
    f = 0
    arr.sort()
    i = 0
    k = 0
    j = len(arr)-1
    while i < len(arr) and i != len(arr) and k < len(arr):
        if arr[k] not in c:
            c.append(arr[k])
            a[i] = arr[k]
            i += 1
        elif arr[k] not in b:
            b.append(arr[k])
            a[j] = arr[k]
            j -= 1
        else:
            f = 1
            break
        k += 1
    if not b:
        b.append(-1)
    if f == 1:
        print('NO')
    else:
        if max(c) == max(b):
            print('NO')
            f = 1
        if f == 0:
            print('YES')
            for i in range(len(a)):
                print(a[i], end=" ")
            print()