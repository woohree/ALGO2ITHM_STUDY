import sys
from collections import deque
sys.stdin = open('input.txt')

# 2,000번 보다 작거나 같은 입력만 주어진다.
# N은 50 이하
# 즉 반복되어도 50x50x2000 = 500,000이 최대
# 열리는 연합이 여러개일 때를 모두 고려, BFS로 한 연합은 한 묶음으로 묶기

N, A, B = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 답
days = 0
while 1:
    # 연합이 발생하는 지 확인
    checking_days = 0
    united_number = 0
    check = []
    check_united_number = []
    for i in range(N):
        for j in range(N):
            queue = deque()
            # x, y 좌표와 x,y좌표에 있는 인구 수를 저장
            queue.append([i, j, countries[i][j], united_number])
            while queue:
                left = queue.popleft()
                for k in range(4):
                    check_x = left[0]+dx[k]
                    check_y = left[1]+dy[k]
                    if 0 <= check_x < N and 0<= check_y < N:
                        if A<=abs(countries[left[0]][left[1]]-countries[check_x][check_y])<=B:
                            # 아직 연합에 속해있지 않다면 연합 숫자를 적어서 저장
                            if [left[0], left[1], countries[left[0]][left[1]]] not in check_united_number:
                                check_united_number.append([left[0], left[1], countries[left[0]][left[1]]])
                                check.append([left[0], left[1], countries[left[0]][left[1]], united_number])

                            if [check_x, check_y, countries[check_x][check_y]] not in check_united_number:
                                check_united_number.append([check_x, check_y, countries[check_x][check_y]])
                                check.append([check_x, check_y, countries[check_x][check_y], united_number])
                                queue.append([check_x, check_y, countries[check_x][check_y], united_number])
                                checking_days += 1
            united_number += 1
    number = []
    for i in range(len(check)):
        # 평균을 구해주는 계산
        if check[i][3] not in number:
            number.append(check[i][3])
            avg_son = 0
            avg_mom = 0
            for j in range(len(check)):
                if check[j][3]==check[i][3]:
                    avg_son += check[j][2]
                    avg_mom += 1
            avg = avg_son//avg_mom
            # 평균을 다시 countries에 적용해줌
            for j in range(len(check)):
                if check[j][3] == check[i][3]:
                    countries[check[j][0]][check[j][1]] = avg
    # 바뀐 게 없으면 탈출
    if checking_days == 0:
        break
    # 바뀐게 있으면 반복
    else:
        days += 1
print(days)
