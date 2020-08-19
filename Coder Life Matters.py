t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    s = 0
    f = 1
    for i in arr:
        if i == 1:
            s += 1
        else:
            s = 0
        if s > 5:
            f = 0
            break
    if f == 0:
        print("#coderlifematters")
    else:
        print("#allcodersarefun")