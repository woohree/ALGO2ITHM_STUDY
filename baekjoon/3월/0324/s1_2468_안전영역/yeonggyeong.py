import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('G.txt')


def dfs(row, col):
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for idx in range(4):
        row, col = row+dx[idx], col+dy[idx]

        if 0 <= row < N and 0 <= col < N and new_matrix[row][col] == False:
            new_matrix[row][col] = 1
            dfs(row, col)
        row, col = row-dx[idx], col-dy[idx]



N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 빗물의 최대높이
max_value = matrix[0][0]

for row in range(N):
    for col in range(N):
        max_value = matrix[row][col] if matrix[row][col] > max_value else max_value

# 안전한 영역의 최대 개수
max_island = 0

# 비가 오지 않을때부터 ~ 최대 높이까지 반복 
for height in range(max_value):

    # 높이가 다를때 마다 초기화
    new_matrix = [[False for _ in range(N)] for _ in range(N)]

    # 빗물의 높이보다 작을때는 99로 침수되었다고 표시하기
    for row in range(N):
        for col in range(N):
            if matrix[row][col] <= height:
                new_matrix[row][col] = 99

    # 섬의 개수를 세기 위한 변수 선언
    island = 0
    for row in range(N):
        for col in range(N):
            if new_matrix[row][col] == False:
                island += 1
                dfs(row, col)
                
    # 섬의 최대 개수 구하기
    if island > max_island:
        max_island = island
        max_height = height

print(max_island)