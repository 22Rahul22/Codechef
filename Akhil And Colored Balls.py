t = int(input())
for _ in range(t):
    x = input()
    y = input()
    z = ""
    for i in range(len(x)):
        if x[i] == y[i] and x[i] == 'W':
            z += 'B'
        elif x[i] == y[i] and x[i] == 'B':
            z += 'W'
        elif x[i] != y[i]:
            z += 'B'
    print(z)