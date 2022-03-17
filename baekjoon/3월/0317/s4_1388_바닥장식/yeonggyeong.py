import sys
sys.stdin = open('G.txt')


def get_count(matrix):
    global n, m
    # 나무 판자의 개수
    tree = 0

    # '-'를 만났을때 다음칸이 범위를 벗어나거나 '|'를 만나면 판자의 개수 추가
    # '|'를 만났을때 다음행이 범위를 벗어나거나 '_'를 만나면 판자의 개수 추가
    for row in range(n):
        for col in range(m):
            # 해당 값이 -라면
            if matrix[row][col] == '-':
                # 범위를 벗어나지 않고
                if 0 <= col+1 < m:
                    # |를 만난다면
                    if matrix[row][col+1] == "|":
                        tree += 1
                else:
                    # 범위를 벗어난다면
                    tree += 1

            # 해당 값이 |라면
            if matrix[row][col] == '|':
                # 범위를 벗어나지 않고
                if 0 <= row+1 < n:
                    #-를 만난다면
                    if matrix[row+1][col] == "-":
                        tree += 1
                else:
                    # 범위를 벗어난다면 
                    tree += 1

    return tree


n, m = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(n)]

answer = get_count(matrix)
print(answer)