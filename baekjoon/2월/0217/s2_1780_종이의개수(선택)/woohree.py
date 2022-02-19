import sys
sys.stdin = open('L.txt')
sys.setrecursionlimit(10**8)

# 2시간했는데 못품~~
# 2차원 배열 슬라이싱까지 했는데
# 시간초과 ㅜㅜ


def get_number_of_papers(matrix, N):
    global cnt_minus
    global cnt_plus
    global cnt_zero

    end = 0
    for row in range(N):
        for col in range(N):
            if matrix[row][col] != matrix[0][0]:
                end = 1
                break
        if end == 1:
            break

    if end == 0:
        if matrix[0][0] == -1:
            cnt_minus += 1
        elif matrix[0][0] == 0:
            cnt_zero += 1
        elif matrix[0][0] == 1:
            cnt_plus += 1

    else:
        for i in range(0, N, N // 3):
            for j in range(0, N, N // 3):
                new = [[0] * (N // 3) for _ in range(N // 3)]
                for r in range(N // 3):
                    for c in range(N // 3):
                        new[r][c] = matrix[r+i][c+j]
                get_number_of_papers(new, N // 3)


cnt_minus = 0
cnt_zero = 0
cnt_plus = 0

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
get_number_of_papers(matrix, N)
print(f'{cnt_minus}\n{cnt_zero}\n{cnt_plus}')

# end = 0
#
# for row in range(N):
#     for col in range(N):
#         if matrix[row][col] != matrix[0][0]:
#             end = 1
#             break
#     if end == 1:
#         break
#
# if end == 0:
#         if matrix[0][0] == -1:
#             cnt_minus += 1
#         elif matrix[0][0] == 0:
#             cnt_zero += 1
#         elif matrix[0][0] == 1:
#             cnt_plus += 1
#
# else:
#     for i in range(0, N, N//3):
#         for j in range(0, N, N//3):
#             new = [[0] * (N // 3) for _ in range(N // 3)]
#             r1 = c1 = 0
#             for r in range(i, i+(N//3)):
#                 for c in range(j, j+(N//3)):
#                     new[r1][c1] = matrix[r][c]
#                     c1 += 1
#                     if c1 == N//3:
#                         c1 = 0
#                 r1 += 1
#                 if r1 == N//3:
#                     r1 = 0
#             get_number_of_papers(new, N//3)