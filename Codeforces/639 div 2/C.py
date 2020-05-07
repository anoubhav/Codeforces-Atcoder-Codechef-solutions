t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    visited = set()
    flag = 1
    for r in range(n):
        new = (r + a[r])%n
        if new in visited:
            print('NO')
            flag = 0
            break
        else:
            visited.add(new)
    if flag: print('YES')

