# Find any string s of length m such that each of the given n strings differs from s in at most one position. 

# Here, brute force works. Why? The constraints are n<=10 and m<=10. This means there are at most 10 strings each of same length m, where m<=10. The number of test cases is 100. So even if our solution is O(t* m^3), it will be well below TLE.

# Note that the desired string s may be equal to one of the given strings ai, or it may differ from all the given strings.

# Idea: Let s (answer) be the first string, compare s with the remaining (n-1) sequences. Keep track of the maximum difference obtained using s. Next, change the first character of s to something else and REPEAT. Once all possible characters in the first position have been checked, move to the next position of s. 

# Thus, we are using brute force over ALL POSSIBLE 1 character different strings from the first string. If any of these also have atmost 1 character difference with remaining n-1 strings, we have our answer.

# Time complexity: at each position in s (total m), try each possible character (26 in lower case) and compare (m comparisons) with each of the n strings. Repeat for t test cases. Overall: O(T * m * 26 * m * n) << TLE


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    strings = []

    for _ in range(n):
        strings.append(input())
    
    stop = 0
    # Over all positions in s (answer)
    for pos in range(m):

        # Over all characters in position
        for char in range(26):
            s = list(strings[0])
            s[pos] = chr(ord('a') + char)
            s = ''.join(s)

            maxdiff = 0

            # Over all strings
            for string in strings:
                diff = 0
                # compare
                for ind in range(m):
                    if s[ind]!=string[ind]:
                        diff+=1

                maxdiff = max(maxdiff, diff)

            if maxdiff == 1:
                stop = 1
                print(s)
                break
        
        if stop:
            break

    if not stop:
        print(-1)
    


