t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    arr = []
    for i in x:
        if i not in arr:
            arr.append(i)
    print(len(arr))