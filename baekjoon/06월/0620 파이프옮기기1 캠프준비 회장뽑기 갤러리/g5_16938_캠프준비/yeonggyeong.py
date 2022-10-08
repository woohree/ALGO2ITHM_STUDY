import sys
from itertools import combinations
sys.stdin = open('G.txt')

N, L, R, X = map(int, sys.stdin.readline().split())
difficulties = list(map(int, sys.stdin.readline().split()))
# 정렬
difficulties.sort() 

result = 0
for i in range(2, N+1):
    for comb in list(combinations(difficulties, i)):
        # 제시된 조건 확인
        if L <= sum(comb) <= R and (comb[-1] - comb[0]) >= X:
            result += 1

print(result)