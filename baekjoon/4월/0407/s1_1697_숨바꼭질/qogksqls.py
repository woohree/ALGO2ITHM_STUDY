# 홈워크 실습과 비슷하다 생각
# 숫자 찾을 때 최소 경로 구하기
# 10m
import sys
sys.stdin = open('B.txt')

'''
# 3000ms bfs
from collections import deque


def bfs():
    global my_min

    while queue:
        my_min += 1
        for _ in range(len(queue)):
            temp = queue.popleft()
            if temp == K:
                return
            if 0 <= temp - 1 and visited[temp - 1] == 0:
                queue.append(temp - 1)
                visited[temp] = 1
            if temp + 1 <= 1000000 and visited[temp + 1] == 0:
                queue.append(temp + 1)
                visited[temp] = 1
            if temp * 2 <= 1000000 and visited[temp * 2] == 0:
                queue.append(temp * 2)
                visited[temp] = 1


N, K = map(int, sys.stdin.readline().rstrip().split())

my_min = -1
visited = [0] * 1000001
queue = deque()
queue.append(N)
bfs()

print(my_min)
'''

'''
# 60ms 재귀
def find(n, k):
    # n이 k보다 클 경우에 할 수 있는 일은 n에 -1을 해주는 방법밖에 없으므로
    # n-k 가 가장 빠른 시간
    if n >= k:
        return n - k

    # n < k 인데 k가 1인 경우는 N=0, K=1인 경우 밖에 없으므로 그냥 1을 return (0, 1)
    # 이게 없으면 k-1일 경우는 괜찮은데, k+1일 때 k=2이면 //2 해줘서 k=1되고 계속 이 짓이 반복되므로 재귀를 못 빠져나감 
    elif k == 1:
        return 1

    # 왜 사람들이 k를 계산해서 n을 찾아나서나 궁금했는데 '곱하기 2' 연산 때문이다.
    # 거꾸로 k부터 계산해 나가면 k가 짝수인지 홀수인지만 생각해서 짝수면 무조건 2로 나누는게 유리하기 때문에
    # 홀수일 경우는 +1, -1한 경우 나눠서 비교
    elif k % 2:
        return min(find(n, k - 1), find(n, k + 1)) + 1

    # 짝수일 경우는 2로 나눴을 때 재귀 돌린 것과 그냥 n과 k의 차이 중에 작은 것 비교
    else:
        return min(k - n, find(n, k // 2) + 1)


N, K = map(int, sys.stdin.readline().split())
print(find(N, K))
'''

'''
# 180ms bfs
from collections import deque


def bfs():
    global my_min

    while queue:
        my_min += 1
        for _ in range(len(queue)):
            temp = queue.popleft()
            if temp == N:  # 수정
                return
            if temp % 2 == 0 and visited[temp // 2] == 0:  # 수정
                queue.append(temp // 2)
                visited[temp] = 1
            if 0 <= temp - 1 and visited[temp - 1] == 0:
                queue.append(temp - 1)
                visited[temp] = 1
            if temp + 1 <= 1000000 and visited[temp + 1] == 0:
                queue.append(temp + 1)
                visited[temp] = 1


N, K = map(int, sys.stdin.readline().rstrip().split())

my_min = -1
visited = [0] * 1000001
queue = deque()
queue.append(K)  # 수정
bfs()

print(my_min)
'''