# The problem is reduced to: finding the greatest divisor of n which is <= K. While checking primality (if number if prime) we have to find all divisors as well. 

# Naive solution is to iterate from 1->n, to check if n is prime. But, divisors occur in pairs. e.g. 2*6 = 12. The divisor pair is (2, 6). If (a, b) is the divisor pair. We can prove by contradiction that one of them has to be less than sqrt(n) and other has to be more than sqrt(n). 

# IF (a, b) is a divisor pair of n and a<b:
# Case 1: if a > sqrt(n) and b > sqrt(n) --> a*b>n. Not possible
# Case 2: if a < sqrt(n) and b < sqrt(n) --> a*b<n. Not possible
# Case 3: if a < sqrt(n) and b > sqrt(n)

# Thus, instead of iterating over all N (<=10**9 will give TLE), we can iterate over sqrt(N) to find a and get the other divisor b directly using N/a = b. So this algorithm is O(sqrt(N)) ~ 10**5. We have 100 test cases. Overall O(t*sqrt(N))~10^7, we can solve without TLE.


## TASK: Find the greatest divisor of n which is <= K. Let it be gd. The answer is n/gd.

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    gd = 1

    if k>=n: 
        gd = n
        print(n//gd) # 1

    elif k == 1:
        gd = 1
        print(n//gd)

    else:# non-trivial case

        i = 2 # divisor
        while i*i<=n: # O(sqrt(n)) time complexity

            # if i is a divisor
            if n%i == 0:
                if i<=k: # a
                    gd = max(gd, i)
                if n//i <= k: # b
                    gd = max(gd, n//i)
            i += 1
        
        print(n//gd)






