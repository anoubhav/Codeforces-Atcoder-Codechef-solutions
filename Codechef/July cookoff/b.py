import os
import sys
from io import BytesIO, IOBase
from math import sqrt, log, log2
# Codechef editorial: https://discuss.codechef.com/t/orthodox-editorial/72331

def trick_brute(nums, n):
    # https://www.youtube.com/watch?v=4roaMb_v-qQ
    if n>60:
        return 'NO'
    seen = set()

    # O(N^2) brute when N < 60
    ans = 'YES'
    for i in range(n):
        orprod = 0
        for j in range(i, n):
            orprod |= nums[j]
            if orprod in seen:
                ans = 'NO'
                break
            else: seen.add(orprod)
    return ans

def nlogn_sort(nums, n):
    # https://www.youtube.com/watch?v=iyl_g30vCzE
    nums.sort(reverse = True)
    seen = set()

    orprod = 0
    ans = 'YES'
    for i in nums:
        orprod |= i
        if orprod in seen:
            ans = 'NO'
            break
        else:
            seen.add(orprod)
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        ans1 = trick_brute(nums, n)
        ans2 = nlogn_sort(nums, n)
        assert ans1 == ans2
        print(ans1)



        
        




































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