t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    if s % 2 == 0:
        print("NO")
    else:
        print("YES")