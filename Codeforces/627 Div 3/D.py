# 1 hr 40 mins. 13 submission errors. TLE/MLE/WA. But finally got it. Bad, could be better. But, I applied new concepts. (very slowly though)
from sys import stdin
from collections import defaultdict
import bisect

def editorial():

    # Input
    n = int(stdin.readline())
    alist = list(map(int, stdin.readline().strip().split()))
    blist = list(map(int, stdin.readline().strip().split()))

    clist = []
    for i in range(n):
        clist.append(alist[i] - blist[i])

    # negative to positive a[i] - b[i]. For each negative a[i]-b[i] : k1, we need to find the smallest possile positive a[j] - b[j]: k2 such that k1 + k2 > 0
    clist.sort()

    neg_pos_pairs = 0
    for i, num in enumerate(clist):
        if num <=0:
            ind = bisect.bisect_left(clist, -num + 1)
            neg_pos_pairs += (n - ind)
        else:
            break

    # i stores the first positive a[i] - b[i]. The number of positive a[i] - b[i] => (n - i). total number of positive pairs = (n-i)C2
    poscount = n - i

    print(neg_pos_pairs +  ((poscount)*(poscount-1))//2)


def my_soln():
    # Input
    n = int(stdin.readline())
    alist = list(map(int, stdin.readline().strip().split()))
    blist = list(map(int, stdin.readline().strip().split()))

    # Stores the number of pairs with value a[i] - b[i]
    d = defaultdict(int)
    # Store the positive a[i] - b[i]
    dposkeys = set()
    # Store the negative a[i] - b[i]
    dnegkeys = set()

    # Number of positive a[i] - b[i]
    poscount = 0
    for i in range(n):
        t = alist[i] - blist[i]
        d[t] += 1
        if t>0:
            poscount += 1
            dposkeys.add(t)
        else:
            dnegkeys.add(t)

    # To prevent MLE
    del alist, blist

    # Sort the positive keys in ascending order
    dposkeys = sorted(list(dposkeys))

    # prefix sums of: the number of (a[i] - b[i]) whose value is more than some positive value.
    pref = [0]
    t = 0
    for k in dposkeys:
        t += d[k]
        pref.append(t)

    pref[0] = t   # [total, total - no. of a[i] - b[i] > K, where K is a positive number. The larger the value of K, the fewer such a[i] - b[i] exist.]
    for i in range(1, len(pref)):
        pref[i] = t - pref[i]

    # negative - positive pairs
    neg_pos_pairs = 0
    for k1 in dnegkeys:
        # find the minimum positive key required such that the positive key + negative key > 0 , i.e. a[i] - b[i] > 0 and a[j] - b[j] < 0 .But, a[i] + a[j] > b[i] + b[j]. That is pos + neg > 0 or pos > -neg. So pos can be more -neg + 1 ONWARDS. Because of 'ONWARDS' we use are prefix sums.
        ind = bisect.bisect_left(dposkeys, -k1 + 1)

        # the number of a[j]-b[j] < 0 is d[k1]. the number of  a[i]-b[i] > 0 such that the sum of k1 + k2>0 is in prefix sum.
        neg_pos_pairs += d[k1]*pref[ind]

    # positive - positive pairs, i.e. a[i] - b[i] > 0 and a[j] - b[j] > 0 ---> a[i] + a[j] > b[i] + b[j]. NC2 possibilities, where N is the # of positive pairs.
    pos_pos_pairs = ((poscount)*(poscount-1))//2

    print(neg_pos_pairs + pos_pos_pairs)


