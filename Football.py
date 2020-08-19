t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [0]*len(a)
    for i in range(len(a)):
        arr[i] = ((a[i] * 2) - b[i]) * 10
    if max(arr) <= 0:
        print(0)
    else:
        print(max(arr))