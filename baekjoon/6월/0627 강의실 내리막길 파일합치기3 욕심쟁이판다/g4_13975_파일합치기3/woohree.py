import sys, heapq
sys.stdin = open('L.txt')


T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)                # 히피파이
    ans = 0
    while len(files) > 1:
        a = heapq.heappop(files)        # 숫자 2개 픽
        b = heapq.heappop(files)
        heapq.heappush(files, a+b)      # 더한거 다시 푸시
        ans += a + b
    print(ans)