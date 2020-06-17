# https://discuss.codechef.com/t/ttuple-editorial/67892

# v1 - v0 * x = u1 - u0 * x
# (u0 - v0) * x = u1 - v1
def eq_solve(v0, v1, u0, u1):
    den = u0 - v0
    num = u1 - v1
    if den != 0:
        return num // den
    return 1
 
def solve(p, q, r, a, b, c, rs):
    if p == a and q == b and r == c:
        return rs
    if rs >= 2:
        return 3
    res = 3
    adds = [a - p, b - q, c - r]
    muls = []
    if p != 0:
        muls.append(a / p)
    if q != 0:
        muls.append(b / q)
    if r != 0:
        muls.append(c / r)
    muls.append(eq_solve(p, a, q, b))
    muls.append(eq_solve(p, a, r, c))
    muls.append(eq_solve(q, b, r, c))
    msks = 2 ** 3
    for msk in range(msks):
        for add in adds:
            np = p
            nq = q
            nr = r
            if (msk & 1) > 0:
                np += add
            if (msk & 2) > 0:
                nq += add
            if (msk & 4) > 0:
                nr += add
            res = min(res, solve(np, nq, nr, a, b, c, rs + 1))
        for mul in muls:
            np = p
            nq = q
            nr = r
            if (msk & 1) > 0:
                np *= mul
            if (msk & 2) > 0:
                nq *= mul
            if (msk & 4) > 0:
                nr *= mul
            res = min(res, solve(np, nq, nr, a, b, c, rs + 1))
    return res
        
 
 
t = int(input())
 
while t > 0:
    p, q, r = map(int, input().split())
    a, b, c = map(int, input().split())
    print(solve(p, q, r, a, b, c, 0))
    t -= 1 