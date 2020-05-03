n, m = map(int, input().split())
hlist = list(map(int, input().split())) #height list
glist = [1]*n #good list; initially all cities are good

for _ in range(m):
    a, b = map(int, input().split())
    ah = hlist[a-1]
    bh = hlist[b-1]

    if ah>bh:
        glist[b-1] = 0
    elif ah < bh:
        glist[a-1] = 0
    else: #both heights are same
        glist[a-1] = 0
        glist[b-1] = 0

print(sum(glist))