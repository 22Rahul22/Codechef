t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l > r:
        a = 24 - l
        print(2*(a+r))
    else:
        print(2*(r-l))