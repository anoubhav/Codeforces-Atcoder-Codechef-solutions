from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n = int(input())
    # n, x = map(int, stdin.readline().strip().split())
    nums = list(map(int, stdin.readline().strip().split()))

    e, o = 0, 0
    for i in nums:
        if i%2==0: e+= 1
        else: o+= 1
    
    if o == 0:
        print('NO')
    elif n%2==0 and e==0:
        print('NO')
    else:
        print('YES')