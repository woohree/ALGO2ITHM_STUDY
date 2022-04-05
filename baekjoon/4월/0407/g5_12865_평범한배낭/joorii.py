import sys
sys.stdin = open('M.txt')


def backpacking():
    # row = 물품의 인덱스, col = 최대 무게
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(K + 1):
            if i == 0 or j == 0:        # 가능한 물품의 개수가 0이거나, 무게가 0일 때
                dp[i][j] = 0
            elif loads[i - 1][0] <= j:  # 해당 물품의 무게 이상으로 고려가 가능할 때
                dp[i][j] = max(loads[i - 1][1] + dp[i - 1][j - loads[i - 1][0]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][K]


# 물품의 수 N, 최대 무게 K
N, K = map(int, input().split())
# [물건의 무게 W, 물건의 가치 V]
loads = [list(map(int, input().split())) for _ in range(N)]
print(backpacking())
