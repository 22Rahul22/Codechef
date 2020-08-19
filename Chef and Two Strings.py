t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    ml = 0
    mx = 0
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            mx += 1
        elif s1[i] != s2[i] and (s1[i] != '?' or s2[i] != '?'):
            ml += 1
            mx += 1
    print(ml, mx)
