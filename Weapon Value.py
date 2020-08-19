t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*10
    for i in range(n):
        s = input()
        for j in range(len(s)):
            a[j] = (ord(s[j]) - 48) ^ a[j]
    print(a.count(1))