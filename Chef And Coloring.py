t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    a = []
    a.append(arr.count('R'))
    a.append(arr.count('G'))
    a.append(arr.count('B'))
    print(min(a[0] + a[1], a[0] + a[2], a[1] + a[2]))