t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    print(s)
    arr = [0]*26
    f = 0
    for i in s:
        arr[ord(i)-ord('a')] += 1
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            f = 1
            break
    if f == 1:
        print("NO")
    else:
        print("YES")