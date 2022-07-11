import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())

tetra = []
n, m = 0, 1
while n < N:
    n += (m * (m + 1)) // 2
    tetra.append(n)
    m += 1

dp = [float(1e9)] * (N+1)
for i in range(1, N+1):
    for t in tetra:
        if t == i:
            dp[i] = 1
            break
        if t > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - t])
print(dp[N])
