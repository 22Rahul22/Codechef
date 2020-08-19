t = int(input())
for _ in range(t):
    s = input().split(' ')
    a = int(s[0])
    b = s[1]
    week = ['mon','tues','wed','thurs','fri','sat','sun']
    day = [0]*7
    for i in range(week.index(b), week.index(b) + 7):
        if a % 7 == 0:
            day[i % 7] = a // 7
        else:
            day[i % 7] = a // 7 + 1
        a -= 1
    for i in range(7):
        print(day[i], end=" ")