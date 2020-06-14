def incontest_using_binsearch():
    # 875ms
    # O(N^2 log N). During the contest I over complicated my solution even after figuring out the key observation that i-j != k-j condition allows to iterate over only i, j and fix k.
    n = int(input())
    s = input()

    # stored the indices of R, G, B
    rinds, ginds, binds = [], [], []
    for i in range(n):
        if s[i] == 'R': rinds.append(i)
        elif s[i] == 'G': ginds.append(i)
        else: binds.append(i)

    rlen, glen, blen = len(rinds), len(ginds), len(binds)

    # This is to check if there exists a k, such that: i-j!=k-j
    def binsearch_same(binds, blen, dist, i):
        lo, hi = 0, blen-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            d = binds[mid] - i
            if dist == d:
                return True
            elif d < dist:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    ans = 0
    for i in rinds:
        for j in ginds:
            # Given j > i. To ensure this, redefine i' < j'.
            dist = abs(i-j)
            i_ = min(i, j)
            j_ = max(i, j)

            # for each (i, j) all k are possible except those which don't satisfy condition 2.
            ans += blen

            ## To figure out if such a k exists in kinds, I did 3 binary searches for the 3 possiblies. I just had to check, if k exists in kinds. I could have easily just made kinds a set. And gotten O(1) lookup time.

            # i' < j' < k
            if binsearch_same(binds, blen, dist, j_):
                ans -= 1
            # i'< k < j' 
            if dist%2==0 and binsearch_same(binds, blen, dist//2, i_):
                ans -= 1
            # # k < i' < j'
            if binsearch_same(binds, blen, -dist, i_):
                ans -= 1
    print(ans)

def using_set():
    #164 ms
    # Time complexity: O(N^2)
    n = int(input())
    s = input()

    rinds, ginds, binds = [], [], set()

    for i in range(n):
        if s[i] == 'R': rinds.append(i)
        elif s[i] == 'G': ginds.append(i)
        else: binds.add(i)

    rlen, glen, blen = len(rinds), len(ginds), len(binds)

    ans = 0

    for i in rinds:
        for j in ginds:
            dist = abs(i-j)
            i_ = min(i, j)
            j_ = max(i, j)
            ans += blen
            # i' < j' < k
            if j_ + dist in binds: # O(1)
                ans -= 1
            # i'< k < j'
            if dist%2==0 and i_ + dist//2 in binds:
                ans -= 1
            # k < i' < j'
            if i_ - dist in binds:
                ans -= 1
    print(ans)

# much better
def solution1():
    # 120ms. Time complexity: O(N^2)
    # https://www.youtube.com/watch?v=aRdGRrsRo7I 
    n = int(input())
    s = input()
    r, g, b = 0, 0, 0
    for i in s:
        if i == 'R': r += 1
        elif i == 'G': g += 1
        else: b += 1
    
    total = r*g*b
    # all permutations of rgb are valid, to check if s[i], s[j], s[k] is a permutation of 'rgb' we could use counter. Or neat trick: ASCII value of the sum of s[i] + s[j] + s[k] is same.

    is_rgb = ord('R') + ord('G') + ord('B')

    for i in range(n):
        for j in range(i+1, n):
            # Condition 2 fails when: i - j = k - j --> k = 2*j - i
            k = 2*j - i
            if k < n:
                if ord(s[i]) + ord(s[j]) + ord(s[2*j-i]) == is_rgb:
                    total -= 1
    print(total)










