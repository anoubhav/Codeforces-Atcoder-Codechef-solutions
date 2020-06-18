# editorial solution: Let i be the greatest integer such that 2^i divides TS. Then answer is floor(TS/(2^(i+1))). 

# Time complexity: Find the highest power of two in TS. O(log(TS))

# my solution
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
            curr = 1<<(pow2+1) # I did that, but I broke it down to more if/else statements which were not required as this formula solves all those cases.
            ans = ts//curr

    print(ans)
            
# tester's code
q = int(input())
while q > 0:
    ts = int(input())
    while ts % 2 == 0:
        ts //= 2
    print(ts // 2)
    q -= 1 

        