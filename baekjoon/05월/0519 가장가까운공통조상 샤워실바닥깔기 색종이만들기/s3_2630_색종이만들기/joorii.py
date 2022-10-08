import sys
sys.stdin = open('M.txt')


def divide(r, c, m):        # r 시작 행 인덱스, c 시작 열 인덱스, m 길이
    global white, blue

    color = matrix[r][c]
    flag = False
    for i in range(r, r + m):
        for j in range(c, c + m):
            if matrix[i][j] != color:
                flag = True
                break
        if flag:
            break

    if not flag:    # 모두 같은 색일 때
        if color:
            blue += 1
        else:
            white += 1

    else:           # 정사각형 안에 다른 색이 있을 때
        divide(r, c + m // 2, m // 2)           # 1사분면
        divide(r, c, m // 2)                    # 2사분면
        divide(r + m // 2, c, m // 2)           # 3사분면
        divide(r + m // 2, c + m // 2, m // 2)  # 4사분면


N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = blue = 0
divide(0, 0, N)
print(white, blue)
