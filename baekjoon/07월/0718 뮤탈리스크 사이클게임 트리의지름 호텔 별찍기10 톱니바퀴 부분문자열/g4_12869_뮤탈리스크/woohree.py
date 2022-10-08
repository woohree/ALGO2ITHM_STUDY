import sys
sys.stdin = open('W.txt')


def dfs(x, y, z):
    if x == 0 and y == 0 and z == 0:                    # 다 죽은 경우
        return 0

    if dp[x][y][z]:                                     # 했던 경우
        return dp[x][y][z]

    dp[x][y][z] = 1 + min(
        dfs(max(x-9, 0), max(y-3, 0), max(z-1, 0)),     # 체력이 음수가 되면 0으로 하기 위한 max
        dfs(max(x-9, 0), max(y-1, 0), max(z-3, 0)),
        dfs(max(x-3, 0), max(y-9, 0), max(z-1, 0)),
        dfs(max(x-3, 0), max(y-1, 0), max(z-9, 0)),
        dfs(max(x-1, 0), max(y-3, 0), max(z-9, 0)),
        dfs(max(x-1, 0), max(y-9, 0), max(z-3, 0))
    )

    return dp[x][y][z]


N = int(input())
SCVs = list(map(int, input().split()))
while len(SCVs) < 3:                                    # SCV가 셋보다 적으면, 죽은 SCV 넣기
    SCVs.append(0)
dp = [[[0]*61 for _ in range(61)] for _ in range(61)]   # dp[x][y][z]는 각 SCV의 체력(x, y, z)에 따른 공격 횟수
print(dfs(SCVs[0], SCVs[1], SCVs[2]))
