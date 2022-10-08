import sys
sys.stdin = open('L.txt')
# 1시간 - 일단 100점까지는 받음
# 100점인거 보니까 A, B가 있을 때 뭔가 안되고 있음
# 44% 인가? 멈춤 ㅜㅜ
from collections import deque


def find_person_packed(visit_list):
    blue = deque()
    red = deque()
    cnt_blue = cnt_red = 0  # 상진이, 지수 각자 포장할 갯수
    # 일단 주문 받은거 포장 시작하는 시각으로 저장
    for n in range(N):
        # 주문받은 시각, 색, 갯수
        t, color, ea = int(visit_list[n][0]), visit_list[n][1], int(visit_list[n][2])
        for i in range(ea):
            if color == 'B':
                # (앞에거 포장 시작 시각 + 포장 시간) 보다 추가할 포장 시작 시각이 크다면 그 시각으로 넣기 
                if not blue or (i == 0 and blue[-1]+A < t):
                    blue.append(t)
                else:
                    blue.append(blue[-1]+A)
                cnt_blue += 1
            else:
                if not red or (i == 0 and red[-1]+B < t):
                    red.append(t)
                else:
                    red.append(red[-1]+B)
                cnt_red += 1

    cnt = time = 0
    result_blue = deque()
    result_red = deque()
    # 시간마다 포장시키고 맨앞에거 pop!
    while blue or red:
        while blue and blue[0] == time:
            blue.popleft()
            cnt += 1  # 포장하는 순서
            result_blue.append(cnt)
        while red and red[0] == time:
            red.popleft()
            cnt += 1
            result_red.append(cnt)
        # 다음 포장 시작 시간은 상진이랑 지수 중 작은 값
        if not blue and not red:
            break
        elif not blue:
            time = red[0]
        elif not red:
            time = blue[0]
        elif blue[0] > red[0]:
            time = red[0]
        else:
            time = blue[0]

    print(cnt_blue)
    print(' '.join(map(str, result_blue)))
    print(cnt_red)
    print(' '.join(map(str, result_red)))


A, B, N = map(int, input().split())
visit_list = [list(input().split()) for _ in range(N)]
find_person_packed(visit_list)
