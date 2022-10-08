import sys
sys.stdin = open('M.txt')


def count_panels(r, c):
    # 수직
    V = [[-1, 0], [1, 0]]
    # 수평
    H = [[0, -1], [0, 1]]

    if panels[r][c] == '':
        return 0

    # 수직으로 | 모양이 있으면 없을 때까지 탐색하면서 빈 공간으로 변경
    elif panels[r][c] == '|':
        panels[r][c] = ''
        for v in V:
            # 범위 제한
            if 0 <= r + v[0] < N and 0 <= c + v[1] < M:
                if panels[r + v[0]][c + v[1]] == '|':
                    count_panels(r + v[0], c + v[1])
        return 1

    # 수평으로 - 모양이 있으면 없을 때까지 탐색하면서 빈 공간으로 변경
    elif panels[r][c] == '-':
        panels[r][c] = ''
        for h in H:
            # 범위 제한 
            if 0 <= r + h[0] < N and 0 <= c + h[1] < M:
                if panels[r + h[0]][c + h[1]] == '-':
                    count_panels(r + h[0], c + h[1])
        return 1


# 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())

panels = [list(map(str, input())) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        count += count_panels(i, j)

print(count)
