import sys
sys.stdin = open('L.txt')
from collections import deque


def get_time_cross_the_bridge():
    weight = time = 0                           # 다리의 무게, 걸린 시간
    bridge = deque([0]*w)                       # 0이면, 빈 공간
    for bus in buses:
        a = bridge.popleft()                    # 맨 앞 버스 통과
        weight -= a                             # 무게만큼 빼주기
        bridge.append(bus)                      # 다음 버스 출발
        weight += bus                           # 무게만큼 더해주기
        time += 1                               # 1시간 소요

        if weight > L:                          # 다리의 최대 하중보다 무게가 커진다면,
            bridge.pop()                        # 출발 취소!
            weight -= bus
            bridge.append(0)
            while 1:                            # 무게가 최대 하중 이하일 때까지 출발 보류!
                b = bridge.popleft()
                weight -= b
                bridge.append(0)
                time += 1
                if weight + bus <= L:           # 최대 하중 이하라면, 출발!
                    bridge.pop()
                    bridge.append(bus)
                    weight += bus
                    break

    return time + w                             # 제일 마지막에 출발한 버스가 건너가려면 시간에 다리 길이 만큼 더해줘야 함


n, w, L = map(int, sys.stdin.readline().rstrip().split())
buses = deque(map(int, sys.stdin.readline().rstrip().split()))
ans = get_time_cross_the_bridge()
print(ans)

# def get_time_cross_the_bridge():
#     weight = 0
#     time = 0
#     bridge = deque()
#     while buses:
#         w_bus = buses.popleft()
#         weight += w_bus
#
#         if weight > L:
#             time += w - 1
#             weight = 0
#             bridge = deque()
#
#         elif len(bridge) == w:
#             weight -= bridge.popleft()
#
#         bridge.append(w_bus)
#         time += 1
#
#     if bridge:
#         time += w
#
#     return time