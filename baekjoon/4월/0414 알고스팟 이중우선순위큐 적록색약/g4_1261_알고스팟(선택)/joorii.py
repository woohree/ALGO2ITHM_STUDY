from collections import deque
import sys
sys.stdin = open('M.txt')

INF = float('inf')


def algo_spot():
    # 상 좌 하 우
    d = ((-1, 0), (0, -1), (1, 0), (0, 1))
    dist = [[INF for _ in range(M)] for _ in range(N)]
    dist[0][0] = 0      # 시작정점
    nexts = deque([[0, 0]])     # 시작지점으로 초기화

    while nexts:
        v = nexts.popleft()

        for dr, dc in d:
            nr, nc = v[0] + dr, v[1] + dc
            if 0 <= nr < N and 0 <= nc < M:
                if dist[nr][nc] > dist[v[0]][v[1]] + matrix[nr][nc]:    # 거리 재갱신
                    dist[nr][nc] = dist[v[0]][v[1]] + matrix[nr][nc]
                    nexts.append([nr, nc])

    print(dist[N - 1][M - 1])


# 가로 크기 M, 세로 크기 N
M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, map(str, sys.stdin.readline().rstrip()))) for _ in range(N)]
algo_spot()
