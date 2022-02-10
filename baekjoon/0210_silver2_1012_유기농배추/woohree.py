# 24:20 시작 / 25:10 끝
# 이건 진짜 왜 틀린지 모르겠는데???
import sys
sys.stdin = open('input.txt')
# def organic(mat):
#     result = 0
#     for i in range(row):
#         for j in range(col):
#             if mat[i][j] == 1:
#                 if mat[i+1][j] == 0 and mat[i][j+1] == 0:
#                     result += 1
#     return result
#
#
# T = int(input())
# ans = []
# for tc in range(1, T+1):
#     row, col, K = list(map(int, input().split()))
#     matrix = [[0]*(col+1) for _ in range(row+1)]
#     for _ in range(K):
#         cabb_location = list(map(int, input().split()))
#         matrix[cabb_location[0]][cabb_location[1]] = 1
#     a = organic(matrix)
#     ans.append(a)
#
# for tc in range(T):
#     print(ans[tc])


def organic(mat):
    result = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                if i == row-1 and j == col-1:
                    if mat[i][j] == 1:
                        result += 1
                elif i == row - 1:
                    if mat[i][j+1] == 0:
                        result += 1
                elif j == col - 1:
                    if mat[i+1][j] == 0:
                        result += 1
                else:
                    if mat[i+1][j] == 0 and mat[i][j+1] == 0:
                        result += 1
    return result


T = int(input())
ans = []
for tc in range(1, T+1):
    row, col, K = list(map(int, input().split()))
    matrix = [[0]*col for _ in range(row)]
    for _ in range(K):
        cabb_location = list(map(int, input().split()))
        matrix[cabb_location[0]][cabb_location[1]] = 1
    a = organic(matrix)
    ans.append(a)

for tc in range(T):
    print(ans[tc])
