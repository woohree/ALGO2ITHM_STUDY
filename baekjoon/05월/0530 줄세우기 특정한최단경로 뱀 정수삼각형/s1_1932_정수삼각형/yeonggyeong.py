import sys
sys.stdin = open('G.txt')

N = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 삼각형이랑 같은 모양으로 dp 배열 생성
dp = [[0] * len(triangle[i]) for i in range(N)]

dp[0][0] = triangle[0][0]

for row in range(1, N):
    # 각 행의 길이
    length = len(triangle[row])
    for col in range(length):
        # 가장 왼쪽일때
        if col == 0:
            dp[row][col] = dp[row-1][col] + triangle[row][col]
        # 가장 오른쪽일때
        elif col == length-1:
            dp[row][col] = dp[row-1][-1] + triangle[row][col]
        else:
            dp[row][col] = max(dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]

print(max(dp[-1]))