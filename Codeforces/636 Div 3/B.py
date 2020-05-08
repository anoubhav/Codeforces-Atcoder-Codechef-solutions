t = int(input())
import math
for _ in range(t):
    n = int(input())
    half =n//2
    if half%2 == 1:
        print('NO')
        continue

    evens = [2*i for i in range(1, half + 1)]
    odds = [2*i + 1 for i in range(0, half - 1)]
    odds = odds + [sum(evens) - sum(odds)]

    print('YES')
    print(' '.join([str(i) for i in evens] + [str(i) for i in odds]))