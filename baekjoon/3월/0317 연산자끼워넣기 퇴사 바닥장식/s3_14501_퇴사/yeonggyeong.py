import sys
sys.stdin = open('G.txt')


def get_profit(N):

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 마지막 날의 상담 소요시간이 하루인 날도 계산하기 위해서 n+1
    dp = [0] * (N + 1)

    # 마지막 날부터 진행
    for i in range(N-1, -1, -1):
        # 상담시간이 정해진 기간을 넘어가지 않으면
        if matrix[i][0] + i <= N:
            time = matrix[i][0]
            profit = matrix[i][1]
            dp[i] = max(profit + dp[i + time], dp[i+1])
        else:
            dp[i] = dp[i+1]

    max_profit = max(dp)
    return max_profit


N = int(input())
answer = get_profit(N)
print(answer)