import sys, heapq
sys.stdin = open('B.txt')

T = int(input())
for _ in range(T):
    K = int(input())
    files = sorted(list(map(int, input().split())))
    cost = 0
    while len(files) != 1:
        a, b = heapq.heappop(files), heapq.heappop(files)
        heapq.heappush(files, a + b)
        cost += a + b
    print(cost)
