import heapq
import sys
sys.stdin = open('M.txt')


def min_heap(n):
    if not arr and n == 0:
        print('0')
    elif n == 0:
        print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, n)


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    min_heap(num)
