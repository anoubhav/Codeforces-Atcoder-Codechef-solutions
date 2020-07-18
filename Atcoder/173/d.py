import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction
def editorial():
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i//2]
        # print(ans)
    print(ans)
    
def main():
    import heapq
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    if n<=3:
        print(sum(nums[:n-1]))
        exit()
    

    hp = list()
    ans = 0
    # Push the first three intervals
    heapq.heappush(hp, (-nums[1], nums[0]))
    heapq.heappush(hp, (-nums[2], nums[0]))
    heapq.heappush(hp, (-nums[2], nums[1]))
    ans = sum(nums[:2])

    i = 3
    while i < n:
        comfort, big = heapq.heappop(hp)
        ans += -comfort

        small = -comfort

        curr = nums[i] # what enters the circle

        #push the smaller interval
        heapq.heappush(hp, (-curr, small))
        heapq.heappush(hp, (-curr, big))
        i += 1
    print(ans)






































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