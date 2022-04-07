# 재귀 사용 시간초과,,
import sys
sys.stdin = open('M.txt')


def jump(col, row, cnt):
    num = matrix[col][row]

    # 가장 오른쪽 아래칸의 0에 도착했을 때
    if col == N - 1 and row == N - 1 and num == 0:
        cnt += 1
        return cnt
    # 가장 오른쪽 아래칸이 아닌 곳에서 0이 있을 때
    elif (col != N - 1 or row == N - 1) and num == 0:
        return cnt

    # 칸의 숫자만큼 아래로 이동
    if col + num < N:
        cnt = jump(col + num, row, cnt)
    # 칸의 숫자만큼 오른쪽으로 이동
    if row + num < N:
        cnt = jump(col, row + num, cnt)

    return cnt


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(jump(0, 0, 0))
