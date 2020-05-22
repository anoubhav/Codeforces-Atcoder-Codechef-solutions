# 7 mins to solve; 0 submission errors

n = int(input())
hlist = list(map(int, input().split()))

# The minimum cost to reach step i (1->n)
dp = [0]*(n+1)
dp[1] = 0 # 1->1

for i in range(2, n+1):
    dp[i] = min(dp[i-1] + abs(hlist[i-2] - hlist[i-1]), (dp[i-2] + abs(hlist[i-3] - hlist[i-1]) if i>2 else 10**9))

print(dp[n])
