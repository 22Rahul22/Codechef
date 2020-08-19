#97 122
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    s = input()
    a = []
    b = []
    for i in s:
        if i not in a:
            a.append(i)
    if len(a) == 26:
        print(0)
    else:
        s = 0
        for i in range(97, 123):
            if chr(i) not in a:
                s += arr[i-97]
        print(s)
