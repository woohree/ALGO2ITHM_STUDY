import sys
sys.stdin = open('G.txt')
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    number = int(sys.stdin.readline())

    if number > 0:
        # heap에 number 넣기
        heapq.heappush(heap, number)
    else:
        # 비어있지 않다면
        # 가장 작은 값 반환
        if heap:
            print(heapq.heappop(heap))
        # 비어있다면 0 반환
        else:
            print(0)