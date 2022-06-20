import sys
from itertools import combinations as com
sys.stdin = open('L.txt')


N, L, R, X = map(int, input().split())
probs = list(map(int, input().split()))
cnt = 0
for i in range(2, N+1):
    combs = list(com(probs, i))                                 # 각 경우의 수
    for comb in combs:
        if L <= sum(comb) <= R and max(comb) - min(comb) >= X:  # 조건에 맞는지 확인
            cnt += 1
print(cnt)