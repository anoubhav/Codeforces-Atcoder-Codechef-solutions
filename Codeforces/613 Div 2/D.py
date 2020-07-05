# https://codeforces.com/contest/1285/submission/68517560
from sys import stdin, stdout
from itertools import repeat
n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))
# a = map(int, stdin.readline().split(), repeat(10, n))
# a = list(set(a))
def div_and_conquer(pos, elems):
    if pos==0: return 0
    zero, one = set(), set()
    for num in elems:
        if num>>(pos-1) & 1:
            one.add(num)
        else:
            zero.add(num)
    
    if not zero:
        return div_and_conquer(pos - 1, one)
    
    if not one:
        return div_and_conquer(pos - 1, zero)
    
    return 2**((pos-1) + min(div_and_conquer(pos-1, zero), div_and_conquer(pos-1, one)))

print(div_and_conquer(30, a))


