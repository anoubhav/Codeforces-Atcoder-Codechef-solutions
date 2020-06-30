## Greedy attempt to E2. Completely wrong. The problem is much harder. 2400 rating.

from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n, m, k = map(int, input().split())
alike, blike = 0, 0
zero_one, one_zero, one_one, zero_zero = [], [], [], []
for i in range(n):
    t, a, b = map(int, input().split())
    alike += a
    blike += b

    if a == 0 and b == 1:
        zero_one.append((t, i))
    elif a == 1 and b == 0:
        one_zero.append((t, i))
    elif a== 1 and b== 1:
        one_one.append((t, i))
    else:
        zero_zero.append((t, i))


if alike < k or blike < k:
    print(-1)
    exit()

zero_one.sort(key = lambda x: x[0])
one_one.sort(key = lambda x: x[0])
one_zero.sort(key = lambda x: x[0])
zero_zero.sort(key = lambda x: x[0])

alike, blike = 0, 0
zo, oo, oz, zz = 0, 0, 0, 0
lzo, loo, loz, lzz = len(zero_one), len(one_one), len(one_zero), len(zero_zero)
tottime = 0
books = []

while alike<k or blike<k:
    if oo >= loo and zo >= lzo and oz>=loz:
        break

    lbo = len(books)
    if lbo == m:
        if alike < k or blike < k:
            print(-1)
            exit()
        else:
            break
        
    if alike <k and blike <k:
        if oo>= loo and zo>=lzo and oz>=loz:
            print(-1)
            exit()
        
        elif (zo >= lzo or oz >= loz):
            if lbo + 1 <= m:
                tottime += one_one[oo][0]
                books.append(one_one[oo][1])
                oo += 1
            else:
                print(-1)
                exit()   


        elif oo >= loo:
            if lbo + 2 <= m:
                tottime += zero_one[zo][0] + one_zero[oz][0]
                books.append(zero_one[zo][1])
                books.append(one_zero[oz][1])
                zo += 1
                oz += 1
            else:
                print(-1)
                exit()   

        elif lbo + 2 <=m and zero_one[zo][0] + one_zero[oz][0] <= one_one[oo][0]:
            tottime += zero_one[zo][0] + one_zero[oz][0]
            books.append(zero_one[zo][1])
            books.append(one_zero[oz][1])
            zo += 1
            oz += 1
            
        else:
            if lbo + 1 <= m:
                tottime += one_one[oo][0]
                books.append(one_one[oo][1])
                oo += 1
            else:
                print(-1)
                exit()   

        alike += 1
        blike += 1

    elif alike == k and blike < k:
        if oo>=loo and zo>=lzo:
            print(-1)
            exit()
        elif lbo + 1 > m:
            print(-1)
            exit()

        elif oo >= loo:
            tottime += zero_one[zo][0]
            books.append(zero_one[zo][1])
            zo += 1
        elif zo >= lzo:
            tottime += one_one[oo][0]
            books.append(one_one[oo][1])
            oo += 1

        elif zero_one[zo][0] < one_one[oo][0]:
            tottime += zero_one[zo][0]
            books.append(zero_one[zo][1])
            zo += 1      
        else:
            tottime += one_one[oo][0]
            books.append(one_one[oo][1])
            oo += 1
        blike += 1
    
    elif alike <k and blike == k:
        if oo>=loo and oz>=loz:
            print(-1)
            exit()
        elif lbo + 1 > m:
            print(-1)
            exit()

        elif oo>=loo:
            tottime += one_zero[oz][0]
            books.append(one_zero[oz][1])
            oz += 1

        elif oz>= loz:
            tottime += one_one[oo][0]
            books.append(one_one[oo][1])
            oo += 1
        elif one_zero[oz][0] < one_one[oo][0]:
            tottime += one_zero[oz][0]
            books.append(one_zero[oz][1])
            oz += 1
        else:
            tottime += one_one[oo][0]
            books.append(one_one[oo][1])
            oo += 1

# if leftover books after k condition is satisfied
if len(books) < m:
    rem = m - len(books)

    remaining_books = zero_one[zo:] + one_zero[oz:] + zero_zero[zz:] + one_one[oo:]

    remaining_books.sort(key = lambda x: x[0])

    if rem > len(remaining_books):
        print(-1)
        exit()

    for book in remaining_books[:rem]:
        tottime += book[0]
        books.append(book[1])

print(tottime)
books = [i + 1 for i in books]
print(*books)



        




