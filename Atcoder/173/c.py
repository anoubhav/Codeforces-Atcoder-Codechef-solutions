import os
import sys
from io import BytesIO, IOBase

def in_contest_solution():
    from itertools import chain, combinations
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    def main():
        h, w, k = map(int, input().split())
        mat = []
        rowcount = dict()
        colcount = dict()
        totcount = 0
        for r in range(h):
            row = input()
            rowcount[r] = row.count('#')
            totcount += rowcount[r]
            mat.append(list(row))
        
        transpose = list(map(list, zip(*mat)))
        for c in range(w):
            col = ''.join(transpose[c])
            colcount[str(c)] = col.count('#')
        
        diff = totcount - k

        if diff<0:
            print(0)
        else:
            # diff > 0. Remove diff blacks.
            ans = 0
            allitems = list(rowcount.items()) + list(colcount.items())
            for subset in powerset(allitems):
                rows = []
                cols = []
                totrem = 0
                for item in subset:
                    if isinstance(item[0], int):
                        rows.append(item)
                    else:
                        cols.append(item)
                    totrem += item[1]

                
                for r in rows:
                    for c in cols:
                        elem = mat[r[0]][int(c[0])]
                        totrem -= 1 if elem == '#' else 0

                if totrem == diff:
                    ans += 1

            print(ans)
        
    main()

def editorial():
    h, w, k = map(int, input().split())
    mat = []
    for r in range(h):
        mat.append(list(input()))
    
    ans = 0
    for rowmask in range(0, 1<<h):
        for colmask in range(0, 1<<w):
            count = 0
            for r in range(h):
                for c in range(w):
                    if (rowmask>>r)&1 == 0 and (colmask>>c)&1 == 0 and mat[r][c] == '#': count += 1
            if count == k: ans += 1
    print(ans)

# in_contest_solution()
editorial()


































