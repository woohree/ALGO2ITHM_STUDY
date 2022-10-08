from heapq import heappop, heappush
import sys
sys.stdin = open('M.txt')


def down_road():
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = [[0] * N for _ in range(M)]
    nexts = [(-matrix[0][0], 0, 0)]     # (높이, 행 좌표, 열 좌표) -오름차순 정렬
    visited[0][0] = 1

    while nexts:
        cnt, cur_r, cur_c = heappop(nexts)

        for move in moves:
            next_r, next_c = cur_r + move[0], cur_c + move[1]
            # 배열의 범위를 넘지 않고, 이전 방문 보다 숫자가 작을 때
            if 0 <= next_r < M and 0 <= next_c < N and matrix[next_r][next_c] < -cnt:
                if not visited[next_r][next_c]:     # 방문한 적이 없으면
                    heappush(nexts, (-matrix[next_r][next_c], next_r, next_c))
                visited[next_r][next_c] += visited[cur_r][cur_c]

    return visited[-1][-1]


# 세로 M, 가로 N
M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
print(down_road())
