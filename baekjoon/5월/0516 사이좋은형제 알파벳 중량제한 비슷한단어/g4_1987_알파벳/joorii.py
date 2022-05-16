# python 3 시간초과
import sys
sys.stdin = open('M.txt')


def dfs(r, c, cnt, p):      # r 행 인덱스, c 열 인덱스, cnt 이동횟수, p 방문문자열
    global ans
    drc = ((-1, 0), (1, 0), (0, -1), (0, 1))

    if cnt > ans:
        ans = cnt

    for d in drc:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in p:
                dfs(nr, nc, cnt + 1, p + board[nr][nc])


R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
ans = 0
dfs(0, 0, 1, board[0][0])
print(ans)
