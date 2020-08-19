t = int(input())
for _ in range(t):
    x = int(input())
    if x % 5 != 0:
        print("-1")
    else:
        if x % 10 == 0:
            print(0)
        else:
            c = 0
            while x % 10 != 0:
                x *= 2
                c += 1
            print(c)