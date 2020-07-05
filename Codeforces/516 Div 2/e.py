n = int(input())
# white and black respectively
positions = {'black': None, 'white': None}

print(0, 0, flush=True)
col = input()
positions[col] = 0
positions['black' if col != 'black' else 'white'] = 10**9

for _ in range(n-1):
    l, r = sorted(positions.values())
    if (r-l) > 1:
        mid = l + (r - l)//2
        print(mid, 0, flush=True)
    else:
        mid = l
        print(l, 2, flush= True)
        
    col = input()
    positions[col] = mid

# point = sum(positions.values())//2

# (mid, 0)
# print(point, 0, point, 1) # vertical line
lst = sorted(list(positions.values()))
if lst[0]!=lst[1]:
    print(lst[0] + 1, 0, lst[0] + 1, 1)
else:
    print(lst[0]+1, 0, lst[0], 1)

    




