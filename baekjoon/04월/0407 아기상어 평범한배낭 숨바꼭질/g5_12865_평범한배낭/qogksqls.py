import sys
sys.stdin = open('B.txt')

'''
# 내 풀이
N, K = map(int, sys.stdin.readline().rstrip().split())
weight_and_value = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N+1)]
values = []
for i in range(1, N+1):
    for j in range(i, 0, -1):
        if dp[j-1][0] + weight_and_value[i-1][0] <= K:
            if dp[i][1] == 0:
                dp[i][0] = dp[j-1][0] + weight_and_value[i-1][0]
                dp[i][1] = dp[j-1][1] + weight_and_value[i-1][1]
                values.append(dp[i][1])
            else:
                if dp[i][1] <= dp[j-1][1] + weight_and_value[i-1][1]:
                    if dp[i][1] < dp[j-1][1] + weight_and_value[i-1][1]:
                        dp[i][0] = dp[j-1][0] + weight_and_value[i-1][0]
                        dp[i][1] = dp[j-1][1] + weight_and_value[i-1][1]
                        values.pop()
                        values.append(dp[i][1])
                    elif dp[i][1] == dp[j-1][1] + weight_and_value[i-1][1]:
                        if dp[i][0] > dp[j-1][0] + weight_and_value[i-1][0]:
                            dp[i][0] = dp[j-1][0] + weight_and_value[i-1][0]
                            dp[i][1] = dp[j-1][1] + weight_and_value[i-1][1]
print(max(values))
'''

'''
# pypy로 150ms 풀이 방법

N, K = map(int, sys.stdin.readline().rstrip().split())
weight_and_value = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

weight_and_value.sort()

dp = [0] * (K+1)
for w, v in weight_and_value:
    for i in range(K, 0, -1):
        if i-w < 0:  # 현재 무게에서 물건의 무게를 뺀 값이 음수인 경우
            break
        else:
            dp[i] = max(dp[i-w] + v, dp[i])  # 해당 가치와 현재 저장되있는 가치 중 max 를 저장

print(dp[-1])
'''
