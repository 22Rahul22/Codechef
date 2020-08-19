t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    a = []
    area = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        if p <= b and area < w * h:
            area = w * h
    if area == 0:
        print("no tablet")
    else:
        print(area)