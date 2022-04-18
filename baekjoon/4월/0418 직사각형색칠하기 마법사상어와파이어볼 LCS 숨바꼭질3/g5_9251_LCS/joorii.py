import sys
sys.stdin = open('M.txt')


A = input()
B = input()

dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

for i in range(len(B) + 1):
    for j in range(len(A) + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif B[i - 1] != A[j - 1]:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        else:           # 알파벳이 동일하면, 1 추가
            dp[i][j] = dp[i - 1][j - 1] + 1

print(dp[-1][-1])
