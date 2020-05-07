t = int(input())

import math

def get_max_ph(tot):
    # quadratic formula; get the height of the highest pyramid that can be constructed using 'tot' cards
    h = (-1 + math.sqrt(1 + 24*tot))//6
    if h == 0:
        return -1
    return tot - (3*h**2 + h)/2 # subtract those number of cards from tot and return

for _ in range(t):
    tot = int(input())
    count = 0
    # repeat the loop until tot number of available cards < 2.
    while tot>1:
        tot = get_max_ph(tot)
        count += 1
    print(count)

