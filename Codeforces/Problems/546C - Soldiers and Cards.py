# 546C
# 30 mins. Slow.
from sys import stdin
from collections import deque

n = int(stdin.readline())
k1nums = deque(map(int, stdin.readline().split()))
k2nums = deque(map(int, stdin.readline().split()))

k1nums.popleft()
k2nums.popleft()

flag = 1
ng = 0
# visited = set()
loopcount = 1000  # For n<=10, I assumed the game finished within 1000 moves. The theoretical maximum is 106. As 1000>106, this solution worked.

while k1nums and k2nums and loopcount:
    loopcount -= 1
    top1, top2 = k1nums.popleft(), k2nums.popleft()
    # l = len(k1nums)
    # if (top1, top2, l, n - l) in visited: ## INCORRECT HASH
    #     print(-1)
    #     flag = 0
    #     break
    # else:
    #     visited.add((top1, top2, l, n - l))

    if top1 > top2:
        k1nums.append(top2)
        k1nums.append(top1)
    else:
        k2nums.append(top1)
        k2nums.append(top2)
    
    ng += 1

if loopcount:
    if not k1nums:
        print(ng, 2)
    else:
        print(ng, 1)
else:
    print(-1)   


# Intuition:
# It's easy to count who wins and after how many "fights", but it's harder to say, that game won't end. How to do it?

# Firstly let's count a number of different states that we can have in the game. Cards can be arranged in any one of n! ways. In every of this combination, we must separate first soldier's cards from the second one's. We can separate it in n + 1 places (because we can count the before and after deck case too).

# So war has (n + 1)! states. If we'd do (n + 1)! "fights" and we have not finished the game yes, then we'll be sure that there is a state, that we passed at least twice. That means that we have a cycle, and game won't end.

# After checking this game more accurately I can say that the longest path in the state-graph for n = 10 has length 106, so it is enough to do 106 fights, but solutions that did about 40 millions also passed.