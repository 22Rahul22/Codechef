t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = [0]*100
    for i in arr:
        a[i-1] += 1
    x = a.index(max(a))+1
    print(len(arr) - arr.count(x))