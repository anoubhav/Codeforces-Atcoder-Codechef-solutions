from sys import stdin, stdout
a, b, c ,d = map(int, stdin.readline().strip().split())

# simulation
i = 0
while a>0 and c>0:
    if i%2 == 0:
        c -= b
    else:
        a -= d
    i+=1

if a <= 0:
    print('No')
else:
    print('Yes')

# math. Let x and y be the number of turns required to reduce the health of T's monster and A's monster to 0.
from math import ceil
x = ceil(a/d)
y = ceil(c/b)

if x>=y:
    print('Yes')
else:
    print('No')