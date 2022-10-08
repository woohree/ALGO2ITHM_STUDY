# 210분
# 25개의 칸: 5 x 5
# 3개 빙고
import sys
sys.stdin = open('B.txt')

# call과 같은 곳을 0으로 바꾸고
# call이 그때마다 bingo의 row or col or cross 합이 0이 되나 검사
# 아무래도 쓸데없는 검사량이 많아지겠지만 break로 백트래킹을 조금이나마 했다.

bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

# answer 리스트 선언
answer = []
# 사회자가 부른 숫자 순서대로 출력해줄 이중 for문
for a in range(5):
    for b in range(5):
        # 빙고의 개수를 셀 count
        count = 0
        # bingo의 이중 for문
        for row in bingo:
            for i in range(5):
                # call의 idx와 같은 숫자를 0으로 바꿔줌
                if row[i] == call[a][b]:
                    row.pop(i)
                    row.insert(i, 0)
                    break
        # 합이 0이 되는 row 카운트
        for m in range(5):
            row_sum = 0
            for n in range(5):
                row_sum += bingo[m][n]
                if row_sum > 0:
                    break
            if row_sum == 0:
                count += 1

        # 합이 0이 되는 col 카운트
        for c in range(5):
            col_sum = 0
            for d in range(5):
                col_sum += bingo[d][c]
                if col_sum > 0:
                    break
            if col_sum == 0:
                count += 1

        # 합이 0이 되는 대각선 카운트
        cross_sum = 0
        for e in range(5):
            cross_sum += bingo[e][e]
            if cross_sum > 0:
                break
        if cross_sum == 0:
            count += 1

        # 합이 0이 되는 또 다른 대각선 카운트
        back_cross_sum = 0
        for f in range(4, -1, -1):
            back_cross_sum += bingo[f][4 - f]
            if back_cross_sum > 0:
                break
        if back_cross_sum == 0:
            count += 1

        # count가 3 이상인 순서를 answer에 저장
        # 원래 값은 맞는데 백준에서는 계속 틀렸다고 떴는데
        # 여기에 break 추가해주니까 갑자기 돌아갔다. 원인은 모르겠다.
        if count >= 3:
            answer.append(a * 5 + b + 1)
            break

# answer에 첫번째로 저장된 값이 정답이므로 다음과 같이 출력.
print(answer[0])
