# You are given four positive integers n, m, a, b (1≤b≤n≤50; 1≤a≤m≤50). Find any such rectangular matrix of size n×m that satisfies all of the following conditions: 

# 1 - each row of the matrix contains exactly a ones;
# 2 - each column of the matrix contains exactly b ones;
# 3 - all other elements are zeros.

# If the desired matrix does not exist, indicate this

## note the constrains are small so we don't need to be efficient. We have to fill a 50x50 matrix. T = 1000. 

# Proving existence of matrix: If we want each row to have A ones AND each column to have B ones. We require that number of rows x A = number of columns x B to hold. If not, the matrix does not exist.

# If it does exist for each row ( in n ), we have to distribute 'A' ones amongst m columns. E.g. n = 3, m = 6, a = 2, b = 1 

# _, _, 1, 1, _, _
# _, 1, _, _, 1, _
# 1, _, _, _, _, 1

# <---- m columns ---->

# Apparently, for each row to insert A 1s, if we greedily pick the columns with lowest column sums (and col sum < b), we can fill the matrix.
# from sys import stdin

# t = int(stdin.readline())
# for _ in range(t):
#     n, m, a, b = map(int, stdin.readline().split())

#     if n*a!=m*b:
#         print('NO')
#         continue

#     print('YES')

#     # All 1s special case.
#     if a==b==n==m:
#         for _ in range(n):
#             print('1'*n)
#         continue

#     # initialise with all 0s
#     matrix = [[0]*m for _ in range(n)]

#     for row in range(n):
#         # get the current column sums; zip takes the contents of the input list and transposes them so that each element of the contained lists is produced at the same time. (from stack)

#         colsum  = [sum(x) for x in zip(*matrix)]

#         # pick A columns with the lowest column sums
#         columns = sorted([(ind, cs) for ind, cs in enumerate(colsum)], key = lambda x: x[1])

#         # For this row and A columns assign 1.
#         for col in range(a):
#             matrix[row][columns[col][0]] = 1

#         print(*matrix[row], sep='')


# Rank 16 solution. Fill the matrix row-wise, cyclically.
t = input()
for tt in range(int(t)):
    n, m, a, b = map(int, input().split())
    if n * a == m * b:
        print('YES')
        for i in range(n):
            s = ['0']*m
            for j in range(a):
                s[(i * a + j) % m] = '1'
            print(''.join(s))
    else:
        print('NO')

        
        
