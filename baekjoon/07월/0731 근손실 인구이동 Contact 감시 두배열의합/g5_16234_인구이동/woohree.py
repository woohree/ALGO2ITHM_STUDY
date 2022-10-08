import sys
sys.setrecursionlimit(10**4)
sys.stdin = open('W.txt')


def dfs(r, c):                                          # 국경 개방하기!
    global cnt
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c] and L <= abs(mat[r][c]-mat[new_r][new_c]) <= R:
            visited[new_r][new_c] = 1
            border.append((new_r, new_c))               # 좌표
            cnt += mat[new_r][new_c]                    # 인구수
            dfs(new_r, new_c)


N, L, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
for t in range(2001):                                   # 매일 새롭게 시작
    visited = [[0]*N for _ in range(N)]
    borders = []                                        # ([좌표들], 총 인구수) 포맷으로 저장
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt = mat[i][j]
                border = [(i, j)]
                visited[i][j] = 1
                dfs(i, j)
                if len(border) > 1:                     # 둘 이상 국경개방했을 때만 추가
                    borders.append((border, cnt))
    if not borders:                                     # 종료조건, 국경개방한 곳이 없을 때
        print(t)
        break
    for border in borders:                              # 개방했으면 인구수 갱신
        for b in border[0]:
            mat[b[0]][b[1]] = border[1] // len(border[0])
