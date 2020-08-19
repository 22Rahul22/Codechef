t = int(input())
for _ in range(t):
    s = input().split(" ")
    a = int(s[0])
    l = 0
    for i in range(a):
        b = input()
        if 'CONTEST_WON' in b:
            x = b.split(" ")
            if int(x[1]) <= 20:
                l += 300 + 20 - int(x[1])
            else:
                l += 300
        elif 'TOP_CONTRIBUTOR' in b:
            l += 300
        elif 'BUG_FOUND' in b:
            x = b.split(" ")
            l += int(x[1])
        elif 'CONTEST_HOSTED' in b:
            l += 50
    if 'INDIAN' in s:
        print(l // 200)
    else:
        print(l // 400)
