t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        s = int(input())
        x = s // pow(2, 16)
        a.append(x)
        y = str(bin(x).replace("0b", ""))
        y += '0'*16
        b.append(abs(int(s) - int(y, 2)))
    print('Case {}:'.format(_ + 1))
    for i in range(len(a)):
        print(b[i], end=" ")
    print()
    for i in range(len(a)):
        print(a[i], end=" ")
