import sys
sys.stdin = open('G.txt')

def operate_air_cleaner(air_cleaner):
    # 반시계 방향
    for i in range(air_cleaner[0]-2, -1, -1):
        matrix[i+1][0] = matrix[i][0]

    for j in range(1, C):
        matrix[0][j-1] = matrix[0][j]

    for k in range(1, air_cleaner[0]+1):
        matrix[k-1][C-1] = matrix[k][C-1]

    for l in range(C-2, 0, -1):
        matrix[air_cleaner[0]][l+1] = matrix[air_cleaner[0]][l]

    matrix[air_cleaner[0]][1] = 0

    # 시계 방향
    for i in range(air_cleaner[1]+2, R):
        matrix[i-1][0] = matrix[i][0]

    for j in range(1, C):
        matrix[R-1][j-1] = matrix[R-1][j]

    for k in range(R-2, air_cleaner[1]-1, -1):
        matrix[k+1][C-1] = matrix[k][C-1]

    for l in range(C-2, 0, -1):
        matrix[air_cleaner[1]][l+1] = matrix[air_cleaner[1]][l]

    matrix[air_cleaner[1]][1] = 0


R, C, T = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기청정기 위치 찾기
for i in range(R):
    if -1 in matrix[i]:
        air_cleaner = (i, i+1)
        break

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

for t in range(T):
    temp = []
    for row in range(R):
        for col in range(C):
            # 미세먼지 값이 5 이상인 위치만 찾기
            if matrix[row][col] >= 5:
                dust = matrix[row][col] // 5
                cnt = 0
                for idx in range(4):
                    new_x, new_y = row + dx[idx], col + dy[idx]
                    if 0 <= new_x < R and 0 <= new_y < C and matrix[new_x][new_y] != -1:
                        cnt += 1
                        temp.append((dust, new_x, new_y))
                
                matrix[row][col] = matrix[row][col] - dust * cnt
    for d, x, y in temp:
        matrix[x][y] += d

    operate_air_cleaner(air_cleaner)
    
answer = sum([sum(i) for i in matrix])
print(answer + 2)


# import sys
# from pprint import pprint
# sys.stdin = open('G.txt')

# # 확산시키기
# def dfs(r, c):
#     global temp, position
#     # 확산된 미세먼지가 아닌 원래 있던 미세먼지로 표시
#     visited[r][c] = 1
#     dust = matrix[r][c] // 5
#     cnt = 0
#     for idx in range(4):
#         new_r, new_c = r + dx[idx], c + dy[idx]
#         # 공기청정기 아닐때
#         if 0 <= new_r < R and 0 <= new_c < C and matrix[new_r][new_c] != -1:
#             cnt += 1
#             # 원래 미세먼지일때 변수에 담아주기
#             if visited[new_r][new_c] == 1:
#                 temp.append(dust)
#                 position.append((r, c))
#             # 동시에 미세먼지 확산 진행되기 때문에 원래 미세먼지가 있던 자리일때
#             elif visited[new_r][new_c] == 0 and matrix[new_r][new_c] > 0:
#                 dfs(new_r, new_c)
#                 matrix[new_r][new_c] += dust
#             # 확산된 미세먼지 자리거나 미세먼지 없을때
#             else:
#                 matrix[new_r][new_c] += dust
#                 visited[new_r][new_c] = -1

#     matrix[r][c] = matrix[r][c] - dust * cnt
#     # 확산 완료 되었다고 표시하기
#     visited[r][c] = -1
#     # dfs 돌때 변수에 담아둔 미세먼지 더해주기
#     if temp and position[0] != (r,c):
#         matrix[r][c] += sum(temp)
#         temp, position = [], []

# def operate_air_cleaner(air_cleaner):
#     # 반시계 방향
#     for i in range(air_cleaner[0]-2, -1, -1):
#         matrix[i+1][0] = matrix[i][0]

#     for j in range(1, C):
#         matrix[0][j-1] = matrix[0][j]

#     for k in range(1, air_cleaner[0]+1):
#         matrix[k-1][C-1] = matrix[k][C-1]

#     for l in range(C-2, 0, -1):
#         matrix[air_cleaner[0]][l+1] = matrix[air_cleaner[0]][l]

#     matrix[air_cleaner[0]][1] = 0

#     # 시계 방향
#     for i in range(air_cleaner[1]+2, R):
#         matrix[i-1][0] = matrix[i][0]

#     for j in range(1, C):
#         matrix[R-1][j-1] = matrix[R-1][j]

#     for k in range(R-2, air_cleaner[1]-1, -1):
#         matrix[k+1][C-1] = matrix[k][C-1]

#     for l in range(C-2, 0, -1):
#         matrix[air_cleaner[1]][l+1] = matrix[air_cleaner[1]][l]

#     matrix[air_cleaner[1]][1] = 0


# R, C, T = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# for i in range(R):
#     if -1 in matrix[i]:
#         air_cleaner = (i, i+1)
#         break

# dx = [-1, 0, 0, 1]
# dy = [0, 1, -1, 0]

# for t in range(T):
#     visited = [[0 for _ in range(C)] for _ in range(R)]
#     temp = []
#     position = []
#     for row in range(R):
#         for col in range(C):
#             if matrix[row][col] > 0 and not visited[row][col]:
#                 dfs(row, col)
#     operate_air_cleaner(air_cleaner)
# answer = sum([sum(i) for i in matrix])
# print(answer+2)