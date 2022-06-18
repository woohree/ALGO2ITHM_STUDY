import sys
sys.stdin = open('L.txt')


def dfs(r, c, d):
    global cnt
    if (r, c) == (N-1, N-1):                        # 도착
        cnt += 1
        return

    for n in nums:
        new_d = d + n
        if 0 <= new_d < 3 and abs(new_d - d) <= 1:  # 새로운 방향 조건(0~2, 현재 방향에서 45도 범위)
            new_r, new_c = r + moves[new_d][0], c + moves[new_d][1]
            if 0 <= new_r < N and 0 <= new_c < N and not mat[new_r][new_c]:
                if new_d == 1:                      # 대각선
                    if not mat[new_r-1][new_c] and not mat[new_r][new_c-1]:
                        dfs(new_r, new_c, new_d)
                else:                               # 오른쪽, 아래
                    dfs(new_r, new_c, new_d)


N = int(input())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cnt = 0
moves = ((0, 1), (1, 1), (1, 0))
nums = (-1, 0, 1)
if mat[N-1][N-1]:
    print(cnt)
else:
    dfs(0, 1, 0)
    print(cnt)