## In contest solution
# n = int(input())
# ans = [0, 0, 0, 0]
# for _ in range(n):
#     s = input()
#     if s == 'AC':
#         ans[0] += 1
#     elif s ==  'WA':
#         ans[1] += 1
#     elif s == 'TLE':
#         ans[2] += 1
#     else:
#         ans[3] += 1

# lst = ['AC', 'WA', 'TLE', 'RE']
# for i in range(4):
#     print(lst[i], 'x', ans[i])


# editorial
N = int(input())
s = [input() for i in range(N)] # Took the input at once into a list.
for v in ['AC', 'WA', 'TLE', 'RE']:
    print('{0} x {1}'.format(v, s.count(v))) # used count