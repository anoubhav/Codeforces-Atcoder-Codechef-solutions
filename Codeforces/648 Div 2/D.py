from sys import stdin, stdout

def isvalid(r, c, n, m):
    if r>=0 and r<= n-1 and c>=0 and c<=m-1:
        return True
    return False

def dfs(matrix, start, end, n, m):
    # return False if cannot reach end from start
    stack = []
    stack.append(start)
    visited = [[0]*m for _ in range(n)]

    while stack:
        r, c = stack.pop()
        visited[r][c] = 1
        if r == end[0] and c== end[1]:
            return True

        if isvalid(r-1, c, n, m) and not visited[r-1][c] and matrix[r-1][c] != '#':
            stack.append([r-1, c])
        if isvalid(r, c-1, n, m) and not visited[r][c-1] and matrix[r][c-1] != '#':
            stack.append([r, c-1])
        if isvalid(r+1, c, n, m) and not visited[r+1][c] and matrix[r+1][c] != '#':
            stack.append([r+1, c])
        if isvalid(r, c+1, n, m) and not visited[r][c+1] and matrix[r][c+1] != '#':
            stack.append([r, c+1])  

    return False

t = int(input())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    matrix = []
    gloc, bloc = [], []
    flag = 0
    for r in range(n):
        row = list(stdin.readline().strip())
        matrix.append(row)
        for c in range(m):
            # ensure adjacent 'G' and 'B' is not there and B is not adjacent to (n, m)
            if row[c] == 'B':
                bloc.append([r, c])
                if (([r, c] in [[n-2, m-1], [n-1, m-2]]) or (isvalid(r-1, c, n, m) and matrix[r-1][c] == 'G') or (isvalid(r, c-1, n, m) and matrix[r][c-1] == 'G') or (isvalid(r, c+1, n, m) and matrix[r][c+1] == 'G')):
                    flag = 1
            elif row[c] == 'G' :
                gloc.append([r, c])
                if (isvalid(r-1, c, n, m) and matrix[r-1][c] == 'B') or (isvalid(r, c-1, n, m) and matrix[r][c-1] == 'B') or (isvalid(r, c+1, n, m) and matrix[r][c+1] == 'B'): flag = 1
    
    # if adjacent GB or B next to (n, m)
    if flag and len(gloc)>0:
        print('No')
        continue

    # no good people
    if len(gloc) == 0:
        print('Yes')

    # no bad people; yes if all good can reach
    elif len(bloc) == 0:
        ans = 'Yes'
        for start in gloc:
            if not dfs(matrix, start, [n-1, m-1], n, m):
                ans = 'No'
                break
        print(ans)
    
    # if no good no bad; all conditions satisfy
    elif len(gloc) == 0 and len(bloc) == 0:
        print('Yes')

    # good and bad people in maze
    else:
        # surround bad people with walls if nbr is empty and exists.
        for start in bloc:
            r, c = start
            if isvalid(r, c-1, n, m) and matrix[r][c-1] == '.':
                matrix[r][c-1] = '#'
            if isvalid(r-1, c, n, m) and matrix[r-1][c] == '.':
                matrix[r-1][c] = '#'
            if isvalid(r+1, c, n, m) and matrix[r+1][c] == '.':
                matrix[r+1][c] = '#'
            if isvalid(r, c+1, n, m) and matrix[r][c+1] == '.':
                matrix[r][c+1] = '#'

        # check all good people can reach (n, m)
        ans = 'Yes'
        for start in gloc:
            if not dfs(matrix, start, [n-1, m-1], n, m):   
                ans = 'No'
                break
        print(ans)

        
        

    
    
