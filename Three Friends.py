t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    s = [x+y, x+z, y+z]
    if min(s) == max(x, y, z):
        print("yes")
    else:
        print("no")