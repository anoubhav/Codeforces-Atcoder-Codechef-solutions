t = int(input())
for _ in range(t):
    ts = int(input())

    if ts%2==1:
        ans = len(range(2, ts+1, 2))
    else:
        temp = ts
        pow2 = 0
        while temp%2 == 0:
            temp >>= 1
            pow2 += 1
        
        if temp == 1:
            ans = 0
        else:
            ans = 0
            curr = 1<<(pow2+1)
            ans = ts//curr

    print(ans)
            

        