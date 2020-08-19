n = int(input())
m, c = map(int, input().split())
x = []
y = []
p = []
for i in range(n):
    a, b, d = map(int, input().split())
    x.append(a)
    y.append(b)
    p.append(d)
l = []
r = []
#eq = m*x + c
for i in range(0, len(x)):
    if y[i] > m*x[i] + c:
        l.append(p[i])
    else:
        r.append(p[i])
print(max(sum(l), sum(r)))
