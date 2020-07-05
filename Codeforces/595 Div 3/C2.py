def greedy():
    # For C2, I used a simpler greedy approach. First, I find the smallest number that is the sum of all powers of 3 till the sum becomes >= n. Let us call the sum Z. So this will lead to a number of form 111111 where 1 => The corresponding power of 3 is added to the sum. Now, suppose the highest power of 3 that was included in the sum is m. I go from mth to 0th power and try to subtract corresponding power from current Z. If it leads to a number that is still >= n, we reduce Z by the current power. Else, we continue. Intuition is that if we subtract a larger power, its sum is anyways going to be larger than the sum of all lower powers combined. So it will be a better choice for sure.

    from sys import stdin
    q = int(stdin.readline().strip())
    for _ in range(q):
        n = int(stdin.readline().strip())

        s = 0
        for i in range(n):
            s += 3**i
            if s >= n:
                break
        
        # i has the greatest power added.
        while s >= n and i>=0:
            if s - 3**i >= n:
                s -= 3**i
            i-=1
        
        print(s)

def binaryTernary():
    from sys import stdin

    q = int(stdin.readline().strip())
    for _ in range(q):
        n = int(stdin.readline().strip())

        lo, hi = 1, n
        ans = None
        while lo<=hi:
            mid = lo + (hi - lo)//2
            
            t = int(bin(mid)[2:], 3)
            if t >= n:
                ans = t
                hi = mid - 1
            else:
                lo = mid + 1
        print(ans)

def editorial():
    from sys import stdin
    q = int(stdin.readline().strip())
    for _ in range(q):
        n = int(stdin.readline().strip())

        def ternary(n):
            if n==0: return '0'
            tern = ''
            while n!=0:
                n, r = divmod(n, 3)
                tern += str(r)
            return tern
        
        tern = ternary(n)

        if '2' not in tern:
            print(n)
            continue
        
        tern = '0' + tern
        ans = tern
        t = tern.find('2')

        while t!=-1:
            ans = ans[:t-1] + str(int(ans[t-1])+1) + '0'*len(ans[t:])
            t = ans.find('2')

        print(int(ans,3))


            
        


editorial()


# greedy()
# binaryTernary()


