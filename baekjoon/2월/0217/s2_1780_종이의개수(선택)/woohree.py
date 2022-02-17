import sys
sys.stdin = open('L.txt')
sys.setrecursionlimit(10**8)

# 2시간했는데 못품~~
# 2차원 배열 슬라이싱 어케하냐 아 짜증나네 ㅋㅋ

cnt_minus = 0
cnt_zero = 0
cnt_plus = 0


def get_number_of_papers(matrix, N):
    judge = 0
    global cnt_minus
    global cnt_plus
    global cnt_zero

    for row in range(N):
        for col in range(N):
            if matrix[row][col] == matrix[0][0]:
                judge += 1

    if judge == N*N:
        if matrix[0][0] == -1:
            cnt_minus += 1
        elif matrix[0][0] == 0:
            cnt_zero += 1
        elif matrix[0][0] == 1:
            cnt_plus += 1

    else:
        for i in range(1, 4):
            new = []
            for j in range(N // 3):
                new += [matrix[j][(i-1)*(N//3):i*(N//3)]]
            print(new)
            get_number_of_papers(new, N//3)

        for l in range(1, 4):
            new2 = []
            for k in range(N // 3, 2 * (N // 3)):
                new2 += [matrix[k][(l-1)*(N//3):l*(N//3)]]
            print(new2)
            get_number_of_papers(new2, N // 3)

        for n in range(1, 4):
            new3 = []
            for m in range(2 * (N // 3), N):
                new3 += [matrix[m][(n-1)*(N//3):n*(N//3)]]
            print(new3)
            get_number_of_papers(new3, N//3)



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
get_number_of_papers(matrix, N)
print(f'{cnt_minus}\n{cnt_zero}\n{cnt_plus}')


# else:
# for i in range(N // 3):
#     new = []
#     for j in range(N // 3):
#         new += [matrix[j][i * (N // 3):(i + 1) * (N // 3)]]
#     # print(new)
#     get_number_of_papers(new, N // 3)
#
# for l in range(N // 3):
#     new2 = []
#     for k in range(N // 3, 2 * (N // 3)):
#         new2 += [matrix[k][l * (N // 3):(l + 1) * (N // 3)]]
#     # print(new2)
#     get_number_of_papers(new2, N // 3)
#
# for n in range(N // 3):
#     new3 = []
#     for m in range(2 * (N // 3), N):
#         new3 += [matrix[m][n * (N // 3):(n + 1) * (N // 3)]]
#     # print(new3)
#     get_number_of_papers(new3, N // 3)