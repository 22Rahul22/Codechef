t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if 'I' in s and 'Y' not in s:
        print("INDIAN")
    elif 'Y' in s and 'I' not in s:
        print("NOT INDIAN")
    else:
        print("NOT SURE")