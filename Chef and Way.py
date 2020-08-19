mod = 1000000007
n, k = map(int, input().split())
arr = list(map(int, input().split()))
c = arr[n-1]
i = len(arr) - 1
j = len(arr) - 2
while i >= 0 and j >= 0:
    if arr[i] - arr[j] > k:
        c *= arr[j+1]
        i = j+1
        j = i-1
    else:
        j -= 1
print(c*arr[0])