import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().rstrip().split()))

# 오름차순 정렬
times.sort()

answer = 0
for i in range(1, N + 1):
    answer += sum(times[0:i])  # slice 사용, 이게 시간초과 안 나네? ㅎ

print(answer)

'''
파이썬은 1초에 2000만 = 20,000,000 번 연산이 가능

따라서 시간제한이 1초, n = 100,000 (10만) 이라고 할 때

O(N^2) 으로 알고리즘을 짜게 되면 10,000,000,000 = 100억 번의 연산이 필요하므로, 시간초과가 나게 된다.

이 경우엔 O(NlogN) 으로 알고리즘을 짜야 1,600,000 번의 연산으로 수행 가능하다. (log 100,000 = 약 16)

ATM 문제는 N = 1000이었고, slice는 O(b-a), sort는 O(NlogN)이므로 시간초과가 안난다!
'''