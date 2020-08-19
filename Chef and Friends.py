n = int(input())
arr = ['ch', 'he', 'ef', 'che', 'hef', 'chef']
c = 0
for _ in range(n):
    s = input()
    for i in arr:
        if i in s:
            c += 1
            break
print(c)