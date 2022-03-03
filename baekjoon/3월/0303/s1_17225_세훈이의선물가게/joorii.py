# import!!!
from collections import deque
import sys
sys.stdin = open('M.txt')

# 상민이가 포장하는 데 걸리는 시간 A, 지수가 포장하는 데 걸리는 시간 B, 손님 수 N
A, B, N = map(int, input().split())

# [주문 시각 t, 포장지 색깔('B'/'R') c, 주문 개수 m]
customers = [list(map(str, input().split())) for _ in range(N)]

blue_queue = deque()
red_queue = deque()

# 상민이와 지수의 마지막 시간 표시
blue_end = red_end = 0

for customer in customers:
    # 파란색 포장지일 때, 즉 상민이 손님일 때
    if customer[1] == 'B':
        for n in range(int(customer[2])):
            # 이전 작업이 없을 때
            if blue_end <= int(customer[0]):
                # [시작시간, 끝나는시간]을 append
                blue_queue.append([int(customer[0]), int(customer[0]) + A])
                blue_end = int(customer[0]) + A
            else:
                blue_queue.append([blue_end, blue_end + A])
                blue_end += A

    # 빨간색 포장지일 때, 즉 지수 손님일 때
    elif customer[1] == 'R':
        for n in range(int(customer[2])):
            # 이전 작업이 없을 때
            if red_end <= int(customer[0]):
                # [시작시간, 끝나는시간]을 append
                red_queue.append([int(customer[0]), int(customer[0]) + B])
                red_end = int(customer[0]) + B
            else:
                red_queue.append([red_end, red_end + B])
                red_end += B

# 손님의 순서를 저장할 리스트
blue_idx = []
red_idx = []

orders = len(blue_queue) + len(red_queue)
# 파란색 포장지 주문과 빨간색 포장지 주문 비교를 위한 변수
current_blue, current_red = [], []

# 주문의 개수만큼 반복
for order in range(orders):
    # current_blue, current_red 초기화
    if order == 0 and blue_queue:
        current_blue = blue_queue.popleft()
    if order == 0 and red_queue:
        current_red = red_queue.popleft()

    # 파란색 주문의 시작시간이 빨간색 주문의 시작시간보다 같거나 빠를때
    if current_blue[0] <= current_red[0]:
        # blue_idx에 주문 번호 append
        blue_idx.append(order + 1)
        # 다음 주문으로 current_blue 바꾸기
        if blue_queue:
            current_blue = blue_queue.popleft()
        # 다음 주문이 없으면 비교를 위해 INF로 바꾸어 놓기
        else:
            current_blue = [float('inf')]
    # 빨간색 주문의 시작시간이 빠를 때
    else:
        # red_idx에 주문 번호 append
        red_idx.append(order + 1)
        # 다음 주문으로 current_red 바꾸기
        if red_queue:
            current_red = red_queue.popleft()
        # 다음 주문이 없으면 비교를 위해 INF로 바꾸어 놓기
        else:
            current_red = [float('inf')]

print(len(blue_idx))
print(' '.join(map(str, blue_idx)))
print(len(red_idx))
print(' '.join(map(str, red_idx)))
