import math
t = int(input())
for _ in range(t):
    n = int(input())
    y = n % 8
    if 1 <= y <= 6:
        if y == 1:
            s = str(n+3) + 'LB'
        elif y == 4:
            s = str(n-3) + 'LB'
        elif y == 2:
            s = str(n+3) + 'MB'
        elif y == 5:
            s = str(n-3) + 'MB'
        elif y == 3:
            s = str(n+3) + 'UB'
        else:
            s = str(n-3) + 'UB'
    else:
        if y == 7:
            s = str(n+1) + 'SU'
        else:
            s = str(n-1) + 'SL'
    print(s)