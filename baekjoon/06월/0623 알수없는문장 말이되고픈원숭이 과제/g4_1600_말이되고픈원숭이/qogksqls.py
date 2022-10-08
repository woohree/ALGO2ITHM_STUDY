import sys
from collections import deque
sys.stdin = open('B.txt')


def bfs(row, col):
    visited = [[[-1, 0] for _ in range(W)] for _ in range(H)]
    visited[0][0] = [0, 0]
    q = deque()
    q.append((row, col))
    while q:
        r, c = q.popleft()
        if r == H-1 and c == W-1:
            return visited[r][c][0]
        for move in monkey_moves:
            dr, dc = r + move[0], c + move[1]
            if 0 <= dr < H and 0 <= dc < W and matrix[dr][dc] != 1:
                if visited[dr][dc][0] == -1:
                    q.append((dr, dc))
                    visited[dr][dc] = [visited[r][c][0] + 1, visited[r][c][1]]
                elif visited[r][c][1] < visited[dr][dc][1]:
                    q.append((dr, dc))
                    visited[dr][dc] = [visited[r][c][0] + 1, visited[r][c][1]]
        if visited[r][c][1] < K:
            for move in horse_moves:
                dr, dc = r + move[0], c + move[1]
                if 0 <= dr < H and 0 <= dc < W and matrix[dr][dc] != 1:
                    if visited[dr][dc][0] == -1:
                        q.append((dr, dc))
                        visited[dr][dc] = [visited[r][c][0] + 1, visited[r][c][1] + 1]
                    elif visited[r][c][1] + 1 < visited[dr][dc][1]:
                        q.append((dr, dc))
                        visited[dr][dc] = [visited[r][c][0] + 1, visited[r][c][1] + 1]

    return visited[-1][-1][0]


K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]

horse_moves = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
monkey_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(bfs(0, 0))
