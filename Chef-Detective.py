n = int(input())
arr = list(map(int, input().split()))
a = [0]*(n+1)
for i in range(n):
    a[arr[i]] += 1
for i in range(len(a)):
    if a[i] == 0:
        print(i, end=" ")