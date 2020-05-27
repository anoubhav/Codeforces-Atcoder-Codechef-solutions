from sys import stdin, stdout

t = int(input())
 
for _ in range(t):
    x1, y1, x2, y2 = map(int, stdin.readline().strip().split())
    
    print((x2-x1)*(y2-y1) + 1) 

# from sys import stdin, stdout
# from collections import defaultdict
# from math import factorial
# t = int(input())
# # ans = []
# # dp = defaultdict(int)

# for _ in range(t):
#     x1, y1, x2, y2 = map(int, stdin.readline().strip().split())

#     # dp[x][y]: be the # of paths to reach (x, y) from (0, 0)
#     m, n = x2, y2
#     if x1 == m or y1 == n:
#         # ans.append(1)
#         print(1)
#         continue

#     m -= (x1 - 1)
#     n -= (y1 - 1)

#     # ans.append(factorial(m+n-2)//(factorial(n-1)*factorial(m-1)))
#     t = factorial(m+n-2)//(factorial(n-1)*factorial(m-1))

#     mi = min(m, n)
#     if mi>=3:
#         if mi%2==0:
#             mi -= 1
#         same = mi//2

#         # num paths from mi, mi to m, n: (0, 0) --> 
#         t1 = x2 - (mi - 1)
#         t2 = y2 - (mi - 1)

#         p = factorial(t1+t2-2)//(factorial(t1-1)*factorial(t2-1))
#         print(t - same*p)
    
#     else:
#         print(t)

        

#     # paths from mi, mi


#     # if (x2, y2) in dp:
#     #     ans.append(dp[x2, y2])
    
#     # else:
#     #     for row in range(1, x2+1):
#     #         for col in range(1, y2+1):
#     #             if row == 1 or col == 1:
#     #                 dp[row, col] = 1
#     #             else:
#     #                 dp[row, col] = dp[row-1, col] + dp[row, col-1]
        
#     #     ans.append(dp[x2, y2])
# # print(*ans, sep = '\n')