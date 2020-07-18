import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict

def kahn_top_sort(g, n):
    # g - adjacency list of graph. n - number of vertices. 
    # BFS topological sort

    # Returns the topological order. If graph of N vertices contains a cycle, then the order list will be of length < n.
    from collections import deque
    order = []
    indeg = [0]*n
    for i in range(n):
        for nbr in g[i]:
            indeg[nbr] += 1

    q = deque()
    for i in range(n):
        if indeg[i] == 0: q.append(i)
    
    while q:
        node = q.popleft()
        order.append(node)
        for nbr in g[node]:
            indeg[nbr] -= 1
            if indeg[nbr] == 0: q.append(nbr)
    return order


def dfs_top_sort(g, n):
    # Returns the topological ordering for a DAG. If cycle exists in the graph, it returns an empty list.
    def topsort(g, node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        
        visited[node] = 1
        for nbr in g[node]:
            if topsort(g, nbr):
                return True
        visited[node] = 2
        stk.append(node)
        return False
    
    visited = [0]*n # 0 - unvisited, 1 - on call stack, 2 - explored
    stk = [] # topsort
    
    for i in range(n):
        if visited[i] == 0:
            # if it contains cycle
            if topsort(g, i): 
                return []
    
    return stk[::-1]

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dg_edgelist = []
        all_edgelist = []

        for _ in range(m):
            t, x, y = map(int, input().split())
            all_edgelist.append([x - 1, y - 1])
            if t == 1: dg_edgelist.append([x - 1, y - 1])

        g = defaultdict(list)
        for a, b in dg_edgelist:
            g[a].append(b)
        
        # topsort = dfs_top_sort(g, n)
        topsort = kahn_top_sort(g, n)
        # print(dfs_top_sort(g, n), kahn_top_sort(g, n))

        if len(topsort) == n:
            print('YES')

            order = [0]*n

            for i, node in enumerate(topsort):
                order[node] = i
            
            for i in range(m):
                x, y = all_edgelist[i]
                if order[x] > order[y]:
                    all_edgelist[i] = [y, x]
            
            for edge in all_edgelist:
                print(edge[0] + 1, edge[1] + 1)

        else:
            print('NO')
        
        



        




































# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion
 
if __name__ == "__main__":
    main()