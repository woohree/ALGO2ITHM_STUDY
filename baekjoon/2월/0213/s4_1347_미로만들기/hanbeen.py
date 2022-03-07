# 백준 1347 미로 만들기 S4 문제
# 2:24 시작 3:36 알고리즘 고민중

import sys
sys.stdin = open('input.txt')

N = int(input())
words = list(''.join(input()))  # 둘째 줄을 리스트로 받음
matrix = [['#'] * 101 for _ in range(101)]
matrix[50][50] = '.'

dx, dy = [0, -1, 0, 1], [0, -1, 0, 1]  # 처음 남쪽 바라볼때: dx[1], dy[2]

m, n = 2, 3
cx, cy = 50, 50
for word in words:
    x, y = cx + dx[m], cy + dy[n]
    if word == 'R':
        m = (m - 1) % 4
        n = (n - 1) % 4
    elif word == 'L':
        m = (m + 1) % 4
        n = (n + 1) % 4
    else:
        matrix[y][x] = '.'
        cx += dx[m]
        cy += dy[n]

my_min_x = 100
my_max_x = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] == '.':
            if my_min_x > j:
                my_min_x = j
            if my_max_x < j:
                my_max_x = j

for row in range(len(matrix)):
    if not matrix[row] == ['#'] * 101:
        answer = ''.join(matrix[row][my_min_x:my_max_x + 1])
        print(answer)
