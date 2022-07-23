import sys
sys.stdin = open('W.txt')


T = int(input())
for _ in range(T):
    n = int(input())
    R = list(map(int, input().split()))
    visited = [i for i in range(1, n+1)]
    S = []
    for i in range(n-1, -1, -1):
        if len(visited) <= R[i]:
            print('IMPOSSIBLE')
            break
        S.append(visited.pop(R[i]))
    else:
        for s in S[::-1]:
            print(s, end=' ')
        print()