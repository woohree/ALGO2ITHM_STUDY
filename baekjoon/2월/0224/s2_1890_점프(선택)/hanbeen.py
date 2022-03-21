import sys
sys.stdin = open('B.txt')

# dfs
# def jump(i, j):
#     global count
#     temp = matrix[i][j]
#     if temp == 0:
#         count += 1
#         return
#     elif i + temp > N and j + temp > N:
#         return
#     else:
#         if i + temp < N:
#             jump(i+temp, j)
#         if j + temp < N:
#             jump(i, j+temp)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 마지막 값 출력
        if i == N-1 and j == N-1:
            print(dp[i][j])
        # 초기값 넣기
        elif i == 0 and j == 0:
            temp = matrix[i][j]
            if i + temp < N:
                dp[i+temp][j] += 1
            if j + temp < N:
                dp[i][j+temp] += 1
        # dp 채우는 과정
        else:
            if dp[i][j] != 0:
                temp = matrix[i][j]
                if i + temp < N:
                    dp[i+temp][j] += dp[i][j]
                if j + temp < N:
                    dp[i][j+temp] += dp[i][j]
