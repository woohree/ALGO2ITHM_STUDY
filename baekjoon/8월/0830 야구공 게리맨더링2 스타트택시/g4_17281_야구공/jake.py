import sys
sys.stdin = open('input.txt')

# 처음에는 이닝마다 타순을 다르게 하는 줄 알아서 이상하게 품(병신)
# 타순 정해놓고 이닝마다 하는 지 알았으면 이따구로 안풀었지
from itertools import permutations

def scoring(batters):
    score = 0
    idx = 0
    # 이닝마다 최다점을 구해봄
    for inning in innings:
        out_cnt = 0
        b1, b2, b3 = 0, 0, 0
        while out_cnt < 3:
            if inning[batters[idx]] == 0:
                out_cnt += 1
            elif inning[batters[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[batters[idx]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[batters[idx]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score

innings_count = int(input())
innings = [list(map(int, input().split())) for _ in range(innings_count)]

# 이닝 최다점 합계
total_score = 0

# 1번부터 9번까지 타순을 랜덤하게 구성함
orders = permutations([i for i in range(1, 9)], 8)
for order in orders:
    # 거기에 이제 4번타자 자리에 0번을 끼워넣음
    batters = list(order)[:3] + [0] + list(order)[3:]
    tmp_score = scoring(batters)
    if total_score < tmp_score:
        total_score = tmp_score
print(total_score)
