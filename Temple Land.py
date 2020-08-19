t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = n // 2
    f = 0
    if n % 2 == 0:
        print('no')
    else:
        for j in range(1, i+1):
            if arr[j - 1] != j:
                f = 1
                break
        if f == 0:
            for j in range(n//2, n-1):
                if arr[j] != arr[j+1] + 1:
                    f = 1
                    break
        if f == 0:
            print('yes')
        else:
            print('no')