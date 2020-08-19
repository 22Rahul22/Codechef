t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    if n == 1:
        print(0)
    else:
        for i in range(n - 1):
            if s[i] not in vowels and s[i + 1] in vowels:
                c += 1
        print(c)