import sys
sys.stdin = open('M.txt')


def panda(cr, cc):
    d = ((-1, 0), (0, 1), (1, 0), (0, -1))

    if dp[cr][cc]:      # 이미 방문한 값이 있는 경우
        return dp[cr][cc]

    dp[cr][cc] = 1      # 1부터 시작
    for dr, dc in d:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < n and bamboo[nr][nc] > bamboo[cr][cc]:
            dp[cr][cc] = max(dp[cr][cc], panda(nr, nc) + 1)     # 더 큰 값 저장

    return dp[cr][cc]


n = int(sys.stdin.readline())
bamboo = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, panda(i, j))
print(answer)
