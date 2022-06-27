import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs(r, c):
    if (r, c) == (M-1, N-1):                        # 종료 조건
        return 1
    if visited[r][c]:                               # 방문한 지점이라면,
        return dp[r][c]                             # dp값을 반환

    visited[r][c] = 1                               # 방문 체크
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < M and 0 <= new_c < N and mat[r][c] > mat[new_r][new_c]:
            dp[r][c] += dfs(new_r, new_c)           # 현 지점의 dp에 다음 지점 dp값 더해주기
    return dp[r][c]


M, N = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
dp = [[0]*N for _ in range(M)]                      # 현 지점에서 도착지까지 갈 수 있는 경우의 수 저장
visited = [[0]*N for _ in range(M)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
dfs(0, 0)
print(dp[0][0])
