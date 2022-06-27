import sys, heapq
sys.stdin = open('G.txt')


T = int(input())

for t in range(T):
    K = int(sys.stdin.readline())

    files = list(map(int, sys.stdin.readline().rstrip().split()))
    # 리스트 heap으로 바꿔주기
    heapq.heapify(files)

    result = 0
    for _ in range(K-1):
        # 가장 비용이 작은 두개 빼서 더해주고 다시 푸쉬
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        sum_file = file1 + file2
        result += sum_file
        heapq.heappush(files, sum_file)

    print(result)