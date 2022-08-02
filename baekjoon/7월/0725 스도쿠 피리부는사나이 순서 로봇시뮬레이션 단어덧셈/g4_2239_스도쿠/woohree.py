import sys
sys.stdin = open('W.txt')


def dfs(n):
    if n == len(zeros):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        exit()                                  # 이거 return으로 했다가 출력초과남.. 전부 0이면 무한루프에 빠짐

    new_r, new_c = zeros[n]                     # 0인 지점 좌표
    for number in range(1, 10):                 # 1~9까지 다 넣어보면서 dfs
        if check(new_r, new_c, number):
            sudoku[new_r][new_c] = number
            dfs(n+1)
            sudoku[new_r][new_c] = 0


def check(r, c, number):
    for check_c in range(9):                    # 가로 체크
        if sudoku[r][check_c] == number:
            return 0

    for check_r in range(9):                    # 세로 체크
        if sudoku[check_r][c] == number:
            return 0

    box_r, box_c = r//3*3, c//3*3
    for check_r in range(3):                    # 박스 체크
        for check_c in range(3):
            if sudoku[box_r+check_r][box_c+check_c] == number:
                return 0
    return 1


sudoku = [list(map(int, list(input()))) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            zeros.append((i, j))
dfs(0)
