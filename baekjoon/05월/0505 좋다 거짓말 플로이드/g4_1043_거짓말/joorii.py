import sys
sys.stdin = open('M.txt')


# 사람의 수 N, 파티의 수 M
N, M = map(int, sys.stdin.readline().split())
# 진실을 아는 사람의 수, 번호
t, *knowns = map(int, sys.stdin.readline().split())
knowns = set(knowns)

parties = []
for _ in range(M):
    cnt, *members = map(int, sys.stdin.readline().split())
    parties.append(set(members))

for _ in range(M):              # 파티의 개수만큼
    for party in parties:       # 모든 파티 탐색
        if knowns & party:      # 진실을 아는 사람이 파티에 있으면
            knowns |= party     # 합집합

ans = 0
for party in parties:           # 각 파티에
    if not party & knowns:      # 진실을 아는 사람과 파티에 온 사람의 교집합이 공집합일 때
        ans += 1

print(ans)
