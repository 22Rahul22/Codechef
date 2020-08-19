t = int(input())
for _ in range(t):
    p, q, k = map(int, input().split())
    s = int((p + q) / k)
    if s % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
