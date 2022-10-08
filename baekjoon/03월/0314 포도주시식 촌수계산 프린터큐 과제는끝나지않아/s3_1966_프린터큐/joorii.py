import sys
from collections import deque
sys.stdin = open('M.txt')


def printer_queue():
    target_idx = M
    count = 1

    queue = deque()
    for p in P:
        queue.append(p)

    while queue:
        for i in range(1, len(queue)):
            # 현재 가장 앞에 있는 문서의 중요도보다 높은 문서가 있고 타켓 문서가 아닐 때
            if queue[i] > queue[0] and target_idx != 0:
                temp = queue.popleft()
                target_idx -= 1
                queue.append(temp)
                break
            # 현재 가장 앞에 있는 문서의 중요도보다 높은 문서가 있고 타켓 문서일 때
            elif queue[i] > queue[0] and target_idx == 0:
                temp = queue.popleft()
                target_idx = len(queue)
                queue.append(temp)
                break

        else:
            # 타켓 문서가 아니라면 큐에서 제외만
            if target_idx != 0:
                queue.popleft()
                target_idx -= 1
                count += 1
            else:
                return count


T = int(input())

for tc in range(T):
    # 문서의 개수 N, 궁금한 문서가 몇 번째 놓여있는지 M
    N, M = map(int, input().split())
    # 문서의 중요도
    P = list(map(int, input().split()))

    print(printer_queue())
