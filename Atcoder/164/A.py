from sys import stdin, stdout
n, m = map(int, stdin.readline().strip().split())

if m>=n:
    print('unsafe')
else:
    print('safe')