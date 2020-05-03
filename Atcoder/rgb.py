from itertools import product

n = int(input())
s = input()
r, g, b = [], [], []

for i, char in enumerate(s):
    if char == 'R': r.append(i)
    elif char == 'G': g.append(i)
    else: b.append(i)

count = 0
# for config in product(r,g,b):
#     a, b, c = config
#     a, b, c = sorted((a, b, c))

#     if (b-a)!=(c-b): count += 1

# print(count)

for i in r:
    for j in g:
        for k in b:
            if i<j<k:
                if (j-i)!=(k-j): count += 1
            if j<i<k:
                if (i-j)!=(k-i): count += 1
            if k<i<j:
                if (i-k)!=(j-i): count += 1
            if i<k<j:
                if (k-i)!=(j-k): count += 1
            if j<k<i:
                if (k-j)!=(i-k): count += 1
            if k<j<i:
                if (j-k)!=(i-j): count += 1
            
print(count)
