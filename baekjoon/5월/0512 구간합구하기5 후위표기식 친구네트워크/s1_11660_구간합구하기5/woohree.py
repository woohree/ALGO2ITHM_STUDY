import sys
sys.stdin = open('L.txt')


def get_dp(mat, operates):
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):                      # (0, 0)부터 각 좌표까지의 누적합 dp에 저장
        for j in range(N):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + mat[i][j]

    for operate in operates:                # 해당 구간의 구간 합 출력
        r1, c1, r2, c2 = operate
        print(dp[r2][c2] - (dp[r1-1][c2] + dp[r2][c1-1]) + dp[r1-1][c1-1])


N, M = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
operates = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
get_dp(mat, operates)
