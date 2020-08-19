n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
sm = 0
for i in arr:
    if sm < i < m:
        sm = i
print(sm)