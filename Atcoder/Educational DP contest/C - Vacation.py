# Solved in 10 mins

n = int(input())
happy_mat = []
for _ in range(n):
    happy_mat.append(list(map(int, input().split())))

# max happiness after i days doing (a, b, c) on that day is in dp[i][0/1/2]
dp = [[0]*3 for _ in range(n+1)]

dp[1][0] = happy_mat[0][0]
dp[1][1] = happy_mat[0][1]
dp[1][2] = happy_mat[0][2]

for day in range(2, n+1):
    for activity in range(3):
        dp[day][activity] = max(dp[day-1][(activity+1)%3], dp[day-1][(activity+2)%3]) + happy_mat[day-1][activity]

print(max(dp[n]))

# ---------------------------------------------------------
# Reduce the state space of DP - Errichto
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




