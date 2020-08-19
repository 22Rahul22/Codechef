t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x, y, s = map(int, input().split())
    if x > 0:
        X = list(map(int, input().split()))
    if y > 0:
        Y = list(map(int, input().split()))
    X.insert(0,0)
    Y.insert(0,0)
    if n not in X:
        X.append(n)
    if m not in Y:
        Y.append(m)
    c = 0
    for i in range(len(Y)):
        for j in range(len(X)):
            c += ((Y[i] - Y[i-1] - 1) // s) * ((X[j] - X[j - 1] - 1) // s)
    print(c)
