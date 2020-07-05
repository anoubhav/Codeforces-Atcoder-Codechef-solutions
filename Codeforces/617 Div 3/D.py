from sys import stdin, stdout
from math import ceil
n, a, b, k = map(int, stdin.readline().strip().split())
hlist = list(map(int, stdin.readline().strip().split()))

score = 0
lose_rems = []

for h in hlist:
    t = h%(a+b)
    if t == 0 or t>a:
        # lose
        # get the remainders when it is your turn
        if t==0:
            lose_rems.append(b)
        else:
            lose_rems.append(t-a)

    else:
        # win
        score += 1

# its easier to finish smaller rems first
lose_rems.sort()
for rem in lose_rems:
    skips = ceil(rem/a)
    if k - skips >=0:
        score += 1
        k -= skips
    else:
        break

print(score)


