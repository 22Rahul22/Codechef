t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    p, q, r = map(int, input().split())
    ad = [0]*3
    m = [0]*3
    ad[0] = p - a
    ad[1] = q - b
    ad[2] = r - c
    m[0] = p / a
    m[1] = q / b
    m[2] = r / c
    while a != p or b != q or c != r:
