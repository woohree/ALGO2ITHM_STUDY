import sys, copy
sys.stdin = open('G.txt')

def dfs(x, y, eat_fish, matrix):
    global max_fish

    eat_fish += matrix[x][y][0]
    matrix[x][y][0] = 0
    max_fish = max(max_fish, eat_fish)

    for fish in range(1, 17):
        fish_x, fish_y = -1, -1

        for row in range(4):
            for col in range(4):
                if matrix[row][col][0] == fish:
                    fish_x, fish_y = row, col
                    fish_d = matrix[row][col][1]
                    break
        if (fish_x, fish_y) == (-1, -1):
            continue

        for i in range(8):
            new_d = (fish_d + i) % 8
            new_x, new_y = fish_x + dx[new_d], fish_y + dy[new_d]

            if 0 <= new_x < 4 and 0 <= new_y < 4 and (new_x, new_y) != (x, y):
                matrix[fish_x][fish_y][1] = new_d
                matrix[fish_x][fish_y], matrix[new_x][new_y] = matrix[new_x][new_y], matrix[fish_x][fish_y]
                break
        
    shark_d = matrix[x][y][1]
    for i in range(1, 5):
        shark_x, shark_y = x + dx[shark_d] * i, y + dy[shark_d] * i

        if 0 <= shark_x < 4 and 0 <= shark_y < 4 and matrix[shark_x][shark_y][0] != 0:
            dfs(shark_x, shark_y, eat_fish, copy.deepcopy(matrix))

        

matrix = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    inputs = list(map(int, input().split()))
    for j in range(4):
        matrix[i][j] = [inputs[j * 2], inputs[j * 2 + 1] -1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
max_fish = 0
dfs(0, 0, 0, matrix)
print(max_fish)