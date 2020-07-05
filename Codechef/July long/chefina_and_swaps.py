import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        alist = list(map(int, input().split()))
        blist = list(map(int, input().split()))

        freq_diff = dd(int)

        for i in alist:
            freq_diff[i] += 1
        for i in blist:
            freq_diff[i] -= 1
        
        exitflag = False

        for k in freq_diff.keys():
            if freq_diff[k]%2:
                exitflag = True
                break
        
        if exitflag:
            print(-1)
            continue
        
        pos, neg = [], []
        for pair in freq_diff.items():
            if pair[1] > 0:
                pos.append(pair)
            elif pair[1] < 0:
                neg.append((pair[0], -pair[1]))

        pos.sort(key=lambda x: x[0])
        neg.sort(key=lambda x: x[0])

        # print(pos, neg)

        pos_start = 0
        cost = 0
        while neg:
            mxneg, freqneg = neg[-1]
            mipos, freqpos = pos[pos_start]

            if freqneg == freqpos:
                numswaps = freqneg//2
                pos_start += 1
                neg.pop()
                cost += min(mxneg, mipos)*numswaps
            
            elif freqneg < freqpos:
                numswaps = (freqpos - freqneg)//2
                pos[pos_start] = (mipos, freqpos - numswaps)
                neg.pop()
                cost += min(mxneg, mipos)*numswaps
            
            else: # freqneg > freqpos
                numswaps = (freqneg - freqpos)//2
                pos_start += 1
                cost += min(mxneg, mipos)*numswaps
                neg[-1] = (mxneg, freqneg - numswaps)
        
        print(cost)

### Read the question completely wrong. I thought I had to make the sequences A and B identical and non-decreasing. And minimizing the cost.
def wrongInterpretation():
    t = int(input())
    for _ in range(t):
        n = int(input())
        alist = list(map(int, input().split()))
        blist = list(map(int, input().split()))

        correct = sorted(alist)

        ainds = dict()
        binds = dict()

        for i, num in enumerate(alist):
            if num not in ainds: 
                ainds[num] = [i]
            else:
                ainds[num].append(i)

        for i, num in enumerate(blist):
            if num not in binds: 
                binds[num] = [i]
            else:
                binds[num].append(i)

        exitflag = False
        for k in ainds.keys():
            if k not in blist or len(ainds[k])!=len(binds[k]):
                exitflag = True
        
        if exitflag:
            print(-1)
            continue
        
        # A solution definitely exists if it reaches here.
        i = 0
        cost = 0
        while i < n:
            af, bf, co = alist[i], blist[i], correct[i]

            if af == co and bf == co:
                pass
            elif af == co and bf!=co:
                last = ainds[af][-1]
                if last > i:
                    alist[last], blist[i] = blist[i], alist[last]
                    cost += co

                    ainds[af].pop()
                    ainds[bf].append(last)
                    binds[bf].pop()

                elif last == i:
                    cost += 2*co
                    lastb = binds[af][-1]
                    blist[i], blist[lastb] = blist[lastb], blist[i]

                    binds[af].pop()
                    binds[bf].append(lastb)
            elif bf == co and af!=co:
                last = binds[bf][-1]
                if last > i:
                    blist[last], alist[i] = alist[i], blist[last]
                    cost += co

                    binds[bf].pop()
                    binds[af].append(last)
                    ainds[af].pop()

                elif last == i:
                    cost += 2*co
                    lasta = ainds[bf][-1]
                    alist[i], alist[lasta] = alist[lasta], alist[i]

                    ainds[bf].pop()
                    ainds[af].append(lasta)
            else:
                cost += 2*co
                lastb = binds[co][-1]
                lasta = ainds[co][-1]
                blist[i], alist[lasta] = alist[lasta], blist[i]

                ainds[co].pop()
                ainds[bf].append(lasta)


                alist[i], blist[lastb] = blist[lastb], alist[i]

                binds[co].pop()
                binds[af].append(lastb)
            i += 1
        print(cost)                

        




































# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion
 
if __name__ == "__main__":
    main()