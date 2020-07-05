from math import ceil
from collections import defaultdict as dd
n = 8
k = 3
dependencies = [[1,6],[2,7],[8,7],[2,5],[3,4]]

g = dd(list)
degrees = [0]*(1+n)

for i, j in dependencies:
    g[i].append(j)
    degrees[j] += 1

sems = 0
separate = dd(set)
while sum(degrees)!=-n:
    toremove = []
    for i, deg in enumerate(degrees):
        if i == 0: continue
        if deg == 0: toremove.append(i)
    

    possible_to_remove = toremove
    for node in toremove:
        # degrees[node] = -1
        for nbr in g[node]:
            degrees[nbr] -= 1

            separate[node].add(nbr)
            separate[nbr].add(node)
            if degrees[nbr] == 0:
                possible_to_remove.append(nbr)
    
    while len(possible_to_remove)>k:
        final = set()
        flag = 0
        for node in possible_to_remove:
            # lets see if we can remove this node this time
            canadd = True
            for sepnode in separate[node]:
                if sepnode in final:
                    canadd = False
                    break
            if canadd:
                final.add(node)
                degrees[node] = -1
                if len(final) == k:
                    for node in final:
                        possible_to_remove.remove(node)
                    sems += 1
                    flag = 1
                    break
                    
        print(possible_to_remove)

    print(final)
    # print(toremove)
    # print(final)
    sems += ceil(len(final)/k)
print(sems)


        



        