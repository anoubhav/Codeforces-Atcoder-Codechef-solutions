# https://codeforces.com/contest/1352/problems

# 12 mins to solve
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    # if n is odd
    if n%2 == 1:
        if k%2 == 0:
            print('NO')
            continue
        else:
            # numbers are odd
            if n<k:
                print('NO')
                continue

            print('YES')

            print(' '.join(['1' for i in range(k-1)] + [str(n - (k-1))]))
    
    # if n is even
    elif n%2 == 0:
        if k%2 == 1:
            # numbers are even
            if n<2*k:
                print('NO')
                continue

            print('YES')

            print(' '.join(['2' for i in range(k-1)] + [str(n - 2*(k-1))]))

        else:
            # numbers are odd/even
            if n<k:
                print('NO')
                continue   
            
            print('YES')

            print(' '.join(['1' for i in range(k-1)] + [str(n - (k-1))]))
    


