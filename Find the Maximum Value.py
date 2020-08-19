t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    a = len(arr) - 1
    arr.remove(a)
    print(max(arr))
    