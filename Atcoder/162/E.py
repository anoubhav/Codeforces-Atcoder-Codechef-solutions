# could not solve. Very interesting math question.
n, k = map(int, input().split())
mod = 10**9 + 7
# For each X, in 1<= X <= K, let us find the number of sequences {A1, A2, .., An} with GCD = X. 

# The necessary and sufficient condition of the greatest common divisor being a multiple of X
# is that all the A1, ..., AN are multiples of X. The number of such sequences is (floor(K/X))^N.
# The necessary and sufficient condition of it being **exactly** X is that it is a multiple of X, but
# not 2X, 3X.... If they are calculated in the **decreasing order** of X, it can be found by subtracting the number of those of 2X, 3X.
# video: https://www.youtube.com/watch?v=CYfEsdTr1pA

# Let dp[i] store the number of sequences whose GCD is i.
dp = [0]*(k+1)
for i in range(k, 0, -1):
    # no. of sequences whose gcd is a multiple of i.
    dp[i] = pow(k//i, n, mod)

    # no. of sequences whose gcd is exactly i. 
    for j in range(2*i, k+1, i):
        dp[i] -= dp[j]

ans = 0
for i in range(1, k+1):
    ans += (i*dp[i])%mod
print(ans%mod)




