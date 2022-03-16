import sys
sys.stdin = open('M.txt')
"""
 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
50 |40 |30 |20 |10 |60 |80 |90 |   |   
 5 | 5 | 5 | 5 | 5 | 6 | 8 |10 |   |
"""

def max_profit():
    for i in range(N):
        # 상담기간이 퇴직일을 넘어가는 경우
        if i + tasks[i][0] > N:
            continue
        temp_max = 0
        # dp에 저장된 이전의 합 중 가장 큰 값 구하기
        for j in range(i):
            if dp[j][0] <= i and dp[j][1] > temp_max:
                temp_max = dp[j][1]
        # 다음 가능한 상담일로 변경
        dp[i][0] = i + tasks[i][0]
        # 수익의 최대 합으로 변경
        dp[i][1] = temp_max + tasks[i][1]

    # dp에 저장된 수익의 합 중 가장 큰 값을 리턴
    max_sum = 0
    for i in range(len(dp)):
        if dp[i][1] > max_sum:
            max_sum = dp[i][1]

    return max_sum


N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

# 다음 idx, 수익 합
dp = [[0, 0] for _ in range(N)]
print(max_profit())
