from collections import defaultdict
d = defaultdict(int)
n = int(input())
lst = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    lst.append((name, score))
    d[name] += score

maxval = max(d.values())
possible_names = set()
for k, v in d.items():
    if v == maxval:
        possible_names.add(k)

# got the max score
d = defaultdict(int)
for i in range(n):
    name, score = lst[i]
    score = int(score)
    d[name] += score

    if d[name]>=maxval and name in possible_names:
        print(name)
        exit()





