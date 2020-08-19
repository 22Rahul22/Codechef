t = int(input())
for _ in range(t):
    s = input()
    arr = []
    a = "><"
    for i in range(len(s)):
        if s[i] == '>':
            arr.append('<')
        elif s[i] == '<':
            arr.append('>')
        else:
            arr.append(s[i])
    s = ""
    for i in arr:
        s += i
    print(s.count(a))