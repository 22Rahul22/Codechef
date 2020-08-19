def s(x, y):
    if x == 0:
        return y
    else:
        sum = 0
        for i in range(y+1):
            sum += i
        return s(x-1, sum)


t = int(input())
for _ in range(t):
    d, n = map(int, input().split())
    print(s(d, n))