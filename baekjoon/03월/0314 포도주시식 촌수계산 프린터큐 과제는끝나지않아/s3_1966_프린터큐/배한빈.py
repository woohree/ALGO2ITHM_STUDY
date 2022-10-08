# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 15분
# 문제에 큐가 언급되어있는 만큼 큐를 써서 풀었다.

import sys
sys.stdin = open('B.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    importance = deque(map(int, input().split()))

    # 중요도에 index를 기억
    importance_index = deque([0, 0] for _ in range(N))
    for i in range(N):
        importance_index[i][0] += importance[i]
        importance_index[i][1] += i

    # 출력 순서를 order_of_output에 저장
    # importance_index가 빈 list가 될 때까지 실행
    order_of_output = []
    while importance_index:
        # importance의 첫번째 값이 max 값이라면
        # order_of_output에 importance_index의 첫번째 값을 저장하고
        # importance도 첫번째 값을 pop해줍니다.
        if importance[0] == max(importance):
            order_of_output.append(importance_index.popleft())
            importance.popleft()
        
        # max 값이 아니라면, 맨 뒤로 보냅니다.
        else:
            importance_index.append(importance_index.popleft())
            importance.append(importance.popleft())

    # 아까 입력한 중요도 별 index를 통해 원하는 값을 출력
    for j in range(N):
        if order_of_output[j][1] == M:
            print(j + 1)
            break
