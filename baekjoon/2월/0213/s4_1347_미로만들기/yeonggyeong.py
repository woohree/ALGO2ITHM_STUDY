import pprint

move = 14
moves = 'LFLFRRFLFRRFLF'
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

matrix = [[0 for i in range(2*len(moves)+1)] for j in range(2*len(moves)+1)]
row, col = len(moves), len(moves)

matrix[row][col] = '.'
idx = 2
mv_cnt = 0
for mv in moves:
    if mv == 'R':
        idx = (idx + 1) % 4
    elif mv == 'L':
        if idx != 0:
            idx = idx - 1   
        else:
            idx = 3
    else:
        mv_cnt += 1
        row, col = row + dx[idx], col + dy[idx]
        matrix[row][col] = '.'

first_r, first_c = 0, 0
for r in range(len(matrix)-1):
    for c in range(len(matrix)-1):
        if matrix[r][c] == '.':
            first_r = r
            first_c = c
            break
        elif matrix[r][c+1] == '.' or matrix[r+1][c] == '.':
            first_r = r
            first_c = c
            break
    if (matrix[first_r][first_c] == '.') or (matrix[first_r+1][first_c] == '.') or (matrix[first_r][first_c+1] == '.'):
        break
print(first_r,first_c, mv_cnt)
answers = [m[first_c:first_c+mv_cnt] for m in matrix[first_r:first_r+mv_cnt]]

for r in answers:
    for c in r:
        if c == 0:
            c = '#'
        print(c, end='')
    print()