def dfs(g, start):
     # gives RE due to recursion depth
    visited[start] = True
    # cc.append(0)
    for nbr in g[start]:
        if not visited[nbr]:
            dfs(g, nbr)


from collections import defaultdict, deque
n, m = map(int, input().split())
g = defaultdict(set)

# If no connections; put them in one group
if m == 0:
    print(1)

else:
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].add(b - 1)
        g[b - 1].add(a - 1)


    visited = [False]*n
    ans = 0
    for i in range(n):
        if not visited[i]:
            # cc = []
            count = 1
            q = deque([i])
            visited[i] = 1
            while q:
                node = q.pop()
                for nbr in g[node]:
                    if not visited[nbr]:
                        q.append(nbr)
                        visited[nbr] = True
                        count += 1
                
            # ans = max(ans, len(cc))
            ans = max(ans, count)

    print(ans)