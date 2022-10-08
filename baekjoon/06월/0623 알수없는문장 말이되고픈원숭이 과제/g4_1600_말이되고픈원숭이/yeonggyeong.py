from collections import deque
import sys
sys.stdin = open('G.txt')

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]

monkey = [(0, 1), (1, 0), (0, -1), (-1, 0)]
horse = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]

# 말 무브가 가능한 횟수만큼 생성
visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

def bfs():
    q = deque()
    q.append((0, 0, K))
    
    while q:
        # x좌표 / y좌표 / 남아있는 말 무브
        x, y, remain = q.popleft()

        # 종료 조건
        if x == H-1 and y == W-1:
            return visited[x][y][remain]

        # 말처럼 움직일 수 있을 때
        if remain > 0:
            for idx in range(8):
                new_x, new_y = x + horse[idx][0], y + horse[idx][1]
                # 인덱스 범위 / 벽 x / 말처럼 움직일 수 있을때
                if 0 <= new_x < H and 0 <= new_y < W and matrix[new_x][new_y] != 1 and not visited[new_x][new_y][remain-1]:
                    visited[new_x][new_y][remain-1] = visited[x][y][remain] + 1
                    q.append((new_x, new_y, remain-1))
        for idx in range(4):
            new_x, new_y = x + monkey[idx][0], y + monkey[idx][1]
            if 0 <= new_x < H and 0 <= new_y < W and matrix[new_x][new_y] != 1 and not visited[new_x][new_y][remain]:
                visited[new_x][new_y][remain] = visited[x][y][remain] + 1
                q.append((new_x, new_y, remain))
    return -1
print(bfs())





# from collections import deque
# import sys
# K = int(sys.stdin.readline())
# W, H = map(int, sys.stdin.readline().split())
#
# matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
#
# move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# horse = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]
#
# visited = [[0 for _ in range(W)] for _ in range(H)]
# def bfs():
#     q = deque()
#     q.append((0, 0, 0, K))
#
#     while q:
#         x, y, cnt, remain = q.popleft()
#
#         if remain >= 1:
#             for idx in range(8):
#                 new_x, new_y = x + horse[idx][0], y + horse[idx][1]
#                 if 0 <= new_x < H and 0 <= new_y < W and not matrix[new_x][new_y]:
#                     if not visited[new_x][new_y] or visited[new_x][new_y] < remain - 1:
#                         if new_x == H - 1 and new_y == W-1:
#                             return cnt + 1
#                         visited[new_x][new_y] = remain-1
#                         q.append((new_x, new_y, cnt+1, remain-1))
#         for idx in range(4):
#             new_x, new_y =  x + move[idx][0], y + move[idx][1]
#             if 0 <= new_x < H and 0 <= new_y < W and not matrix[new_x][new_y]:
#                 if not visited[new_x][new_y] or visited[new_x][new_y] < remain:
#                     if new_x == H - 1 and new_y == W-1:
#                             return cnt + 1
#                     visited[new_x][new_y] = remain
#                     q.append((new_x, new_y, cnt+1, remain))
#     return -1
# print(bfs())