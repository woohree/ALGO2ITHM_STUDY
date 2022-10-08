from collections import deque
import sys
sys.stdin = open('M.txt')


def dummy(r, c):
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    count = idx = 0             # count는 이동 시간, idx는 방향
    snake = deque()             # 왼쪽이 뱀의 머리, 오른쪽이 뱀의 꼬리
    snake.append((0, 0))
    start_r, start_c = r, c
    board[start_r][start_c] = -1            # 뱀의 위치 -1

    while 1:
        if moves:
            cur = moves[0]
            if int(cur[0]) == count:
                moves.popleft()
                if cur[1] == 'L':
                    idx = (idx - 1) % 4
                    continue
                elif cur[1] == 'D':
                    idx = (idx + 1) % 4
                    continue

        start_r += d[idx][0]
        start_c += d[idx][1]

        if 0 <= start_r < N and 0 <= start_c < N:   # 보드 안에 위치해 있을 때, 즉 벽에 안 부딪힐 때
            if board[start_r][start_c] == -1:       # 뱀과 부딪힐 때
                return count
            elif board[start_r][start_c] == 1:      # 사과가 있을 떄
                board[start_r][start_c] = -1
                snake.appendleft((start_r, start_c))
            else:
                board[start_r][start_c] = -1
                snake.appendleft((start_r, start_c))
                last_r, last_c = snake.pop()
                board[last_r][last_c] = 0
            count += 1
        else:
            return count

    return count


# 보드의 크기 N
N = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]

# 사과의 개수 K
K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1         # 사과 위치 1

# 뱀의 방향 변환 횟수 L
L = int(sys.stdin.readline())
moves = deque(list(map(str, sys.stdin.readline().split())) for _ in range(L))

print(dummy(0, 0) + 1)
