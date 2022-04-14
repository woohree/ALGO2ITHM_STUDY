import sys, heapq
sys.stdin = open('L.txt')


T = int(sys.stdin.readline())
for tc in range(T):
    k = int(sys.stdin.readline())
    hq_min, hq_max = [], []
    visited = [0] * k
    for i in range(k):
        char, n = sys.stdin.readline().split()
        if char == 'I':
            heapq.heappush(hq_min, (int(n), i))
            heapq.heappush(hq_max, (-int(n), i))
            visited[i] = 1
        else:
            if n == '1':
                while hq_max and not visited[hq_max[0][1]]:     # 최소힙에서 지운거 최대힙에서도 지우기
                    heapq.heappop(hq_max)
                if hq_max:                                      # 다 지웠으면 그 다음 최대값 지우기
                    temp = heapq.heappop(hq_max)
                    visited[temp[1]] = 0
            else:
                while hq_min and not visited[hq_min[0][1]]:     # 최대힙에서 지운거 최소힙에서도 지우기
                    heapq.heappop(hq_min)
                if hq_min:                                      # 다 지웠으면 그 다음 최소값 지우기
                    temp = heapq.heappop(hq_min)
                    visited[temp[1]] = 0

    while hq_max and not visited[hq_max[0][1]]:                 # 덜 지운 찌끄레기들 지워주기
        heapq.heappop(hq_max)
    while hq_min and not visited[hq_min[0][1]]:
        heapq.heappop(hq_min)

    if not hq_min:
        print('EMPTY')
    else:
        print(-heapq.heappop(hq_max)[0], heapq.heappop(hq_min)[0])


