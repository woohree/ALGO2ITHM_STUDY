import sys
sys.stdin = open('L.txt')


def F_W():
    for k in range(n):
        D[k][k] = 0
        for s in range(n):
            for e in range(n):
                D[s][e] = min(D[s][k] + D[k][e], D[s][e])


n = int(input())
m = int(input())
inf = float('inf')
D = [[inf]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    D[a-1][b-1] = min(D[a-1][b-1], c)       # 경로가 하나 이상일 때 !! 짧은 걸로 하려고!! min을 쓴 거 였구나!!!
F_W()
for i in range(n):
    for j in range(n):
        if D[i][j] == inf:
            D[i][j] = 0
    print(' '.join(map(str, D[i])))