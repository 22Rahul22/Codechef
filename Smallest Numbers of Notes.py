t = int(input())
for _ in range(t):
    n = int(input())
    notes = [100, 50, 10, 5, 2, 1]
    t = True
    i = 0
    c = 0
    while n > 0:
        if notes[i] <= n:
            c += int(n / notes[i])
            n = n % notes[i]
        i += 1
    print(c)