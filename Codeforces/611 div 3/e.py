from collections import defaultdict as dd
from sys import stdin
n = int(input())
nums = list(map(int, stdin.readline().split()))

nums.sort()

freq = dd(int)
for i in nums:
    freq[i] += 1

maxset = set()
minset = set()

ind = 0
while ind < n:
    curr = nums[ind]
    if curr in minset:
        # leave as it is
        pass
    elif (curr - 1) in minset:
        # change all to curr-1
        pass
    else:
        # change all to curr + 1 (g et it closer to the next larger value)
        minset.add(curr+1)
    ind += freq[curr]

ind = 0
while ind < n:
    curr = nums[ind]
    if freq[curr] == 1:
        if (curr-1) not in maxset:
            maxset.add(curr-1)
        else:
            if (curr) not in maxset:
                maxset.add(curr)
            else:
                maxset.add(curr+1)

    elif freq[curr] == 2:
        if (curr-1) not in maxset:
            maxset.add(curr-1)
            if (curr) not in maxset:
                maxset.add(curr)
            else:
                maxset.add(curr+1)
        else:
            maxset.add(curr)
            maxset.add(curr+1)
    
    else:# freq >= 3; put all possibilities into set
        maxset.add(curr-1)
        maxset.add(curr)
        maxset.add(curr+1)

    ind += freq[curr]

print(len(minset), len(maxset))
    

        
