t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0]
    ind = [0]*n
    comm = []
    for i in range(n-1):
        if arr[i] not in comm:
            arr.append(0)
            comm.append(arr[i])
            ind[arr[i]] = i
        else:
            arr.append(abs(ind[arr[i]] - i))
            ind[arr[i]] = i
    print(arr.count(arr[n-1]))
