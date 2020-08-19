t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    name = []
    for i in range(n):
        s = input()
        name.append(s)
    for i in range(n):
        if name[i].split(" ")[0] in b:
            a.append(name[i])
            b.append(name[i].split()[0])
            x = b.index(name[i].split(" ")[0])
            a[x] = name[x]
        else:
            a.append(name[i].split(" ")[0])
            b.append(name[i].split(" ")[0])
    for i in range(len(a)):
        print(a[i], end="\n")