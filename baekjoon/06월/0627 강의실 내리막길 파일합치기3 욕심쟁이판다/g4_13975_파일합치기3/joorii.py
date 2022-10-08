from heapq import heappush, heappop
import sys
sys.stdin = open('M.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    files.sort()

    answer = 0
    while len(files) != 1:
        temp = heappop(files) + heappop(files)
        answer += temp
        heappush(files, temp)

    print(answer)
