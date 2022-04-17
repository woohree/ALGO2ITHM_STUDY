import sys
sys.stdin = open('L.txt')


"""
같은 문자가 나오면 좌상단 값 +1,
 => 좌상단 dp값이 직전 문자까지 센 값, 따라서 그 값에 +1
그 외, max(위, 왼쪽)

[DP]
  A C A Y K P
C 0 1 1 1 1 1
A 1 1 2 2 2 2
P 1 1 2 2 2 3
C 1 2 2 2 2 3
A 1 2 3 3 3 3
K 1 2 3 3 4 4
"""


def LCS(A, B):
    dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if B[i-1] == A[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp


A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline())
ans = LCS(A, B)
print(ans[-1][-1])
