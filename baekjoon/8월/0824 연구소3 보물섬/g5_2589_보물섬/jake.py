import sys
from collections import deque
sys.stdin = open('input.txt')

# 정보 받아오기
Y, X = map(int, input().split())
matrix = [list(input().strip()) for _ in range(Y)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 답
max_count = 0

for i in range(Y):
    for j in range(X):
        if matrix[i][j] == 'W':
            pass
        else:
            # check를 통해 방문 여부를 확인
            check = [[False]*X for _ in range(Y)]
            check[i][j] = True
            queue = deque()
            # Y, X축 좌표와 거리를 queue에 추가함
            queue.append([i, j, 1])
            while queue:
                y, x, count = queue.popleft()
                for k in range(4):
                    new_y = y+dy[k]
                    new_x = x+dx[k]
                    # 방문하지 않았고 범위 내에 있고 'W'가 아닌 곳에 한해 방문
                    if 0 <= new_x < X and 0 <= new_y < Y and matrix[new_y][new_x] != 'W' and check[new_y][new_x] == False:
                        check[new_y][new_x] = True
                        # 방문하고 나서는 방문 거리를 +1 함
                        queue.append([new_y, new_x, count+1])
                        if max_count < count:
                            max_count = count

print(max_count)