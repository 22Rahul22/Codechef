t = int(input())
for _ in range(t):
    m, k = map(int, input().split())
    arr = list(map(int, input().split()[:m]))
    b = []
    print(arr)
    if int(len(arr) / 2) % 2 != 0 or len(arr) == 1:
        print(-1)
    else:
        print(int(m / 2))
        n = m - 1
        for i in range(int(m / 2)):
            if i % 2 == 0:
                print(n - i + 1, i + 1, n - (i + 1) + 1)
                temp = arr[n - i]
                arr[n - i] = arr[n - (i + 1)]
                arr[n - (i + 1)] = arr[i]
                arr[i] = temp
            else:
                print(n - i + 2, i + 1, n - i + 1)
                temp = arr[n - i + 1]
                arr[n - i + 1] = arr[n - i]
                arr[n - i] = arr[i]
                arr[i] = temp
