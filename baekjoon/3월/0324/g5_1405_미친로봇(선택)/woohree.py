import sys
sys.stdin = open('L.txt')


def dfs(r, c, cnt, prob):               # 이동하는 방향에 해당하는 확률값을 곱해가며 진행
    global ans
    if cnt == N:                        # 로봇이 N번 이동했으면,
        ans += prob                     # 확률 더해주고 종료!
        return
    mat[r][c] = 1                       # 방문 도장
    for i in range(4):
        new_r, new_c = r + moves[i][0], c + moves[i][1]
        if 0 <= new_r < 2*N+1 and 0 <= new_c < 2*N+1 and not mat[new_r][new_c]:  # 다음 지점을 재방문하면 단순해짐
            dfs(new_r, new_c, cnt+1, prob*probs[i])                              # 한번만 방문하면 단순하지 않은 경우
            mat[new_r][new_c] = 0                                                # 방문 도장 초기화


N, *probs = map(int, sys.stdin.readline().rstrip().split())
for idx in range(4):
    probs[idx] /= 100
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 0동 1서 2남 3북
mat = [[0]*(2*N+1) for _ in range(2*N+1)]
cnt = ans = 0
prob = 1
dfs(N, N, cnt, prob)
print(ans)
