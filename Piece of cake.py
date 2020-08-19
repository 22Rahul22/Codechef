t = int(input())
for _ in range(t):
    s = input()
    a = []
    b = []
    for i in s:
        if i not in a:
            a.append(i)
            b.append(s.count(i))
    b.sort()
    s = 0
    for i in range(len(b)-1):
        s += b[i]
    if s == max(b):
        print("YES")
    else:
        print("NO")