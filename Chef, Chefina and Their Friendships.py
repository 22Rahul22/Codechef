t = int(input())
for _ in range(t):
    s = input()
    a = []
    f = 0
    g = 0
    c = 0
    x = s[0]
    print(len(s)//2 + 1)
    if len(s) == 4:
        if s[0] == s[1] and s[2] == s[3]:
            print(1)
        else:
            print(0)
    else:
        for i in range(len(s)//2 + 1):
            if s[i] == x:
                a.append(i)
        print(a)
        for z in range(1, len(a)):
            i = 0
            j = a[z]
            while i < a[z] and j < len(s):
                if s[i] != s[j]:
                    break
                else:
                    j += 1
                    i += 1
            if i == a[z]:
                f = 1
            if f == 1:
                i = j
                q = ((len(s) - j) // 2) + i
                while i < (len(s) - j + 1) and q < len(s):
                    if s[i] != s[q]:
                        g = 0
                        break
                    else:
                        i += 1
                        q += 1
                if q == len(s):
                    g = 1
                    c += 1
        print(c)
