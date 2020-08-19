t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0]*8
    for i in range(n):
        a, b = map(int, input().split())
        if 1 <= a <= 8:
            if arr[a-1] < b:
                arr[a-1] = b
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)