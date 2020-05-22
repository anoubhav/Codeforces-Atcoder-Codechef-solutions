# 15 mins to solve both types of DP.
# This solution does NOT give errichto TLE coz he used C++.

n, k = map(int, input().split())
hlist = list(map(int, input().split()))

# dp[i] stores the minimum cost to reach step i (starting from step 1) i: 1->N
dp = [10**9]*(n+1)
dp[1] = 0

## TLE : backward fill
for i in range(2, n+1):
    for ss in range(1, k+1): # ss: step size
        if i-ss >= 1:
            dp[i] = min(dp[i], dp[i-ss] + abs(hlist[i-1] - hlist[i - ss - 1]))
        else:
            break

print(dp[n])

# dp[i] stores the minimum cost to reach step i (starting from step 1) i: 1->N
dp = [10**9]*(n+1)
dp[1] = 0
## TLE: forward fill
for i in range(n+1):
    for ss in range(i+1, i+k+1):
        if ss<=n:
            dp[ss] = min(dp[ss], dp[i] + abs(hlist[i-1] - hlist[ss - 1]))
        else:
            break

print(dp[n])