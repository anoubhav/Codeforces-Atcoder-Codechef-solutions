n, a, b, c = list(map(int, input().split()))
slist = []
d = {'A': a, 'B':b, 'C':c}
soln = []
prev = None

for i in range(n):
    s = input()

    # corner case
    if prev:
        if prev[0] in s:
            d[prev[0]] += 1
            d[prev[1]] -= 1
            soln.append(prev[0])
        else:
            d[prev[1]] += 1
            d[prev[0]] -= 1
            soln.append(prev[1])
        prev = None
    
    # corner case
    if d[s[0]] ==1 and d[s[1]] == 1:
        prev = s

    # greedy
    elif d[s[0]] >= d[s[1]]:
        d[s[0]] -= 1
        d[s[1]] += 1
        soln.append(s[1])

    elif d[s[0]] < d[s[1]]:
        d[s[1]] -= 1
        d[s[0]] += 1
        soln.append(s[0])

    if d['A'] < 0 or d['B'] < 0 or d['C'] < 0:
        print('No')
        exit()
        break

print('Yes')
print('\n'.join(soln))



