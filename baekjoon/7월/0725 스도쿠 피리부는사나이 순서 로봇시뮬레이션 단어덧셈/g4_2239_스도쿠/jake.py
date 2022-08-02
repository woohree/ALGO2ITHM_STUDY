import sys
sys.stdin = open('input.txt')

# 행 체크
def rowCheck(row, num):
    for col in range(9):
        if sdoku[row][col] == num:
            return False
    return True


# 열 체크
def colCheck(col, num):
    for row in range(9):
        if sdoku[row][col] == num:
            return False
    return True


# 3 * 3 체크
def squareCheck(row, col, num):
    now_row = (row // 3) * 3
    now_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sdoku[now_row + i][now_col + j] == num:
                return False
    return True


def dfs(zero):
    # depth에 해당하는 값=현재 0을 채우고 있는 값
    # 만약 끝이라면 스도쿠판 끝에 도달한 것이므로 끝
    if zero == len(zero_sdoku):
        for row in range(9):
            for col in range(9):
                print(sdoku[row][col], end="")
            print()
        exit()

    now_row, now_col = zero_sdoku[zero]  # 현재 확인할 위치
    for num in range(1, 10):
        # 세 가지 조건에 모두 만족하면 숫자 그리기
        if rowCheck(now_row, num) and colCheck(now_col, num) and squareCheck(now_row, now_col, num):
            sdoku[now_row][now_col] = num
            dfs(zero + 1)
            sdoku[now_row][now_col] = 0

# 스도쿠 파일 받아오기
sdoku = [list(map(int, input())) for i in range(9)]
# 0 위치 담기
zero_sdoku = []
for x in range(9):
    for y in range(9):
        if sdoku[x][y] == 0:
            zero_sdoku.append((x, y))
dfs(0)