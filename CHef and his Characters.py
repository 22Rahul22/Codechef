t = int(input())
for _ in range(t):
    s = input()
    a = ['c', 'h', 'e', 'f']
    z = []
    c = 0
    b = 0
    for i in range(len(s)-3):
        if s[i] in a:
            z = []
            c = 0
            for j in range(i, i+4):
                if s[j] in a and s[j] not in z:
                    z.append(s[j])
                    c += 1
                else:
                    break
            #print(z, c)
            if c >= 4:
                b += 1
    if b > 0:
        print('lovely', b)
    else:
        print('normal')