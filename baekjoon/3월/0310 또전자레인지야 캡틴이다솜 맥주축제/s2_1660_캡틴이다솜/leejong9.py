import sys

input = sys.stdin.readline

n = int(input())

bomb = []
num = 0
a = 1

while n > num:
    num += (a * (a + 1)) // 2
    bomb += [num]
    a += 1

dp = [300001 for _ in range(n + 1)]
for i in range(1, n + 1):
    for b in bomb:
        if b == i:
            dp[i] = 1
            break
        if b > i:
            break
        dp[i] = min(dp[i], dp[i - b] + 1)

print(dp[n])