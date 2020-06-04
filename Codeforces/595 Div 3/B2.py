# Unsolved in contest. O(N^2) solution would not work as N<=2*10^5. Did not notice the cyclic nature of the problem. Barely recognized the first problem itself.

from sys import stdin, stdout
from collections import defaultdict
q = int(input())
for _ in range(q):
    n = int(input())
    nums = list(map(int, stdin.readline().strip().split()))

    nums = [0] + nums
    ans = []

    visited = defaultdict(int)

    for i in nums[1:]:
        if not visited[i]:
            count = 1
            found = nums[i]
            cycle = [i, found]
            while found!=i:
                found = nums[found]
                count += 1
                cycle.append(found)
            
            for el in cycle:
                visited[el] = count
            ans.append(count)
        else:
            ans.append(visited[i])

    print(*ans)


    

