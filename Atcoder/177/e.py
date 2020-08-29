
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sieve_optimized(limit):
    # Preprocessing step takes O(N log log N) time complexity.
    n = limit
    # Filimitd all primes upto n  (including n)
    sievebound = (n-1)//2
    sieve = [-1]*(sievebound + 1)
    # sieve[0] = True
    crosslimit = (int(sievebound**0.5) - 1)
    for i in range(1, crosslimit + 1):
        if sieve[i] == -1:
            for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
                sieve[j] = 2*i + 1
    return sieve

def factorization(n, sieve):
    # Factorisaton query takes O(log N) time after preprocessing.
    divs = [1]
    while n!=1:
        if n&1:
            div = sieve[(n-1)//2]
            if div == -1:
                divs.append(n)
                break
            else:
                n //= div
                divs.append(div)
        else:
            n >>= 1
            divs.append(2)

    return divs

maxnum = 10**6 + 1
sieve = sieve_optimized(maxnum)

n = int(input())
nums = list(map(int, input().split()))

seen = dict()
maxval = 0
for i in nums:
    factors = factorization(i, sieve)
    if len(factors) <= 1: continue
    for f in set(factors[1:]):
        if f in seen:
            seen[f] += 1
            maxval = max(maxval, seen[f])
        else:
            seen[f] = 1


if maxval == n:
    print('not coprime')

elif 1 < maxval < n:
    print('setwise coprime')

else:
    print('pairwise coprime')