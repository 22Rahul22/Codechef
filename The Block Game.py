t = int(input())
for _ in range(t):
    n = input()
    x = ""
    for i in range(len(n)-1, -1, -1):
        x += n[i]
    if x == n:
        print("wins")
    else:
        print("losses")
