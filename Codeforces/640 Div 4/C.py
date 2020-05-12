# https://codeforces.com/contest/1352/problems

# 8 mins to solve

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    ans = n*(k//(n-1))
    
    if k%(n-1)==0:
        ans -= 1
    else:
        ans += k%(n-1)

    print(ans)


# From 1 to N, there are N-1 numbers not divisible by N. In every block of N numbers, N-1 are not divisible by N. So if we want K numbers, there must be at least KN−1 blocks.

# Each block with N numbers. Let the number of blocks be B. This will take you to B×N.

# So, from 1 to BN, you have B×(N−1) bad numbers. Count how many more do you need and add that to your current value. If you are already complete, then BN−1 is your Kth Number.