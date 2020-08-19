#97 122
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x = n
    alp = []
    for i in range(122, 96, -1):
        alp.append(chr(i))
    if x % 2 != 0:
        x = n-1
    a = []
    for i in s:
        a.append(i)
    temp = ''
    for i in range(0, x, 2):
        temp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = temp
    for i in range(len(a)):
        a[i] = alp[ord(a[i]) - 97]
    for i in a:
        print(i, end="")
    print()