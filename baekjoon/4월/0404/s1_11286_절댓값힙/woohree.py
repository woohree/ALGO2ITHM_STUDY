import sys, heapq
sys.stdin = open('L.txt')


N = int(sys.stdin.readline())
tree = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if not n:
        if tree:
            print(heapq.heappop(tree)[1])
        else:
            print(0)
    else:
        heapq.heappush(tree, (abs(n), n))  # 리스트, 튜플 둘다 가능한데, 튜플이 속도가 좀더 빨랐음 + 메모리도 덜 먹음
