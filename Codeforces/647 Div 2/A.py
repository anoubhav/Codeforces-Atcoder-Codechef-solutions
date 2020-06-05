# Did not get in contest, due to floating point precision error. Next time we very careful about using / backslash or // backslash. This ruined the entire contest as not gettting A really hit me. -60 points in the contest.
import math
def shift_operations():
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        if a==b:
            print(0)
            continue
        if a<b: a, b = b, a

        if a%b!=0:
            print(-1)
            continue

        numshifts = 0
        while a > b and a & 1 !=1:
            numshifts += 1
            a >>= 1
        
        if a!=b:
            print(-1)
        else:
            print(math.ceil(numshifts/3))
        
shift_operations()

def my_soln():
    # Very sensitive to extra backslash/ in division
    
    def primeFactors(n): 
        ans = []
        # Print the number of two's that divide n 
        while n % 2 == 0: 
            ans.append(2) 
            n = n>>1
        
        if int(n)!=1:
            return [-1]
        else:
            return ans

    from sys import stdin, stdout
    q = int(input())
    for _ in range(q):
        a, b = map(int, stdin.readline().strip().split())

        if a == b:
            print(0)
            continue

        if a<b:
            a, b = b, a
        
        if a%b!=0:
            print(-1)
        
        else:
            pfactors = primeFactors(a//b)

            if pfactors == [-1]:
                print(-1)
            else:
                twos = len(pfactors)
                ans = 0
                q, r = divmod(twos, 3)
                ans += q
                twos = r
                q, r = divmod(twos, 2)
                ans += q
                twos = r
                q, r = divmod(twos, 1)
                ans += q

                print(ans)