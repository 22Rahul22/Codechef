n, q = map(int, input().split())
arr = list(map(int, input().split()))
a = min(arr)
b = max(arr)
for i in range(q):
    t = int(input())
    if a <= t <= b:
        print("Yes")
    else:
        print('No')