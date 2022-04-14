import heapq
import sys
sys.stdin = open('M.txt')


T = int(input())

for tc in range(T):
    k = int(sys.stdin.readline())
    max_hq, min_hq = [], []
    on_heap = [False for _ in range(k)]         # 입력한 순서대로 인덱스 부여, 힙 안에 있는지 판별

    for i in range(k):
        op, num = map(str, sys.stdin.readline().split())
        if op == 'I':           # 삽입
            heapq.heappush(min_hq, (int(num), i))
            heapq.heappush(max_hq, (-int(num), i))
            on_heap[i] = True
        else:                   # 삭제
            if num == '-1':     # 최솟값 삭제
                while min_hq and not on_heap[min_hq[0][1]]:     # 힙에 남아 있는 요소일 때까지
                    heapq.heappop(min_hq)
                if min_hq:
                    on_heap[min_hq[0][1]] = False
                    heapq.heappop(min_hq)
            else:               # 최댓값 삭제
                while max_hq and not on_heap[max_hq[0][1]]:     # 힙에 남아 있는 요소일 때까지
                    heapq.heappop(max_hq)
                if max_hq:
                    on_heap[max_hq[0][1]] = False
                    heapq.heappop(max_hq)

    while min_hq and not on_heap[min_hq[0][1]]:
        heapq.heappop(min_hq)
    while max_hq and not on_heap[max_hq[0][1]]:
        heapq.heappop(max_hq)

    print('EMPTY') if not min_hq and not max_hq else print(f'{-max_hq[0][0]} {min_hq[0][0]}')


"""
# 시간초과
min_hq, max_hq = [], []
for _ in range(k):
    op, n = map(str, input().split())
    if op == 'I':
        heapq.heappush(min_hq, int(n))
        heapq.heappush(max_hq, -int(n))
    elif min_hq and op == 'D':
        if n == '-1':
            temp = heapq.heappop(min_hq)
            max_hq.remove(-temp)
        else:
            temp = -heapq.heappop(max_hq)
            min_hq.remove(temp)
if min_hq:
    print(-max_hq[0], min_hq[0])
else:
    print('EMPTY')
"""
