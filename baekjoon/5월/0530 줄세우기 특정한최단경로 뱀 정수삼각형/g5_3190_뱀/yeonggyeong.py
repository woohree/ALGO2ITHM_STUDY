from collections import deque
import sys
sys.stdin = open('G.txt')

# 방향 바꾸기
def change_direction(d, idx):

    if d == 'L':
        return (idx - 1) % 4
    else:
        return (idx + 1) % 4        

def solution():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx, time = 0, 0
    x, y = 0, 0
    queue = deque()
    queue.append([0, 0])

    # 뱀이 있는 위치는 2로 표시
    matrix[x][y] = 2

    while True:
        time += 1
        x, y = x + dx[idx], y + dy[idx]
        # 인덱스 벗어나지 않고 뱀의 몸이 없을 때
        if 0 <= x < N and 0 <= y < N and matrix[x][y] != 2:
            # 비어있는 곳이면,
            if matrix[x][y] == 0:
                matrix[x][y] = 2
                queue.append([x, y])
                p_x, p_y = queue.popleft()
                # 가장 끝 부분을 비어있는 곳으로 변ㄱ녕
                matrix[p_x][p_y] = 0
            # 사과 있는 곳
            else:
                # 해당 위치를 뱀으로 변경
                matrix[x][y] = 2
                queue.append([x, y])
        else:
            return time

        # 방향을 바꿔야 하는지 확인하기
        if snake.get(str(time)):
            idx = change_direction(snake[str(time)], idx)

N = int(sys.stdin.readline())
apple_cnt = int(sys.stdin.readline())
apples = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(apple_cnt)]

snake_cnt = int(sys.stdin.readline())
snake = {}
for _ in range(snake_cnt):
    t, d = sys.stdin.readline().rstrip().split()
    snake[t] = d

matrix = [[0 for _ in range(N)] for _ in range(N)]

for apple_x, apple_y in apples:
    matrix[apple_x-1][apple_y-1] = 1

print(solution())