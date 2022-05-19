import sys
sys.stdin = open('M.txt')


def fill_tile(r, c, k):     # r 시작 행 인덱스, c 시작 열 인덱스
    global idx

    flag = False
    for i in range(r, r + k):       # 사분면에 배수구가 있는지 확인
        for j in range(c, c + k):
            if matrix[i][j] == -1:
                flag = True
                break
        if flag:
            break

    if flag:        # 사분면에 배수구가 있을 때
        for i in range(r, r + k):
            for j in range(c, c + k):
                if not matrix[i][j]:
                    matrix[i][j] = idx
    else:           # 사분면에 배수구가 없을 때
        for i in range(r, r + k):
            for j in range(c, c + k):
                if i != 0 and i != K - 1 and j != 0 and j != K - 1:
                    continue
                matrix[i][j] = idx

    idx += 1


# 바닥 한 변의 길이
K = 2 ** int(input())
# 배수구의 위치 x, y
x, y = map(int, input().split())
r, c = K - y, x - 1         # 배수구의 위치를 좌상단이 (0,0)인 좌표로 변경
matrix = [[0 for _ in range(K)] for _ in range(K)]
matrix[r][c] = -1           # 배수구 위치 표시
if K == 2:                  # 바닥 한 변의 길이가 2일 때
    for i in range(K):
        for j in range(K):
            print(matrix[i][j], end=' ') if matrix[i][j] == -1 else print(1, end=' ')
        print()
else:                       # 바닥 한 변의 길이가 4일 때
    idx = 1
    fill_tile(0, 0, K // 2)     # 2사분면
    fill_tile(2, 0, K // 2)     # 3사분면
    fill_tile(0, 2, K // 2)     # 1사분면
    fill_tile(2, 2, K // 2)     # 4사분면

    for i in range(K):
        for j in range(K):
            print(matrix[i][j], end=' ') if matrix[i][j] else print(idx, end=' ')
        print()
