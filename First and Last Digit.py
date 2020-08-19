t = int(input())
for _ in range(t):
    n = input()
    c = len(n)
    f = ord(n[0]) - 48
    l = ord(n[c-1]) - 48
    print(f+l)