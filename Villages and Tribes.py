t = int(input())
for _ in range(t):
    s = input()
    f = 100
    c = 0
    a = 0
    b = 0
    for i in s:
        if i == 'A':
            if f == 0:
                a += c
            f = 0
            c = 0
            a += 1
        elif i == 'B':
            if f == 1:
                b += c
            f = 1
            c = 0
            b += 1
        elif i == '.':
            c += 1
    print(a, b)