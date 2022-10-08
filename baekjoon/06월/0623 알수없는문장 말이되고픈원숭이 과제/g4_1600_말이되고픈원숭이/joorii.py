from collections import deque
import sys
sys.stdin = open('M.txt')


def monkey():
    horse_moves = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2))
    monkey_moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    nexts = deque([(0, 0, 0, 0)])    # (행 좌표, 열 좌표, 이동 횟수, 말 움직임 횟수)
    visited[0][0] = (1, 0)

    while nexts:
        cur_r, cur_c, cnt, h_cnt = nexts.popleft()

        if cur_r == H - 1 and cur_c == W - 1:   # 종료조건
            return cnt

        if h_cnt < K:     # 말의 움직임으로 움직일 수 있을 때
            for dr, dc in horse_moves:
                next_r, next_c = cur_r + dr, cur_c + dc
                if 0 <= next_r < H and 0 <= next_c < W and matrix[next_r][next_c] != 1:
                    if not visited[next_r][next_c][0] or visited[next_r][next_c][1] > h_cnt + 1:    # 방문한 적 없거나 말의 움직임 룃수가 더 적을 떄
                        visited[next_r][next_c] = (1, h_cnt + 1)
                        nexts.append((next_r, next_c, cnt + 1, h_cnt + 1))

        for dr, dc in monkey_moves:
            next_r, next_c = cur_r + dr, cur_c + dc
            if 0 <= next_r < H and 0 <= next_c < W and matrix[next_r][next_c] != 1:
                if not visited[next_r][next_c][0] or visited[next_r][next_c][1] > h_cnt:    # 방문한 적 없거나 말의 움직임 룃수가 더 적을 떄
                    visited[next_r][next_c] = (1, h_cnt)
                    nexts.append((next_r, next_c, cnt + 1, h_cnt))
    return -1


K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
matrix = []
visited = [[(0, 0)] * W for _ in range(H)]      # (방문 체크, 말 움직임 횟수)
for _ in range(H):
    matrix.append(list(map(int, sys.stdin.readline().split())))
print(monkey())
