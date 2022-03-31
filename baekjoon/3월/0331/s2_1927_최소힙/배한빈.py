# 이건 혁명..?
# heapq 안 쓰고 그냥 풀면 시간초과...
# heap 직접 구현은 누군가 해주실 것 같다.

import sys, heapq
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
min_heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)

    # 최대 힙
    # 그냥 입력할 때 (-) 붙이면 이제 대소가 뒤바껴서 들어가고,
    # pop하면 원래는 제일 큰 녀석이 나오면서 다시 (-)만 붙이면 되는 모양이다.
    # if x == 0:
    #     if min_heap:
    #         print(-heapq.heappop(min_heap))
    #     else:
    #         print(0)
    # else:
    #     heapq.heappush(min_heap, -x)
