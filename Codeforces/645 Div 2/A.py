from sys import stdin, stdout
t = int(input())
for _ in range(t):
    # n = int(stdin.readline())
    n, m = map(int, stdin.readline().strip().split())

    print((n*m)//2 + (n*m)%2)

