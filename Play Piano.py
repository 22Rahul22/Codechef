t = int(input())
for _ in range(t):
    s = input()
    b = [0]*2
    c = 0
    t = True
    for i in range(len(s)):
        if s[i] == 'A':
            b[0] += 1
            b[1] = 0
        elif s[i] == 'B':
            b[1] += 1
            b[0] = 0
        if sum(b) > 1:
            print("no")
            t = False
            break
        c += 1
        if c % 2 == 0:
            b[0] = b[1] = 0
    if t:
        print("yes")