t = int(input())
for _ in range(t):
    s = input()
    a = s.count('a')
    b = s.count('b')
    m = max(a, b)
    print(len(s) - m)
    