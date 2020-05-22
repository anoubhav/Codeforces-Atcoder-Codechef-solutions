# Problem D - 10 mins (memo) + 10 mins (iterative) + Errichto solution
def memo_knapsack(w, n):
    if memo[w][n]!=-1:
        return memo[w][n]
    else:
        if w == 0 or n == 0: return 0 # no capacity knapsack has 0 value; no items has 0 value

        if weights[n-1]>w:
            # cant include
            memo[w][n] = memo_knapsack(w, n-1)
            return memo[w][n]

        else:
            include = values[n-1] + memo_knapsack(w - weights[n-1], n-1)
            exclude = memo_knapsack(w, n-1)

            memo[w][n] = max(include, exclude)
            return memo[w][n]

def iterative_knapsack(W, N):
    memo = [[0]*(n+1) for _ in range(W + 1)]

    for i in range(1, N+1):
        for capacity in range(1, W+1):
            if weights[i-1] > capacity:
                memo[capacity][i] = memo[capacity][i-1]
            else:
                exclude = memo[capacity][i-1]
                include = values[i-1] + memo[capacity-weights[i-1]][i-1]
                memo[capacity][i] = max(include, exclude)

    return memo[W][N]

n, W = map(int, input().split())
weights = []
values = []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# memo[w][n] - max value we can obtain with capacity w and number of items n
memo = [[-1]*(n+1) for _ in range(W + 1)]

print(memo_knapsack(W, n))
print(iterative_knapsack(W, n))

# ----------------------------------------------
# Errichto solution: 1D DP - O(n*W)

n, W = map(int, input().split())

# dp[i] - the maximum total value of items with total weight EXACTLY i
dp = [0]*(W+1)

for _ in range(n):
    w, v = map(int, input().split())
    
    # reverse order is important for 0/1. if we go dp[0] --> dp[3] --> dp[6], than item with weight 3 will get 
    # repeated twice for dp[6], but reverse we will only encounter each item once for each dp[i]

    for cap in range(W-w, -1, -1): 
        dp[cap+w] = max(dp[cap+w], dp[cap] + v)
    
# the maximum total value of items with total weight EXACTLY i
ans = 0
for i in range(W+1):
    ans = max(ans, dp[i])
print(ans)