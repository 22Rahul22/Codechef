import math
t = int(input())
for _ in range(t):
    n = int(input())
    flag = 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print("yes")
    else:
        print("no")