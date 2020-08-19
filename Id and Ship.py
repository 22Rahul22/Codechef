t = int(input())
for _ in range(t):
    s = input().upper()
    a = ['', 'BattleShip', 'Cruiser', 'Destroyer', '', 'Frigate']
    print(a[ord(s)-65])