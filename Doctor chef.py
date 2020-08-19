t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    a = arr.copy()
    print(arr)
    i = 0
    k = 0
    while True:
        while x > arr[i]:
            i += 1
        if i == 0:
            while x < arr[k]:
                x *= 2
                arr[len(arr)-1] -= x
                c += 1
                if arr[len(arr)-1]*2 > a[len(a)-1]:
                    arr[len(arr)-1] = a[len(a)-1]
                else:
                    arr[len(arr)-1] *= 2
            print("x =", x)
            print("c =", c)
            print(arr)
            y = x * 2
            z = arr[k] * 2
            j = 0

