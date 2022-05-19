from pprint import pprint
import sys
sys.stdin = open('G.txt')

# 2 * 2 행렬에서 하나의 위치만 빼고 초기화
def fill_floor(x, y, matrix, number, not_x, not_y):
    for row in range(x[0], x[1]):
        for col in range(y[0], y[1]):
            if (row, col) != (not_x, not_y):
                    matrix[row][col] = number


N = int(input())
water_x, water_y = map(int, input().split())
water_x, water_y = 2 ** N - water_y, water_x - 1

if N == 1:
    matrix = [[1 for _ in range(2**N)] for _ in range(2**N)]
    matrix[water_x][water_y] = -1

elif N == 2:
    matrix = [[1 for _ in range(2**N)] for _ in range(2**N)]
    if (water_x, water_y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        matrix[water_x][water_y] = -1
        fill_floor([1, 3], [1, 3], matrix, 2, 1, 1)
        fill_floor([0, 2], [2, 4], matrix, 3, 1, 2)
        fill_floor([2, 4], [0, 2], matrix, 4, 2, 1)
        fill_floor([2, 4], [2, 4], matrix, 5, 2, 2)
    elif (water_x, water_y) in [(0, 2), (0, 3), (1, 2), (1, 3)]:
        matrix[water_x][water_y] = -1
        fill_floor([1, 3], [1, 3], matrix, 2, 1, 2)
        fill_floor([0, 2], [0, 2], matrix, 3, 1, 1)
        fill_floor([2, 4], [0, 2], matrix, 4, 2, 1)
        fill_floor([2, 4], [2, 4], matrix, 5, 2, 2)
    elif (water_x, water_y) in [(2, 0), (2, 1), (3, 0), (3, 1)]:
        matrix[water_x][water_y] = -1
        fill_floor([1, 3], [1, 3], matrix, 2, 2, 1)
        fill_floor([0, 2], [0, 2], matrix, 3, 1, 1)
        fill_floor([0, 2], [2, 4], matrix, 4, 1, 2)
        fill_floor([2, 4], [2, 4], matrix, 5, 2, 2)
    else:
        matrix[water_x][water_y] = -1
        fill_floor([1, 3], [1, 3], matrix, 2, 2, 2)
        fill_floor([0, 2], [0, 2], matrix, 3, 1, 1)
        fill_floor([0, 2], [2, 4], matrix, 4, 1, 2)
        fill_floor([2, 4], [0, 2], matrix, 5, 2, 1)


for row in matrix:
    print(' '.join(map(str, row)))