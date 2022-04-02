import heapq
import sys
sys.stdin = open('G.txt')

N = int(input())
orders = [int(input()) for _ in range(N)]


heap = []

for i in range(N):
    if orders[i] == 0:
        if heap:
            num = heapq.heappop(heap)
            print(num[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [abs(orders[i]), orders[i]])
