t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    a = []
    k = 0
    s = ""
    j = 0
    arr.append(0)
    for i in range(n):
        if arr[i] + 1 == arr[i + 1]:
            c += 1
        else:
            if c >= 2:
                a.append(i - c)
                a.append(i)
                s += str(arr[a[j]]) + "..." + str(arr[a[j+1]])+","
                j += 2
            elif c == 1:
                s += str(arr[i-1]) + "," + str(arr[i])+","
            else:
                s += str(arr[i])+","
            c = 0
    s = s[:len(s)-1]
    print(s)