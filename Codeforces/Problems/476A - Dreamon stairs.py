# You have to climb n steps.
# You can climb 1 or 2 steps each move.
# You want number of moves to be a multiple of m, i.e., num_moves : {0, m, 2m 3m, 4m..., km, ...}

# Let's say you make m moves. num_moves = m. Then, m <= possible_steps <= 2*m. As at each move you can make either 1 or 2 steps.

# If you make k*m moves for some integer k. num_moves = km. Then, k*m<= possible_steps <= 2*k*m.

# We want to find the smallest k, for which n lies in [k*m, 2*k*m]. And thus, num_moves (answer) = k*m

# k*m <= n <= 2*k*m
# k <= (n/m) and k >= (n/2m)

# We want the smallest k. So only the condition, k>=(n/2m) is useful in finding the smallest value. If they wanted us to find the largest k, then k<=(n/m) would be useful. 

# So, k>=(n/2m) --> k = ceil(n/2m).

# Num_moves = k*m

# Side note: When does -1 happen? Only when n < m and n!=0. If n > m, you will always find a [k*m, 2*k*m] range in which it will belong.

from math import ceil
n, m = map(int, input().split())

if n < m: 
    print(-1)
else:
    print(m*ceil(n/(2*m)))
