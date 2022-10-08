import sys
sys.stdin = open('B.txt')


def dfs():
    return


T = int(input())
for _ in range(T):
    n = int(input())
    R = list(map(int, input().split()))
    S = [0] * n
    for i in range(n-1, -1, -1):
        for j in range(R[i]+1, n, 1):
            if j not in S[i:]:
                S[i] = j

    print(S)
