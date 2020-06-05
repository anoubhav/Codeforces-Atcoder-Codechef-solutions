t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [[0]*n for _ in range(n)]

    parity = 0
    parity_last = {0: 2, 1: 1}
    for diag in range(2*n - 1):
        parity +=1 # start with odd
        start = parity_last[parity%2]

        beg = max((diag+1)-n, 0)
        end = min(diag+1, n)

        for i in range(beg, end):
            j = diag - i
            matrix[i][j] = start
            start += 2
        
        parity_last[parity%2] = start

    for row in matrix:
        print(*row)
        

