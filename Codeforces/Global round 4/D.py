# 1hr 30 mins on D. 
# 
# I wasted 1 hr on doing something completely wrong, I did not satisfy a given condition which was clearly given in the problem. Next, you have an idea, think if it satisfies the constraints before spending a lot of time on it.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

def closest_prime(n):
    import bisect
    p = primes[bisect.bisect_left(primes, n)]
    return p

def alternate_soln():
    n = int(input())
    p = closest_prime(n)

    print(p)
    # degree 2
    for i in range(n):
        print(i+1, (i+1)%n + 1)
    
    # degree 3
    for i in range(p - n):
        print(i+1, i+1+n//2)

alternate_soln()

# Accepted
def my_soln():
    import math


    def create_list(start, p):
        for i in range(start, start + p - 1):
            edgelist.append((i, i+1))

        edgelist.append((i+1, start))
        end = i+1
        return end # included



    n = int(input())
    edgelist = []

    closest_p = closest_prime(n)
    diff = closest_p - n

    create_list(1, n)

    if diff == 0:
        print(closest_p)
        for edge in edgelist:
            print(*edge)

    else:
        start = 1
        flag = 0
        s = set()
        while diff!=0:
            if start not in s:
                edgelist.append((start, (start + 2)))
                s.add(start)
                s.add(start + 2)
                diff -= 1

            start += 1
            if start == n-1:
                flag = 1
                break

        if flag and diff!=0:
            print(-1)
        else:
            print(closest_p)
            for edge in edgelist:
                print(*edge)
