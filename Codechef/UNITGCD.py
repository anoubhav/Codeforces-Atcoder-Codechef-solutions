import math

def coprime(a,b):
    if a==1 or b==1: return 1
    if a%b==0 or b%a==0: return 0
    if a%2==0 and b%2==0: return 0

    for num in range(3, math.floor(math.sqrt(min(a,b))), 2):
        if a%num == 0 and b%num == 0:
            return 0
    
    return 1

def find_largest_coprime_set(d):
    # create dictionary of coprimes
    for i in d.keys():
        for j in d.keys():
            if i!=j:
                flag = 1
                for k in d[i]:
                    if not coprime(j, k):
                        flag = 0
                        break
                if flag: d[i].append(j)
    
    # remove largest set
    maxkey = max(enumerate(d.items()), key = lambda x: len(x[1][1]))[1][0]
    ans = [len(d[maxkey])]
    for i in d[maxkey]:
        del d[i]
        ans.append(i)
    string = ' '.join([str(i) for i in ans])

    return list(d.keys()), string
    
def get_pages(n):
    d = dict(zip(range(1, n+1),[[i] for i in range(1, n+1)]))
    num_day = 0
    ans = []
    while d!={}:
        d, string = find_largest_coprime_set(d)
        d = dict(zip(d, [[i] for i in d]))
        ans.append(string)
        num_day+=1
    print(num_day)
    print('\n'.join(ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        get_pages(n)
