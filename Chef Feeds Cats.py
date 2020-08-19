t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [0]*n
    flag = 0
    a = list(map(int, input().split()))
    for i in range(len(a)):
        arr[a[i]-1] += 1
        if max(arr) - min(arr) > 1:
            print("NO")
            flag = 1
            break
    if flag == 0:
        print("YES")