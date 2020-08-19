import math


def isPrime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return 0
    return 1


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    sum = x + y
    t = True
    while t:
        if isPrime(sum) and sum != x + y:
            print(sum - x - y)
            break
        else:
            sum += 1
