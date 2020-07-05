from sys import stdout, stdin
n = int(stdin.readline().strip())

def binary(lo, hi):
    mid = lo + (hi-lo)//2
    return mid

lo, hi = 1, n
loe, hie = 1, n
while True:
    mido = binary(lo, hi)
    mide = binary(loe, hie)

    print(mido)
    stdout.flush()
    to = stdin.readline().strip()
    if to == 'E': 
        exit()
    elif to == 'G':
        lo = mido + 1
    else:
        hi = mido - 1

    print(mide)
    stdout.flush()
    te = stdin.readline().strip()
    if te == 'E': 
        exit()
    elif te == 'G':
        loe = mide + 1
    else:
        hie = mide - 1


