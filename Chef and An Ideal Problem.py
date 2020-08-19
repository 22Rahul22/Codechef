n = int(input())
print(n)
a = int(input())
if (n != 1 and a != 2) or (n != 2 and a != 1):
    print(abs(a - n))
else:
    print(3)