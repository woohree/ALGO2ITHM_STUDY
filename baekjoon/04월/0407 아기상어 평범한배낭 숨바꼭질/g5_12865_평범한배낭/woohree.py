import sys
sys.stdin = open('L.txt')


def get_maximum_value():
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(1, K+1):
            if stuffs[i-1][0] <= w:         # 확인할 물건의 무게가 목표 무게와 같거나 작다면,
                # ((목표 무게-현재 무게), 이전 물건)의 최대 벨류 + 현재 물건의 벨류 vs (같은 무게, 이전 물건)의 최대 벨류를 비교
                dp[i][w] = max(stuffs[i-1][1]+dp[i-1][w-stuffs[i-1][0]], dp[i-1][w])
            else:                           # 아니라면, 같은 무게 이전 물건의 최대 벨류가 현재까지의 최대 벨류
                dp[i][w] = dp[i-1][w]
    return dp[-1][-1]


N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]
ans = get_maximum_value()
print(ans)