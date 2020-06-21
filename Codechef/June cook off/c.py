from sys import stdin, setrecursionlimit

def is_close(a, b, prec):
    return f'{a:.{prec}f}' == f'{b:.{prec}f}'

t = int(input())

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    incomes = list(map(int, stdin.readline().split()))
    pops = list(map(int, stdin.readline().split()))

    g = [[]*n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    
    ratio = []
    mx = 0
    for i in range(n):
        t = incomes[i]/pops[i]
        ratio.append((t, i))
        if t> mx: mx = t
    
    del incomes, pops

    special = set()
    for i in range(n):
        if is_close(mx, ratio[i][0], prec = 4):
            special.add(ratio[i][1])
    
    del ratio

    visited = [0]*n

    ans = 1
    anspath = []
    for i in special:
        if not visited[i]:
            numsp_inpath = 1
            path = [i+1]
            stk = [i]
            while stk:
                node = stk.pop()
                visited[node] = 1
                for nbr in g[node]:
                    if not visited[nbr] and nbr in special:
                        numsp_inpath += 1
                        path.append(nbr+1)
                        stk.append(nbr)   
                        visited[nbr] = 1 

            if numsp_inpath > ans:
                ans = numsp_inpath
                anspath = path.copy()
    
    print(ans)
    print(*anspath)
    



