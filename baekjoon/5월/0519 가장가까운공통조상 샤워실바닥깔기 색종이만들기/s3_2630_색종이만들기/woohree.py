import sys
sys.stdin = open('L.txt')


def div_and_conq(r, c, n):
    global white, blue

    start, flag = mat[r][c], 0                              # 시작지점 숫자, 전부 같은지 판별할 flag
    for i in range(r, r+n):
        for j in range(c, c+n):
            if mat[i][j] != start:                          # 만약 다르면,
                flag = 1                                    # flag 세우고,
                div_and_conq(r, c, n//2)                    # 사분할 재탐색!
                div_and_conq(r + n//2, c, n//2)
                div_and_conq(r, c + n//2, n//2)
                div_and_conq(r + n//2, c + n//2, n//2)
                break
        if flag:
            break

    else:                                                   # 다 같으면,
        if start == 1:
            blue += 1                                       # 구분해서 카운트!
        else:
            white += 1


N = int(input())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = blue = 0
div_and_conq(0, 0, N)
print(white)
print(blue)
