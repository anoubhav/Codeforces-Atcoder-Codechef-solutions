# 9 mins.  No errors. Good.
# The only observation we need is that we don't need to jump left at all. This only decreases our position so we have less freedom after the jump to the left. Then, to minimize d, we only need to jump between the closest 'R' cells. Find the maximum distance between two R's. That is the answer.

from sys import stdin
t = int(input())
for _ in range(t):
    string = stdin.readline().strip()

    maxdist = 1
    prev = -1 # starts at 0, but 0 indexing so made it -1
    for i, char in enumerate(string):
        if char == 'R':
            maxdist = max(maxdist, i - prev)
            prev = i

    # (n+1) to last R distance
    maxdist = max(maxdist, len(string) - prev)
    print(maxdist)


