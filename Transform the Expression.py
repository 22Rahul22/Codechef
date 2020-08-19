t = int(input())
for _ in range(t):
    a = list(input())
    b = []
    c = ['+', '-', '*', '/', '^']
    for i in range(len(a)):
        if a[i] == '(':
            b.append(a[i])
        elif 'a' <= a[i] <= 'z':
            print(a[i], end="")
        elif a[i] in c:
            b.append(a[i])
        elif a[i] == ')':
            j = len(b) - 1
            while b[j] != '(':
                if b[j] in c:
                    print(b[j], end="")
                    b.pop()
                else:
                    b.pop()
                j -= 1
            b.pop()
    if len(b) != 0 and b[0] != '(':
        print(b.pop(),end="")
    print()