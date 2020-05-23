# 259B - 10 mins. Good.
from sys import stdin
sq= []
for _ in range(3):
    sq.append(list(map(int, stdin.readline().split())))

new = sq.copy()
# stupid edge case mistake; did not include 10**5
for i in range(1, 10**5+1):
    firstcol = i + sq[0][1] + sq[0][2]
    # check if center
    j = firstcol - sq[1][0] - sq[1][2]
    k = firstcol - sq[2][0] - sq[2][1]

    if 0<j<=10**5 and 0<k<=10**5 and i+j+k==firstcol and sum(sq[0] + [i]) == firstcol and sum(sq[1] + [j]) == firstcol and sum(sq[2] + [k]) == firstcol:
        new[0][0] = i
        new[1][1] = j
        new[2][2] = k
        break
    # check if right corner

for row in new:
    print(*row)

    