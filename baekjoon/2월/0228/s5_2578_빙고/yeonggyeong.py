import sys
sys.stdin = open('G.txt')


def get_bingo(matrix, play):

    bingo = [[0] * 5 for _ in range(5)]
    cnt = 0
    # 사회자가 부른 숫자와 인덱스를 반복
    for number, p in enumerate(play):
        for row in range(5):
            for col in range(5):
                # 사회자가 부른 숫자와 빙고판의 숫자가 같다면 해당 빙고 위치를 1로 바꾸기
                if p == matrix[row][col]:
                    bingo[row][col] += 1
                    # 바꾼 빙고 위치의 행이 전부 1이라면 빙고 cnt + 1
                    if bingo[row] == [1, 1, 1, 1, 1]:
                        cnt += 1
                    # 바꾼 빙고 위치의 열이 전부 1이라면 빙고 cnt + 1
                    if [b[col] for b in bingo] == [1, 1, 1, 1, 1]:
                        cnt += 1
                    # 왼쪽 위 시작 대각선이 모두 1이라면 빙고 cnt + 1
                    if (row == col) and [bingo[c][c] for c in range(5)] == [1, 1, 1, 1, 1]:
                        cnt += 1
                    # 오른쪽 위 시작 대각선이 모두 1이라면 빙고 cnt + 1
                    elif (row + col == 4) and [bingo[rc][4-rc] for rc in range(5)] == [1, 1, 1, 1, 1]:
                        cnt += 1

                    # 빙고 개수가 3이상이라면 종료
                    if cnt >= 3:
                        return number + 1

            if matrix[row][col] == p:
                break

matrix = [list(map(int, input().split())) for _ in range(5)]
play = []
for _ in range(5):
    play.extend(list(map(int, input().split())))

print(get_bingo(matrix,play))