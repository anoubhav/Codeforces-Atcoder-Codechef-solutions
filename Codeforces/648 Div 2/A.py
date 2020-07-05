from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    tot = 0
    usedcols = set()
    for row in range(n):
        r = input()
        if '1' in r: 
            tot += 1
        rnums = list(map(int, r.split()))
        for i in range(m):
            if rnums[i] == 1:
                usedcols.add(i)


    if n - tot <=0:
        print('Vivek')
    elif len(usedcols) == m:
        print('Vivek')
    else:
        left = n - tot
        left2 = m - len(usedcols)

        left = min(left, left2)

        if left%2==1:
            print('Ashish')
        else:
            print('Vivek')

