def binc(x,y):
    a = bin(x).replace("0b", "")
    b = bin(y).replace("0b", "")
    aplusb = a + b
    bplusa = b + a
    ab = int(aplusb, 2)
    ba = int(bplusa, 2)
    return(ab-ba)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            m.append(binc(arr[i],arr[j]))
    print(max(m))

