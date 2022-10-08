from collections import deque
import sys
sys.stdin = open('M.txt')


def get_time():
    # 다리 위에는 인덱스 저장
    bridge = deque()
    bridge.append(trucks.popleft())
    bridge[0][1] += 1
    # 시간
    time = 1
    # 다리 위의 무게
    total_weight = bridge[0][0]

    # 다리 위에 더 이상 트럭이 없을 때까지
    while bridge:
        time += 1

        for truck in bridge:
            # 트럭의 위치 한 칸씩 전진
            truck[1] += 1

        # 트럭이 다리를 다 건너 갔을 때
        if bridge[0][1] > W:
            temp = bridge.popleft()
            total_weight -= temp[0]

        if trucks:
            # 다음 트럭이 들어왔을 때 다리의 최대하중을 넘을 때
            if total_weight + trucks[0][0] > L:
                pass

            # 다음 트럭이 다리 위로 진입하기
            else:
                temp = trucks.popleft()
                temp[1] += 1        # 위치 다리 위로 변경
                bridge.append(temp)
                total_weight += temp[0]

    return time


# 트럭의 개수 N, 다리의 길이 W, 다리의 최대하중 L
N, W, L = map(int, input().split())
inputs = list(map(int, input().split()))
trucks = deque()
# 트럭의 무게, 트럭 위치(0 ~ W + 1)
for i in range(len(inputs)):
    trucks.append([inputs[i], 0])

print(get_time())
