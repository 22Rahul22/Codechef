import statistics
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    b = [arr[0], arr[1], arr[2]]
    while len(arr) != 2:
        arr.remove(statistics.median(b))
        if len(arr) == 2:
            break
        b = [arr[0], arr[1], arr[2]]
    print(arr[0], arr[1])
