import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs(r, c):
    if dp[r][c] == -1:                                      # 방문 안한 지점(-1)만 확인
        dp[r][c] = 0                                        # 현 지점 dp값 초기화
        for move in moves:
            new_r, new_c = r + move[0], c + move[1]
            if 0 <= new_r < n and 0 <= new_c < n and mat[r][c] < mat[new_r][new_c]:
                dp[r][c] = max(dp[r][c], dfs(new_r, new_c)) # 현재 값 vs 이동가능한 다음 값

    return dp[r][c] + 1                                     # 이전 값 +1 해준 값을 반환해야, 위의 max계산이 맞음(하나 이동했다는 뜻)


n = int(input())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]                             # -1로 시작하면, visited같이 쓸 수 있음
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(n):
    for j in range(n):
        dfs(i, j)
print(max(map(max, dp))+1)                                  # 맨 마지막 지점 +1이 안되어 있음
