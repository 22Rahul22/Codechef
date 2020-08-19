t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    bob = 0
    limak = 0
    t = True
    for i in range(1, 500):
        if i % 2 != 0:
            a -= i
            if a < 0:
                print("Bob")
                break
        else:
            b -= i
            if b < 0:
                print("Limak")
                break


