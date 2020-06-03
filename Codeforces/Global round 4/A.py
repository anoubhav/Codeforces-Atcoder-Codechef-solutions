from sys import stdin, stdout
n = int(input())
alist = list(map(int, stdin.readline().strip().split()))

totsum = sum(alist)
ssf = alist[0]
indices = set()
indices.add(1)

flag = 1
for i in range(1, n):
    if 2*alist[i] <= alist[0]:
        indices.add(i+1)
        ssf += alist[i]
    if ssf >  totsum/2:
        flag = 0
        break

if flag:
    print(0)
else:
    print(len(indices))
    print(*sorted(list(indices)))