t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        x = int(input())
        if x % k == 0:
            s.append('1')
        else:
            s.append('0')
    a = ""
    for i in range(len(s)):
       a += s[i]
    print(a)
