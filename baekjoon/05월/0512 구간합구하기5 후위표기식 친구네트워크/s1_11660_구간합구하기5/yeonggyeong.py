from pprint import pprint
import sys
sys.stdin = open('G.txt')

N, M = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 가로누적/세로누적/전체누적
new_matrix = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]

"""
0 0 0 0
1 2 3 4
2 3 4 5

[0, 0, 0] [0, 0, 0] [0, 0, 0] [0, 0, 0] [0, 0, 0]
[0, 0, 0] [1, 1, 1] [3, 2, 3] [6, 3, 6] [10, 4, 10]
[0, 0, 0], [2, 3, 3], [5, 5, 8], [9, 7, 15], [14, 9, 24]
"""
for row in range(1, N+1):
    for col in range(1, N+1):
        new_matrix[row][col][0] = matrix[row-1][col-1] + new_matrix[row][col-1][0]
        new_matrix[row][col][1] = matrix[row-1][col-1] + new_matrix[row-1][col][1]
        new_matrix[row][col][2] = new_matrix[row-1][col][2] + new_matrix[row][col][0]

for _ in range(M):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    print(new_matrix[end_x][end_y][2] - new_matrix[start_x-1][end_y][2] - new_matrix[end_x][start_y-1][2] + new_matrix[start_x-1][start_y-1][2])
