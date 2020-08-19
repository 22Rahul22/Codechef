t = int(input())
for _ in range(t):
    b = int(input())
    x = int(b/2) - 1
    sum = 0
    while x > 0:
        sum += x
        x -= 1
    print(sum)