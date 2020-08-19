t = int(input())
for _ in range(t):
    s = input().split(" ")
    n = int(s[0])
    p = s[1]
    arr = list(map(int, input().split()))
    if p == 'Dee' and n == 1 and arr[0] % 2 == 0:
        print('Dee')
    else:
        print('Dum')