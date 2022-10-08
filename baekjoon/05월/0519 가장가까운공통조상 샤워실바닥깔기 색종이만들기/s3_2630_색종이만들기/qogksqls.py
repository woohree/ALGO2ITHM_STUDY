import sys
sys.stdin = open('B.txt')

'''
재귀 돌림
나는 저번 'z'문제가 살짝 연상되긴했다.

check에 기준 색깔 입력

'''


def solution(r, c, n):
    global white, blue

    check = matrix[r][c]
    if n == 1:
        if check == 1:
            blue += 1
        else:
            white += 1
        return

    flag = 1  # flag가 그대로 1이면 그 구간은 전부 같은 색
    for i in range(r, r+n):
        for j in range(c, c+n):
            if matrix[i][j] != check:
                flag = 0  # 이 구간에 두 가지 색깔이 있음
                # 4가지 재귀 돌림, 좌표값 아래와 같이 설정
                solution(r, c, n//2)
                solution(r, c + n//2, n//2)
                solution(r + n//2, c, n//2)
                solution(r + n//2, c + n//2, n//2)
                break
        if not flag:
            break
    if flag:
        if check == 1:
            blue += 1
        else:
            white += 1
        return


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

white = blue = 0
solution(0, 0, N)

print(white)
print(blue)
