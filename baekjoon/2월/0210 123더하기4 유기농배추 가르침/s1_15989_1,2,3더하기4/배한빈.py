import sys
sys.stdin = open('B.txt')

T = int(sys.stdin.readline().rstrip())

#     0  1  2  3
dp = [1, 1, 2, 3]
for i in range(4, 10001):
    dp.append(dp[i-1] + dp[i-2] - dp[i-3])  # 점화식
    if i % 3 == 0:
        dp[i] += 1

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])
