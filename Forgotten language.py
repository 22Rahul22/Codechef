t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().split(" ")
    arr = [0]*len(s)
    a = []
    for i in range(k):
        x = input().split(" ")
        a += x
    for i in s:
        if i in a:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    print()
