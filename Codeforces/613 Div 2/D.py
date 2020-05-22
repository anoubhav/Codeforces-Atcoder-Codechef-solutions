from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(5*10**5)
n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))

def div_and_conquer(pos, elems):
    if pos==0: return 0
    zero, one = set(), set()
    mask = 1<<(pos-1)
    for num in elems:
        if (num&mask)>>(pos-1):
            one.add(num)
        else:
            zero.add(num)
    
    if not zero:
        return div_and_conquer(pos - 1, one)
    
    if not one:
        return div_and_conquer(pos - 1, zero)
    
    return 1<<(pos-1) + min(div_and_conquer(pos-1, zero), div_and_conquer(pos-1, one))

print(div_and_conquer(30, a))


