from sys import stdin, stdout
from collections import defaultdict
t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    s = stdin.readline().strip()

    start = (0, 0)
    ans, minlen = 10**9, 10**9
    d = defaultdict(list)
    d[start] = [0]

    for i, mov in enumerate(s):
        if mov == 'L':
            new = (start[0] - 1, start[1])
        elif mov == 'R':
            new = (start[0] + 1, start[1])
        elif mov == 'U':
            new = (start[0], start[1] + 1)
        else:
            new = (start[0], start[1] - 1)
        
        if len(d[new]):
            prev = d[new][-1]

            if i - prev + 1 < minlen:
                minlen = i - prev + 1
                ans = (prev+1, i+1)
            else:
                pass

        d[new].append(i+1)
        start = new

    answers.append((ans if ans!=10**9 else -1))
    # print(d)

for ans in answers:
    if ans == -1:
        print(ans)
    else:
        print(*ans)

