import sys
sys.stdin = open('B.txt')


def find_possible_location(i, j, d, next_row, next_col):
    if 0 <= next_row < 4 and 0 <= next_col < 7 and fishes[next_row][next_col] <= 16:
        fishes[i][j], fishes[next_row][next_col] = fishes[next_row][next_col], fishes[i][j]
        fishes[i][j + 1] = d
        fishes[i][j+1], fishes[next_row][next_col+1] = fishes[next_row][next_col+1], fishes[i][j+1]
        return
    else:
        if d == 8:
            d = 1
            next_row, next_col = i + directions[d][0], j + directions[d][1] * 2
            find_possible_location(i, j, d, next_row, next_col)
        else:
            d += 1
            next_row, next_col = i + directions[d][0], j + directions[d][1] * 2
            find_possible_location(i, j, d, next_row, next_col)


def reset_fishes():
    for k in range(1, 17):
        flag = False
        for i in range(4):
            for j in range(0, 7, 2):
                if fishes[i][j] == k:
                    d = fishes[i][j+1]
                    find_possible_location(i, j, d, i + directions[d][0], j + directions[d][1] * 2)
                    flag = True
                    break
            if flag:
                break
    return


def dfs(eat_fishes, c, dirt):
    global my_max
    if 0 <= c[0] + directions[dirt][0] < 4 and 0 <= c[1] + directions[dirt][1] * 2 < 7:
        fishes[c[0]][c[1]], fishes[c[0]][c[1]+1] = 20, 20
        reset_fishes()
        while 1:
            fishes[c[0]][c[1]], fishes[c[0]][c[1]+1] = 0, 0
            c[0] += directions[dirt][0]
            c[1] += directions[dirt][1] * 2
            dfs(eat_fishes+fishes[c[0]][c[1]], c, fishes[c[0]][c[1]+1])
            c[0] -= directions[dirt][0]
            c[1] -= directions[dirt][1] * 2

    else:
        my_max = max(my_max, eat_fishes)
        return


fishes = [list(map(int, input().split())) for _ in range(4)]
directions = {
    1: [-1, 0],
    2: [-1, -1],
    3: [0, -1],
    4: [1, -1],
    5: [1, 0],
    6: [1, 1],
    7: [0, 1],
    8: [-1, 1],
}

my_max = 0
dfs(fishes[0][0], [0, 0], fishes[0][1])

print(my_max)
