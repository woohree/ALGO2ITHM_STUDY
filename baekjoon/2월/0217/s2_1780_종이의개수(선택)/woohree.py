import sys
sys.stdin = open('L.txt')
sys.setrecursionlimit(10**8)

# 7468ms ㅋㅋㅋㅋㅋㅋㅋㅋㅋ


def get_number_of_papers(matrix, N):
    global cnt_minus
    global cnt_plus
    global cnt_zero

    # 전부 다 같은지 검사,
    # 시간 오래 걸릴 수 있는 구간
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

    # 내부 인자가 다를 경우
    else:
        # N이 1일 경우,
        # 더 재귀돌릴 필요없이 바로 검사 가능
        # 원래 이 줄 없이 했는데 시간초과 => 이거 추가 했더니 가까스로 채점해줌
        if N // 3 == 1:
            for l in range(N):
                for m in range(N):
                    if matrix[l][m] == -1:
                        cnt_minus += 1
                    elif matrix[l][m] == 0:
                        cnt_zero += 1
                    elif matrix[l][m] == 1:
                        cnt_plus += 1

        # 9등분 배열 새로 뽑으면서 재귀 진행,
        # 시간 무조건 오래 걸렸을 구간
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
