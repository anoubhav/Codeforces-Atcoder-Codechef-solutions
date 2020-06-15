from sys import stdin, stdout
n = int(input())
s = set()
for _ in range(n):
    s.add(input())

print(len(s))