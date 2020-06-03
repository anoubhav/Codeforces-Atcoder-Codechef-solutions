# https://codeforces.com/blog/entry/78195
N, S = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
dp = [[0 for j in range(S + 1)] for i in range(N + 1)]
dp[0][0] = 1

# dp[i][j] is the answer over all subsets of the first i elements of the array A that sum to j.
for i in range(N) : 
    for j in range(S + 1) : 
        #  If we skip A[i], we can place in subset or not (two options)
        dp[i + 1][j] += 2 * dp[i][j]
        dp[i + 1][j] %= mod 

        # If we pick A[i], increase the sum by A[i] and no. of elements by i.
        if j + A[i] <= S : 
            dp[i + 1][j + A[i]] += dp[i][j]
            dp[i + 1][j + A[i]] %= mod
            
print(dp[N][S])






# Given a sequence A, find number of subsets whose sum is S
def my_attempt():
    # I just calculated the subset of numbers who sum to S.
    n, S = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[-1]*(n+1) for _ in range(S+1)]
    def subsetSum(s, n, arr, v):
        if dp[s][n]!=-1:
            return dp[s][n]
        else:
            if s == 0:
                return 1
            elif s!=0 and n==0:
                return 0
            else:
                if arr[n-1] > s:
                    dp[s][n] = subsetSum(s, n-1, arr, v)
                    return dp[s][n]
                else:
                    exclude = subsetSum(s, n-1, arr, v)

                    v1 = v.copy()
                    v1.append(arr[n-1])
                    include = subsetSum(s - arr[n-1], n-1, arr, v1)


                    dp[s][n] = include + exclude
                    return dp[s][n]

    v = []
    print('Number of subsets whose elements add upto S:', subsetSum(S, n, arr, v))

    
