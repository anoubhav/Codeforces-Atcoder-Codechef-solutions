# We are given the final state of battlefied matrix. We have to verify whether such a final state (after all cannons fired) is even possible or not. Output: 'YES' or 'NO'.

## Valid configuration
# 0011
# 0010

# If A[i][j] (row, col) is 1, then there MUST be ATLEAST one of the below scenarios

#  1) the polygon border on its right or a 1, i.e., A[i][j+1] must be the border or 1
#  2) the polygon border below it or a 1, i.e.,  A[i+1][j] must be the border or 1.

# If NONE of the above are true, then the cannon shot (of 1) WILL NOT stop at A[i][j]. Thus, making it an invalid configuration.

## invalid configuration
# 00100
# 01000

## TASK: Print if matrix configuration is valid

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []

    for r in range(n):
        row = [int(i) for i in input()]
        matrix.append(row)

    # As t<=1000 and matrix dim <= 50. We can use brute force, by iterating over all rows and columns, i.e., O(N^2) solution for each test case. Yielding overall # of operations of 1000*50*50, well below time limit.

    ans = 'YES'
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 1:
                if row == n-1 or col == n-1:
                    # valid
                    pass
                elif matrix[row+1][col] == 1 or matrix[row][col+1] == 1:
                    # valid
                    pass
                else:
                    # invalid
                    ans = 'NO'
                    break
    print(ans)





