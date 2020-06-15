from sys import stdin, stdout

s = input()
n = len(s)
P = 2019

# suffix_rems is a list of remainders obtained by dividing the suffix starting at i with P. suffix[i] = s[i:]%P.

suffix_rems = [-1]*n
suffix_rems[-1] = int(s[-1])%P

# Stores the frequency of remainders obtained. We just want number of (i, j) pairs.
rems_d = dict()
rems_d[0] = 1
rems_d[int(s[-1])] = 1

# Those remainders which occur more than once. To pick (i, j) pairs from N, we need N > 1.
special_keys = set()

for i in range(n-1)[::-1]:
    rem = (pow(10, n-i-1, P) * int(s[i]) + suffix_rems[i + 1])%P

    if rem in rems_d:
        rems_d[rem] += 1
        special_keys.add(rem)
    else:
        rems_d[rem] = 1

    suffix_rems[i] = rem

ans = 0
for key in special_keys:
    t = rems_d[key]
    # pick any two of those same remainder indices.
    ans += (t*(t-1))//2

print(ans)