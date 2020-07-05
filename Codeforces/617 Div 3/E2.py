def bubbleSort(arr, n): 
    tags = list(range(1, n+1))
    dislikes = []
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                tags[j], tags[j+1] = tags[j+1], tags[j]
                dislikes.append([tags[j], tags[j+1]])

    return dislikes

n = int(input())
s = input()
if s == ''.join(sorted(s)):
    print(1)
    print('1'*n, sep=' ')
    exit()

dislikes = bubbleSort(list(s), n)

if len(dislikes) == 0:
    print('YES')
    print('0'*n)
    exit()
from collections import defaultdict

g = defaultdict(list)

nodes = set()
for i, j in dislikes:
    g[i].append(j)
    g[j].append(i)
    nodes.add(i)
    nodes.add(j)

# print(dislikes)
# print(nodes)
def dfs_twocolor_np(node, g):
    global ok, res
    for nbr in g[node]:
        if colors[nbr] == 0:
            colors[nbr] = -colors[node] 
            dfs_twocolor_np(nbr, g)

        else:
            if colors[nbr] == colors[node]:

                colors[nbr] = 2
                ok = False
        

colors = [0]*(n+1)

res = 2
for node in range(1, n+1):
    if colors[node] == 0:
        ok = True
        colors[node] = -1

        dfs_twocolor_np(node, g)
        # print(node, colors)

        if not ok:
            res = 3

            # check nbrs of color[nbr]
    else:
        continue

# print('YES')
print(res)
ans = []
for i in colors[1:]:
    if i == 1: ans.append(str(i+1))
    elif i == -1: ans.append(str(1))
    else:ans.append(str(3))

print(*ans, sep=' ')