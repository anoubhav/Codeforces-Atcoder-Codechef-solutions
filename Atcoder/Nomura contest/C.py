from sys import stdin, stdout
n = int(stdin.readline())
nmleaves = list(map(int, stdin.readline().strip().split()))

if nmleaves[0]:
   if n == 0 and nmleaves[0] == 1:
      print(1)
   else:
      print(-1)
   exit()

# pref[i]: sum(nmleaves[i:]), i.e., the number of leaves at or below level i.
pref = [0]*(n+1)
totsum = sum(nmleaves)
pref[0] = totsum
t = 0
for i in range(1, n+1):
    t += nmleaves[i-1]
    pref[i]  = totsum - t

prev_nl = 1
ans = 1
for lev in range(1, n+1):
    nodes = min(prev_nl*2, pref[lev])
    ans += nodes
    prev_nl = nodes - nmleaves[lev]
    if prev_nl < 0:
        print(-1)
        exit()
print(ans)


# We maximize the number of nodes we have at each level. First, note that there can only be as many nodes at any level as there are leaves at or below that level in the tree. Second, note that there can only be twice as many nodes at any level as there were non-leaf nodes at the previous level. At each level, we add the minimum of these two values to the answer. We print -1 if any level has fewer nodes than it must have leaves.











# worked on 70% of the test cases. Got WA for the remaning 30 %.
def failed_attempt(): 
    # pref[i]: sum of all elements in nmleaves after i, i.e. sum(nmleaves[i+1:])
    full = sum(nmleaves)
    tot = 0
    pref = [0]*(n+1)
    for i, l in enumerate(nmleaves):
        tot += l
        pref[i] = full - tot

    if n==0:
        print(0)

    else:
        if nmleaves[0]!=0:
            print(-1)
            exit()
        
        ## it exists
        ans = 0
        for level, leaves in enumerate(nmleaves):
            if leaves > 2**(level):
                print(-1)
                exit()

            if level == 0:
                ans += 1
                validnom = 1
            else:
                maxup = 2*validnom
                maxnom = maxup - leaves

                if level+1<len(nmleaves):
                    validnom = min(maxnom, pref[level], 2**level - leaves)
                    ans += (leaves + validnom)
                else:
                    ans += leaves
        print(ans)



