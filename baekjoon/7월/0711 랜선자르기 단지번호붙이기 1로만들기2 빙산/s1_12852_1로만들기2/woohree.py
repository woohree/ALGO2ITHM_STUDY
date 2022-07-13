import sys
sys.stdin = open('L.txt')


# 구글링 ㅜㅜ
N = int(input())
dp = [[0, []] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1].append(1)

for i in range(2, N+1):                         # 2부터 연산횟수, 거쳐간 숫자들 함께 저장하는 dp
    dp[i][0] = dp[i-1][0] + 1                   # -1인 경우
    dp[i][1] = dp[i-1][1] + [i]
    if not i % 3 and dp[i//3][0]+1 < dp[i][0]:  # 3으로 나누는 경우
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
    if not i % 2 and dp[i//2][0]+1 < dp[i][0]:  # 2로 나누는 경우
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]

print(dp[N][0])
print(*dp[N][1][::-1])
