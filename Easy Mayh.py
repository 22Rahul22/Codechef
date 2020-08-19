def sd(x):
    temp = x
    s = 0
    while temp > 0:
        r = temp % 10
        s += r
        temp = int(temp/10)
    return s


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if sd(arr[i] * arr[j]) > max:
                max = sd(arr[i] * arr[j])
    print(max)