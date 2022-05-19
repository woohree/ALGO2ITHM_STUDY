import sys
sys.stdin = open('G.txt')

N = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

white, blue = 0, 0


def cut_page(N, matrix):
    global white, blue
    # 하나의 칸일때,
    if N == 1:
        if matrix[0][0]:
            blue += 1
        else:
            white += 1
        return

    # 입력받은 matrix의 합 구하기
    sum_m = sum([sum(i) for i in matrix])

    # 합이 0이면 흰색으로만 구성
    if sum_m == 0:
        white += 1
        return 
    # 합이 N * N이면 파란색으로만 구성
    elif sum_m == N * N:
        blue += 1
        return
        
    # 사각형 나누기
    left_top, left_bottom, right_top, right_bottom = [], [], [], []
    for row in range(N):
        if row < N // 2:
            left_top.append(matrix[row][:N//2])
            right_top.append(matrix[row][N//2:])
        else:
            left_bottom.append(matrix[row][:N//2])
            right_bottom.append(matrix[row][N//2:])

    cut_page(N//2, left_top)
    cut_page(N//2, right_top)
    cut_page(N//2, left_bottom)
    cut_page(N//2, right_bottom)


cut_page(N, matrix)
print(white)
print(blue)