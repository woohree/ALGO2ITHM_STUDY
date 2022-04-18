from collections import deque
import sys
sys.stdin = open('G.txt')

N, M, K = map(int, input().split())

fireballs = deque()
matrix = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])
    # matrix[r-1][c-1].append([m, s, d])


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireballs:
        ball_x, ball_y, ball_m, ball_s, ball_d = fireballs.popleft()

        # 각 마지막 행/열은 처음 행/열과 이어져있음
        new_x = (ball_x + ball_s * dx[ball_d]) % N 
        new_y = (ball_y + ball_s * dy[ball_d]) % N

        matrix[new_x][new_y].append([ball_m, ball_s, ball_d])
        # if not (new_x == ball_x and new_y == ball_y):
        #     matrix[new_x][new_y].append([ball_m, ball_s, ball_d])
        #     if len(matrix[ball_x][ball_y]) >= 2:
        #         for i in range(len(matrix[ball_x][ball_y])):
        #             if i == [ball_m, ball_s, ball_d]:
        #                 matrix[ball_x][ball_y].pop(i)
        #     else:
        #         matrix[ball_x][ball_y] = []
        #
        # else:
        #     matrix[ball_x][ball_y] = []
    
    for row in range(N):
        for col in range(N):

            if len(matrix[row][col]) >= 2:
                mass, speed, cnt, cnt_odd = 0, 0, 0, 0
                while matrix[row][col]:
                    ball = matrix[row][col].pop()
                    mass += ball[0]
                    speed += ball[1]
                    cnt += 1
                    # 홀수의 개수가 0이거나 총 개수와 같다면 
                    if ball[2] % 2:
                        cnt_odd += 1
                
                mass = mass // 5
                if mass == 0:
                    continue

                speed = speed // cnt
                if cnt == cnt_odd or cnt_odd == 0:
                    direction = [0, 2, 4, 6]
                else:
                    direction = [1, 3, 5, 7]
                
                for idx in range(4):
                    fireballs.append([row, col, mass, speed, direction[idx]])
            
            if len(matrix[row][col]) == 1:
                ball = matrix[row][col].pop()
                fireballs.append([row, col, ball[0], ball[1], ball[2]])

print(sum([i[2] for i in fireballs]))