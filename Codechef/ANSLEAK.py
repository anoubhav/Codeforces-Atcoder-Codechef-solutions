from collections import Counter
def get_most_frequent(solns):
    return Counter(solns).most_common()[0][0]
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        ans = []
        n, m, k = list(map(int, input().split()))
        for _ in range(n):
            solns = list(map(int, input().split()))
            ans.append(get_most_frequent(solns))
        print(' '.join([str(i) for i in ans]))
