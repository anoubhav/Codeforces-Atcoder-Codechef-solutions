from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n, m, x, y = map(int, stdin.readline().split())

    tot = 0
    for row in range(n):
        row = stdin.readline().strip()
        i = 0
        while i < m:
            if row[i] == '*':
                i += 1
                continue
            else:
                if i+1 < m and row[i+1] == '.':
                    tot += min(2*x, y)
                    i += 2
                else:
                    tot += x
                    i += 1
    print(tot)



