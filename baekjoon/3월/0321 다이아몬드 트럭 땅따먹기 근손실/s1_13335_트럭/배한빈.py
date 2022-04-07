import sys
sys.stdin = open('B.txt')

from collections import deque

n, w, load = map(int, input().split())  # 트럭개수, 다리길이, 다리의 최대 하중
trucks = deque(map(int, input().split()))  # 트럭 당 무게

bridge = deque([0] * w)

time = 0
while bridge:
    # 124ms
    time += 1
    bridge.popleft()
    if trucks:
        # bridge 의 원소 합과 trucks 의 첫 번째 값을 더한 값이 최대 하중보다 작거나 같은 경우
        if sum(bridge) + trucks[0] <= load:
            bridge.append(trucks.popleft())
        # 최대 하중보다 크면 0만 추가
        else:
            bridge.append(0)

    ## 2896ms
    # for _ in range(w):
    #     if not trucks:
    #         break
    #     if sum(bridge) + trucks[0] <= load and 0 in bridge:
    #         if bridge[-1] != 0:
    #             bridge.popleft()
    #             bridge.append(0)
    #         bridge.pop()
    #         bridge.append(trucks.popleft())
    #         time += 1
    # if not trucks:
    #     break
    # bridge.popleft()
    # bridge.append(0)
    # time += 1
    # if sum(bridge) + trucks[0] <= load:
    #     bridge.pop()
    #     bridge.append(trucks.popleft())

print(time)
