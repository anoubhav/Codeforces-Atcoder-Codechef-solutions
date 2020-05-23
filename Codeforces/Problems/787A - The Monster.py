# 787A
# 50 mins. Excessive, lacked in math theory.
# Good reference (not used while solving): https://math.stackexchange.com/questions/1656120/formula-to-find-the-first-intersection-of-two-arithmetic-progressions

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

from sys import stdin
a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())

const = b - d + c - a

# m*c + n*(-a) = const = b - d + c - a
# Linear Diophantine equation gives the below if condition.
# for solution to exist
if const%gcd(a, c) == 0: 
    for m in range(1, 10**7):
        # if n is positive
        if m*c>=const:
            # if n is an integer
            if (m*c - const)/a == (m*c - const)//a:
                # b + (n-1)*a
                print(b + ((m*c - const)//a - 1)*a)
                break
else:
    print(-1)


def my_soln_in_comp():
    # I made it highly explicit with the edge cases. All those if statements in the beginning were not needed for the Linear diophantine solution at the end.
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)

    from sys import stdin
    a, b = map(int, stdin.readline().split())
    c, d = map(int, stdin.readline().split())

    # gen term
    # b + (n-1)*a = d + (m-1)*c
    # b - d + c - a = mc - na

    if a == 0:
        if c!=0:
            if b<d:
                print(-1)
            elif (b-d)%c==0:
                print()

            else:
                print(-1)
        else:
            if b!=d:
                print(-1)
            else:
                print(b)

    if (b%2==1 and a%2==0 and d%2 == 0 and c%2 == 0) or (d%2==1 and c%2==0 and b%2 == 0 and a%2 == 0):
        print(-1)

    else:
        const = b - d + c - a

        # m*c + n*(-a) = const
        # Linear Diophantine equation gives the below if condition.
        if const%gcd(a, c) == 0:
            for m in range(1, 10**7):
                if m*c>=const:
                    if (m*c - const)/a == (m*c - const)//a:
                        print(b + ((m*c - const)//a - 1)*a)
                        break
        
        else:
            print(-1)





    