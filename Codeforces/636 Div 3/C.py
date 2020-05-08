# Solved in competition
# Algopedia DP solution: https://www.youtube.com/watch?v=ppk9pXL9rR4&t=18s
t = int(input())
import math

def my_soln(n, seq):
    prev = seq[0]
    totsum = 0
    for i, curr in enumerate(seq):
        # if current element has same sign as prev, greedily store the largest element
        if curr*prev > 0:
            prev = max(curr, prev)

        # if current element has different sign than prev, update sum with with sign' maximum and store this new elem
        elif curr*prev < 0:
            totsum += prev
            prev = curr
    
    # Sum is only updated on switch in sign; hence add the last maximum element
    totsum += prev

    print(totsum)    

for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))

    # Greedy approach
    my_soln(n, seq)



