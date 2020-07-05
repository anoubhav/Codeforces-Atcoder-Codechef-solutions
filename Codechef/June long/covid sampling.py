t = int(input())
for _ in range(t):
    n, p = map(int, input().split())

    ## Ask queries
    while True:
        # print(1, r1, r2, c1, c2)
        # X denotes no. of infected people in [r1:r2+1][c1:c2+1]
        X = input()
        # invalid query or ran out of Q queries
        if X == -1: 
            exit()

        else:
            # Execute your algorithm, if found the matrix, break out of loop
            pass

        

    ## Now you know the matrix A, print it.
    # print(2)
    # for row in range(n):
    #     print(matrix[row])

    ## Check if your answer is correct
    # X = input()
    # if X == 1: continue
    # else: exit()
