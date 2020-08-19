t = int(input())
for _ in range(t):
    s = sorted(input())
    p = input()
    m = {}
    n = {}
    ans = ''
    if len(s) == len(p):
        print(p)
    else:
        a = [0] * 26
        b = [0] * 26
        for i in range(len(s)):
            a[ord(s[i]) - ord('a')] += 1
            m[s[i]] = a[ord(s[i]) - ord('a')]
        for i in range(len(p)):
            a[ord(p[i]) - ord('a')] -= 1
            b[ord(p[i]) - ord('a')] += 1
            n[p[i]] = b[ord(p[i]) - ord('a')]
            m[p[i]] = a[ord(p[i]) - ord('a')]
        keys = list(m.keys())
        keyp = list(n.keys())
        for i in range(len(keys)):
            if keys[i] == keyp[0]:
                if keys[i] > keyp[1]:
                    ans += p
                    ans += keys[i]*m[keys[i]]
                else:
                    ans += keys[i]*m[keys[i]]
                    ans += p
            else:
                ans += keys[i]*m[keys[i]]
        print(ans)

