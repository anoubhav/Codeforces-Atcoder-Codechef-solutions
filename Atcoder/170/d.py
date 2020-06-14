from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

# Question: Calculate number of elements in array which are not divisible by any other. Naive: O(N^2) time and O(1) space.

# I used the concept of Sieve of Eratosthenes (without knowing this you won't understand). Which gave a solution of O(N log N + Amx log Amx) time and space.

t = int(input())
nums = list(map(int, stdin.readline().split()))

# sort the numbers, re-read the question. Order does not matter.
nums.sort()

# we want to calculate seive upto the largest number in nums. Luckily thats only 10^6. 
n = nums[-1]

# is_prime is a boolean, it actually means is_not_divisble by all others (in this context). Initially (like in seive) set all as 'primes'.
is_prime = [1]*(n+1)

# if any elements are repeated in the array, they are not 'prime'.
d = dict()
for elem in nums:
    if elem not in d:
        d[elem] = 0
    else:
        is_prime[elem] = 0

# in the sorted array, go from the lowest element to the highest. Mark the multiples of the lowest
# element upto the highest as 'not prime', i.e, if they exist in our list, they are divisible by something else.
for num in nums:
    for mult in range(2*num, n+1, num):
        is_prime[mult] = 0

# in our list, those which are still 'prime' return their count.
print(sum([is_prime[i] for i in nums]))