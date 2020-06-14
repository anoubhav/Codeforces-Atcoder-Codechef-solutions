from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

# Gives TLE
def naive_2D_dp(n, nums):
    # let dp[i][j]: maximum sum of j elements chosen from the first i elements where no two are adjacent.

    # dp[i][j] = max(dp[i-2][j-1] + nums[i], dp[i-1][j]); maximum between selecting the ith element and not selecting it. If we select, we have to use dp[i-2][j-1] to prevent adjacent.

    dp = [[0]*(n//2 + 1) for i in range(n+1)]

    # sum of 0 to select 0 elements
    for i in range(1, n+1):
        dp[i][0] = 0

    # to select one out of one.
    dp[1][1] = nums[0]

    for i in range(1, n+1):
        for j in range(1, i//2 + 1):
            dp[i][j] = max(nums[i-1] + (dp[i-2][j-1] if i>1 and j>0 else 0), dp[i-1][j] if i>0 else 0)

    print(dp[n][n//2])


# Source: https://icode54.blogspot.com/p/dp-1-atcoder-beginner-contest-162.html
def oneD_dp(n, nums):
    # let dp[i] be the maximum sum after picking i/2 elements. Two cases: i is odd, i is even. In both we choose the max from selecting i, and not selecting i.


    # Case 1) i is even (pick exactly i/2 elements): dp[i] = max(dp[i-2] + nums[i], odd indices sum). 
    # 1 2 3 4 5 6. If you pick 6 (i) you check the max of (i-2). If you don't pick 6, to pick i/2 elements you ave to pick the odd indices : 1, 3, 5.

    # Case 2) i is odd (i/2 is same as (i-1)/2 if we don't pick): dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    # odd indices prefix sum needed for even case.
    oddpref = [0]*(n+1)
    oddpref[1] = nums[0]

    for i in range(3, n+1, 2):
        if i%2:
            oddpref[i] += oddpref[i-2] + nums[i-1]
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n+1):
        if i%2 == 0:
            dp[i] = max(dp[i-2] + nums[i-1], oddpref[i-1])
        else:
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
    print(dp[n])

oneD_dp(n, nums)