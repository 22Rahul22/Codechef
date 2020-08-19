n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
diff = int(input())
arr.sort()
c = 0
a = arr[0]
f = 1
i = 0
while f == 1:
    temp = c
    j = i + 1
    while j < n:
        if arr[j] - arr[i] >= diff:
            c += 1
            break
        else:
            j += 1
    if temp != c:
        arr.remove(arr[i])
        arr.remove(arr[j])
    else:
        arr.remove(arr[i])