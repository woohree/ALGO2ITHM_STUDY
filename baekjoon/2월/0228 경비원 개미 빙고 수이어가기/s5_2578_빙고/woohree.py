import sys
sys.stdin = open('input.txt')


def three_bingo(bingo_map, calls):
    cnt = 0
    for i in range(5):      # i, j는 사회자 호명 숫자판 인덱스
        for j in range(5):
            cnt += 1
            end = 0
            for row in range(5):  # row, col은 빙고판 인덱스
                for col in range(5):
                    if bingo_map[row][col] == calls[i][j]:  # 사회자가 호명하는 숫자 '#'으로 바꾸기
                        bingo_map[row][col] = '#'
                        end = 1
                        break
                if end == 1:
                    break
            # 5x5 빙고판에서 3빙고를 할 수 있는 최솟값이 12,
            # 따라서 12부터 빙고인 지 보면 됨
            if cnt >= 12:
                bingo_cnt = 0  # 전체 빙고 카운트
                cross1_cnt = 0  # 좌상->우하 대각선 빙고 카운트
                cross2_cnt = 0  # 우상->좌하 대각선 빙고 카운트
                for row in range(5):
                    if bingo_map[row] == ['#'] * 5:  # 가로 빙고
                        bingo_cnt += 1
                    col_cnt = 0  # 세로 빙고 카운트
                    for col in range(5):
                        if bingo_map[col][row] == '#':  # 세로 빙고
                            col_cnt += 1
                            if col_cnt == 5:
                                bingo_cnt += 1
                        if row == col and bingo_map[row][col] == '#':  # 좌상->우하 대각선 빙고
                            cross1_cnt += 1
                            if cross1_cnt == 5:
                                bingo_cnt += 1
                        if row+col == 4 and bingo_map[row][col] == '#':  # 우상-> 좌하 대각선 빙고
                            cross2_cnt += 1
                            if cross2_cnt == 5:
                                bingo_cnt += 1
                if bingo_cnt >= 3:  # 빙고가 3개 이상이면 종료!
                    return cnt


bingo_map = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]
ans = three_bingo(bingo_map, calls)
print(ans)
