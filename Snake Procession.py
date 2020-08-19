t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    f = 0
    z = 0
    for i in s:
        if i == 'H' and f == 0:
            f = 1
        elif i == 'T' and f == 1:
            f = 0
        elif i == 'H' and f == 1:
            z = 1
            break
        elif i == 'T' and f == 0:
            z = 1
            break
    if f == 1:
        z = 1
    if z == 0:
        print("Valid")
    else:
        print("Invalid")