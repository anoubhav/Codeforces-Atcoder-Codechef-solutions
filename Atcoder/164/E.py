from sys import stdin, stdout
q = int(input())
for _ in range(q):
    n = int(input())
    n, m = map(int, stdin.readline().strip().split())
    nums = list(map(int, stdin.readline().strip().split()))