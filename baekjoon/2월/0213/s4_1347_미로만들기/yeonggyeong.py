move = int(input())
moves = input()
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# matrix 초기화
matrix = [[0 for i in range(2*len(moves)+1)] for j in range(2*len(moves)+1)]
row, col = len(moves), len(moves)

# 처음 지점 설정
matrix[row][col] = '.'
# 남쪽 방향은 [1, 0] 이기 때문에 idx=2로 설정
idx = 2
for mv in moves:
    if mv == 'R':
        idx = (idx + 1) % 4
    elif mv == 'L':
        if idx != 0:
            idx = idx - 1   
        else:
            idx = 3
    else:
        row, col = row + dx[idx], col + dy[idx]
        matrix[row][col] = '.'

# '.' 이 있는 좌표 구하기
print_lst = []
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == '.':
            print_lst.append([r, c])

# .이 있는 row의 최솟값, 최댓값 col의 최솟값, 최댓값 구해서 빼면 정사각형
min_r, min_c = 101, 101
max_r, max_c = 0, 0

for i in print_lst:
    if min_r > i[0]:
        min_r = i[0]
    if min_c > i[1]:
        min_c = i[1]

    if max_r < i[0]:
        max_r = i[0]
    if max_c < i[1]:
        max_c = i[1]

answers = [m[min_c:max_c+1] for m in matrix[min_r:max_r+1]]

for r in answers:
    for c in r:
        if c == 0:
            c = '#'
        print(c, end='')
    print()