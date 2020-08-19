n, k = map(int, input().split())
c = 0
for _ in range(n):
    a = int(input())
    if a % k == 0:
        c += 1
print(c)