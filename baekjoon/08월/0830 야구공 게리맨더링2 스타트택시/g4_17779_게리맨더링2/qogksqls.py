import sys
sys.stdin = open('B.txt')

'''
1. 개빡친다 진짜
2. 문제 이해 못한듯
'''


def count_p(x, y, r, c):  # 1, 1, 1, 2
    # 1구역
    No1, j = 0, c
    for i in range(r+x):
        No1 += sum(matrix[i][:j+1])
        if i+1 >= r:
            j -= 1
    min_p = No1
    max_p = No1

    # 2구역
    No2, j = 0, c+1
    for i in range(r+y+1):
        No2 += sum(matrix[i][j:])
        if i >= r:
            j += 1
    if min_p > No2:
        min_p = No2
    elif max_p < No2:
        max_p = No2

    # 3구역
    No3, j = 0, c - x
    for i in range(r+x, N):
        No3 += sum(matrix[i][:j])
        if j < c - abs(x-y):
            j += 1
    if min_p > No3:
        min_p = No3
    elif max_p < No3:
        max_p = No3

    # 4구역
    No4, j = 0, c+y
    for i in range(r+y+1, N):
        No4 += sum(matrix[i][j:])
        if j > c - abs(x-y):
            j -= 1
    if min_p > No4:
        min_p = No4
    elif max_p < No4:
        max_p = No4

    # 5구역
    No5, le, ri = 0, c, c + 1
    le_check, ri_check = 0, 0
    for i in range(r, r+x+y+1):
        # print(matrix[i][le:ri])
        No5 += sum(matrix[i][le:ri])
        if le_check < x:
            le -= 1
            le_check += 1
        else:
            le += 1
        if ri_check < y:
            ri += 1
            ri_check += 1
        else:
            ri -= 1
    if min_p > No5:
        min_p = No5
    elif max_p < No5:
        max_p = No5
    # print(No1, No2, No3, No4, No5)
    # print(max_p - min_p)
    return max_p - min_p


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 구역 범위 설정
my_min = matrix[3][3] * N * N + 1
for x in range(1, N):
    for y in range(1, N):
        # print('x:', x, 'y', y)
        for c in range(1, N):
            for r in range(1, N):
                if 1 <= r + x + y < N and x < c < N - y:
                    my_min = min(my_min, count_p(x, y, r, c))
print(my_min)
