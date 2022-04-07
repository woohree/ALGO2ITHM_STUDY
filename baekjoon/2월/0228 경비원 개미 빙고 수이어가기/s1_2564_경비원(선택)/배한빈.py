# 40분
# 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미
# 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리
# 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리
# 상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.
# 각 상점 사이의 최단 거리의 합을 출력

import sys
sys.stdin = open('B.txt')

w, h = map(int, input().split())
N = int(input())
store_locations = [list(map(int, input().split())) for _ in range(N)]
mr_dong = list(map(int, input().split()))

# 최소 거리 구한거 넣을 리스트
min_distance = []
for i in range(N):
    # 임시로 거리 구하는 리스트 하나 선언
    distance = []

    # 동근이가 상점이랑 같은 방향에 있을 경우
    if store_locations[i][0] == mr_dong[0]:
        min_distance.append(abs(store_locations[i][1] - mr_dong[1]))

    # 동근이가 북쪽, 상점이 각각 서, 동쪽에 있을 경우
    elif store_locations[i][0] == 3 and mr_dong[0] == 1:
        min_distance.append(store_locations[i][1] + mr_dong[1])
    elif store_locations[i][0] == 4 and mr_dong[0] == 1:
        min_distance.append(w - store_locations[i][1] + mr_dong[1])

    # 동근이가 남쪽, 상점이 각각 서, 동쪽에 있을 경우
    elif store_locations[i][0] == 3 and mr_dong[0] == 2:
        min_distance.append(h - store_locations[i][1] + mr_dong[1])
    elif store_locations[i][0] == 4 and mr_dong[0] == 2:
        min_distance.append(h - store_locations[i][1] + w - mr_dong[1])

    # 동근이가 서쪽, 상점이 각각 북, 남쪽에 있을 경우
    elif store_locations[i][0] == 1 and mr_dong[0] == 3:
        min_distance.append(store_locations[i][1] + mr_dong[1])
    elif store_locations[i][0] == 2 and mr_dong[0] == 3:
        min_distance.append(store_locations[i][1] + h - mr_dong[1])

    # 동근이가 동쪽, 상점이 각각 북, 남쪽에 있을 경우
    elif store_locations[i][0] == 1 and mr_dong[0] == 4:
        min_distance.append(w - store_locations[i][1] + mr_dong[1])
    elif store_locations[i][0] == 2 and mr_dong[0] == 4:
        min_distance.append(w - store_locations[i][1] + h - mr_dong[1])

    # 동근이가 상점이랑 반대 방향에 있을 경우(북, 남)
    elif (store_locations[i][0] == 1 and mr_dong[0] == 2) or (store_locations[i][0] == 2 and mr_dong[0] == 1):
        distance.append(mr_dong[1] + h + store_locations[i][1])
        distance.append((w - mr_dong[1]) + h + (w - store_locations[i][1]))
        min_distance.append(min(distance))

    # 동근이가 상점이랑 반대 방향에 있을 경우(동, 서)
    elif (store_locations[i][0] == 3 and mr_dong[0] == 4) or (store_locations[i][0] == 4 and mr_dong[0] == 3):
        distance.append(mr_dong[1] + w + store_locations[i][1])
        distance.append((h - mr_dong[1]) + w + (h - store_locations[i][1]))
        min_distance.append(min(distance))

print(sum(min_distance))
