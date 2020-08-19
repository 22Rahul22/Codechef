n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
x = max(c)
y = max(c)
z = max(c)
for i in range(len(t)):
    if t[i] == 1 and c[i] <= x:
        x = c[i]
    elif t[i] == 2 and c[i] <= y:
         y = c[i]
    elif t[i] == 3 and c[i] <= z:
        z = c[i]
if x + y < z:
    print(x + y)
else:
    print(z)