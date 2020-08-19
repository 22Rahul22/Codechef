t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input()
    a = []
    a.append(x)
    for i in s:
        if i == 'L':
            x -= 1
        else:
            x += 1
        if x not in a:
            a.append(x)
    print(len(a))