t = int(input())
for _ in range(t):
    n = input()
    a = []
    b = []
    for i in range(int(len(n)/2)):
        a.append(n[i])
    if len(n) % 2 != 0:
        for i in range((int(len(n)/2)+1), len(n)):
            b.append(n[i])
    else:
        for i in range(int(len(n)/2), len(n)):
            b.append(n[i])
    a.sort()
    b.sort()
    if a == b:
        print("YES")
    else:
        print("NO")