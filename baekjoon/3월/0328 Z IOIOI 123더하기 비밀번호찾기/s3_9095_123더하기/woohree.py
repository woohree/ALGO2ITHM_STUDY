import sys
sys.stdin = open('L.txt')


def dfs(i):
    global cnt

    if i == n:
        cnt += 1
        return

    for j in range(1, 4):
        if i + j <= n:
            dfs(i+j)


def dpp(n):
    dp = [1, 2, 4]
    if n > 3:
        for i in range(3, n):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
        return dp[-1]
    else:
        return dp[n-1]


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    # cnt = 0
    # for i in range(1, 4):
    #     dfs(i)
    # print(cnt)
    ans = dpp(n)
    print(ans)