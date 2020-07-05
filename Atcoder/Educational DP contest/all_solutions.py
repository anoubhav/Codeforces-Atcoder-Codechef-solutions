# ---------------------------------------------------
# Problem A - 6.5 mins
# n = int(input())
# hlist = list(map(int, input().split()))

# dp = [0]*(n+1)

# for i in range(2, n+1):
#     dp[i] = min(dp[i-1] + abs(hlist[i-2] - hlist[i-1]), dp[i-2] + abs(hlist[i-3] - hlist[i-1]) if i>2 else 10**9)

# print(dp[n])
# ---------------------------------------------------
# Problem B - 9.5 mins
# n, k = map(int, input().split())
# hlist = list(map(int, input().split()))

# dp = [10**9]*(n+1)
# dp[1] = 0

# for i in range(2, n+1):
#     for j in range(1, k+1):
#         if i-j>0:
#             dp[i] = min(dp[i], dp[i-j] + abs(hlist[i-1-j] - hlist[i-1]))
#         else:
#             break

# print(dp[n])
# ---------------------------------------------------
# Problem C - 10 mins
# n = int(input())
# happymat = []
# dp = []
# for _ in range(n):
#     happymat.append(list(map(int, input().split())))
#     dp.append([0]*3)

# # dp[i][j] stores the max happiness after day i ... doing activity j on that day
# dp[0][0] = happymat[0][0]
# dp[0][1] = happymat[0][1]
# dp[0][2] = happymat[0][2]

# for i in range(1, n):
#     for j in range(3):
#         dp[i][j] = happymat[i][j] + max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

# print(max(dp[n-1]))


# Problem C - from errichto --> Save dp state space. you only need previous day values to compute latest state.
# n = int(input())
# happymat = []
# for _ in range(n):
#     happymat.append(list(map(int, input().split())))

# # dp[j] stores the max happiness doing activity j on the current
# dp = [0]*3

# for i in range(n):
#     prev = dp.copy()
#     for j in range(3):
#         dp[j] = happymat[i][j] + max(prev[(j+1)%3], prev[(j+2)%3])

# print(max(dp))
# ---------------------------------------------------
# # Problem D - 10 mins (memo) + 10 mins (iterative) + Errichto solution
# # def memo_knapsack(w, n):
# #     if memo[w][n]!=-1:
# #         return memo[w][n]
# #     else:
# #         if w == 0 or n == 0: return 0 # no capacity knapsack has 0 value; no items has 0 value

# #         if weights[n-1]>w:
# #             # cant include
# #             memo[w][n] = memo_knapsack(w, n-1)
# #             return memo[w][n]

# #         else:
# #             include = values[n-1] + memo_knapsack(w - weights[n-1], n-1)
# #             exclude = memo_knapsack(w, n-1)

# #             memo[w][n] = max(include, exclude)
# #             return memo[w][n]

# # def iterative_knapsack(W, N):
# #     memo = [[0]*(n+1) for _ in range(W + 1)]

# #     for i in range(1, N+1):
# #         for capacity in range(1, W+1):
# #             if weights[i-1] > capacity:
# #                 memo[capacity][i] = memo[capacity][i-1]
# #             else:
# #                 exclude = memo[capacity][i-1]
# #                 include = values[i-1] + memo[capacity-weights[i-1]][i-1]
# #                 memo[capacity][i] = max(include, exclude)

# #     return memo[W][N]

# # n, W = map(int, input().split())
# # weights = []
# # values = []

# # for _ in range(n):
# #     w, v = map(int, input().split())
# #     weights.append(w)
# #     values.append(v)

# # # memo[w][n] - max value we can obtain with capacity w and number of items n
# # memo = [[-1]*(n+1) for _ in range(W + 1)]

# # print(memo_knapsack(W, n))
# # print(iterative_knapsack(W, n))

# n, W = map(int, input().split())

# # dp[i] - the maximum total value of items with total weight exactly i
# dp = [0]*(W+1)   #- O(W)

## O (n*W)
# for _ in range(n):
#     w, v = map(int, input().split())

    ## O(W)
#     for cap in range(W-w, -1, -1):
#         dp[cap+w] = max(dp[cap+w], dp[cap] + v)
    
# ans = 0
# for i in range(W+1): #- O(W)
#     ans = max(ans, dp[i])
# print(ans)

# ---------------------------------------------------
# Problem E - constraints on W went from 10^5 to 10^9. (see 30 min into dp video)
# Try input:
# 1 10**9
# 10**9 10

# Before dp[i] represented the MAX VALUE for weight of knapsack EXACTLY i. But 1<=i<=10**9 is very large.
# Thumb rule is to keep the dimension of the dp small. So we redefine it.

# Let dp[i] be the MIN WEIGHT to get a value EXACTLY i. v of item is less than 1000. There are 100 items. (n<=100). So dp[i] is at most 10**5. Much smaller than 10**9

n, W = map(int, input().split())

weights, values = [], []
valuesum = 0
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
    valuesum += v

# N*W = 100*10**9 = 10**11. We are looking for minimum weight so initializaiton should be large numbers.
# in D , dp was looking for maximum value so intialization was all 0s.

dp = [10**11 + 1]*(valuesum + 1)
dp[0] = 0   # no items for 0 value

for item in range(n):
    w, v = weights[item], values[item]
    for value in range(valuesum - v, -1, -1):
        dp[value + v] = min(dp[value + v], dp[value] + w)

for i in range(valuesum, -1, -1):
    if dp[i] <= W:
        print(i)
        break

