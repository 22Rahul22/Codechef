t = int(input())
for _ in range(t):
    x1, x2, x3, v1, v2 = map(int, input().split())
    a = abs(x1 - x3)
    b = abs(x2 - x3)
    a /= v1
    b /= v2
    if a > b:
        print("Kefa")
    elif a < b:
        print("Chef")
    else:
        print("Draw")
