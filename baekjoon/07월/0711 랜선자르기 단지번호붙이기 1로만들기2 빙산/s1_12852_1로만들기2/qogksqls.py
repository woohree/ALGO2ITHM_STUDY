import sys
from collections import deque
sys.stdin = open('B.txt')


def bfs(n, arr):
    q = deque()
    q.append(1)
    while q:
        i = q.popleft()
        if i*3 <= n and arr[i*3] == 0:
            arr[i*3] = i
            q.append(i*3)
        if i*2 <= n and arr[i*2] == 0:
            arr[i*2] = i
            q.append(i*2)
        if i+1 <= n and arr[i+1] == 0:
            arr[i+1] = i
            q.append(i+1)
        if i * 3 == n or i * 2 == n or i + 1 == n:
            return


N = int(input())
dp = [0] * (N+1)
dp[1] = 1
bfs(N, dp)
ans = [N]
j = N
while N != 1:  # 100% 조건
    ans.append(dp[j])
    j = dp[j]
    if j == 1:
        break
print(len(ans) - 1)
print(*ans)
