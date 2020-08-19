t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    s3 = input()
    f = 1
    for i in range(2):
        if s1[i] == s2[i] and s1[i] == 'l' and s2[i + 1] == 'l':
            print('yes')
            f = 0
            break
    if f == 1:
        for i in range(2):
            if s2[i] == s3[i] and s2[i] == 'l' and s3[i + 1] == 'l':
                print('yes')
                f = 0
                break
    if f == 1:
        print('no')
