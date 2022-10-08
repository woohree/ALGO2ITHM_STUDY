import sys
from collections import deque
sys.stdin = open('L.txt')


def bfs():
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    h_moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
    news = deque()
    news.append((0, 0, K))
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]         # 방문확인에 말 이동횟수(k) 포함
    visited[0][0][K] = 1
    t = 0

    while news:
        t += 1
        for _ in range(len(news)):
            r, c, k = news.popleft()
            if (r, c) == (H-1, W-1):                                    # 종료 조건
                return t-1
            for move in moves:                                          # 웡숭이 이동
                new_r, new_c = r + move[0], c + move[1]
                if 0 <= new_r < H and 0 <= new_c < W and not mat[new_r][new_c] and not visited[new_r][new_c][k]:
                    visited[new_r][new_c][k] = 1                        # 말 이동x => k는 그대로 
                    news.append((new_r, new_c, k))
            if k > 0:
                for h_move in h_moves:                                  # 말 이동
                    new_r, new_c = r + h_move[0], c + h_move[1]
                    if 0 <= new_r < H and 0 <= new_c < W and not mat[new_r][new_c] and not visited[new_r][new_c][k-1]:
                        visited[new_r][new_c][k-1] = 1                  # 말 이동 횟수 -1 에 저장
                        news.append((new_r, new_c, k-1))
    return -1


K = int(input())
W, H = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
ans = bfs()
print(ans)