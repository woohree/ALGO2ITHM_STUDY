import sys
sys.stdin = open('G.txt')

R, C = map(int, sys.stdin.readline().split())

matrix = [list(sys.stdin.readline()) for _ in range(R)]

direction = [[0, 1, -1, 0, -1, 1], [0, 1, 1, 0, 1, 1], [1, 0, 0, -1, 1, -1], [1, 0, 0, 1, 1, 1]]

result = 0
for d in direction:
    visited = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if matrix[r][c] == '.' and matrix[r+d[0]][c+d[1]] == '.' and matrix[r+d[2]][c+d[3]] == 'X' and matrix[r+d[4]][c+d[5]] == 'X':
                if not visited[r][c] and not visited[r+d[0]][c+d[1]]:
                    visited[r][c] = 1
                    visited[r+d[0]][c+d[1]] = 1
                    result += 1
print(result)

# visited = [[0 for _ in range(C)] for _ in range(R)]
#
# result = 0
# for r in range(R):
#     for c in range(C):
#         if matrix[r][c] == '.' and matrix[r][c+1] == '.' and matrix[r-1][c] == 'X' and matrix[r-1][c+1] == 'X':
#             if not visited[r][c] and not visited[r][c+1]:
#                 visited[r][c] = 1
#                 visited[r][c+1] = 1
#                 result += 1
#
# visited = [[0 for _ in range(C)] for _ in range(R)]
#
# for r in range(R):
#     for c in range(C):
#         if matrix[r][c] == '.' and matrix[r][c+1] == '.' and matrix[r+1][c] == 'X' and matrix[r+1][c+1] == 'X':
#             if not visited[r][c] and not visited[r][c+1]:
#                 visited[r][c] = 1
#                 visited[r][c+1] = 1
#                 result += 1
#
# visited = [[0 for _ in range(C)] for _ in range(R)]
#
# for r in range(R):
#     for c in range(C):
#         if matrix[r][c] == '.' and matrix[r+1][c] == '.' and matrix[r][c-1] == 'X' and matrix[r+1][c-1] == 'X':
#             if not visited[r][c] and not visited[r+1][c]:
#                 visited[r][c] = 1
#                 visited[r+1][c] = 1
#                 result += 1
#
# visited = [[0 for _ in range(C)] for _ in range(R)]
#
# for r in range(R):
#     for c in range(C):
#         if matrix[r][c] == '.' and matrix[r+1][c] == '.' and matrix[r][c+1] == 'X' and matrix[r+1][c+1] == 'X':
#             if not visited[r][c] and not visited[r+1][c]:
#                 visited[r][c] = 1
#                 visited[r+1][c] = 1
#                 result += 1
#
# print(result)