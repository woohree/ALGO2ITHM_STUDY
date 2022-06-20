import sys
sys.stdin = open('L.txt')


def F_W():
    for k in range(1, N+1):
        D[k][k] = 0
        for s in range(1, N+1):
            for e in range(1, N+1):
                D[s][e] = min(D[s][k] + D[k][e], D[s][e])


N = int(input())
inf = float('inf')
D = [[inf]*(N+1) for _ in range(N+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    D[a][b] = 1                         # 친구관계는 양방향!
    D[b][a] = 1
F_W()                                   # 가중치 모두 1, 거치는 친구의 수 세기
ans = []
min_num = 51
for i in range(1, N+1):                 # 각 경로에서 가장 큰 수 = 점수
    max_num = max(D[i][1:])
    if max_num < min_num:               # 각 경로에서 가장 큰 수 중 가장 작은 수 = 회장 후보
        min_num = max_num
        ans = [i]
    elif max_num == min_num:
        ans.append(i)
print(min_num, len(ans))
print(*ans)