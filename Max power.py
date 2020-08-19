n = int(input())
s = input()
c = 0
for i in range(n-1, -1, -1):
    if s[i] == '0':
        c += 1
    else:
        break
print(c)