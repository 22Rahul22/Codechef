t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x = 0
    y = 0
    temp = 100
    for i in range(n):
        if s[i] == 'L' and temp != 1:
            x -= 1
            temp = 1
        elif s[i] == 'R' and temp != 1:
            x += 1
            temp = 1
        elif s[i] == 'U' and temp != 0:
            y += 1
            temp = 0
        elif s[i] == 'D' and temp != 0:
            y -= 1
            temp = 0
    print(x, y)
