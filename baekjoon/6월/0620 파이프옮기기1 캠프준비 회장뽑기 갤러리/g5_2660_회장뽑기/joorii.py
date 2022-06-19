import sys
sys.stdin = open('M.txt')


def floyd_warshall():
    for k in range(members):
        friends[k][k] = 0
        for i in range(members):
            for j in range(members):
                friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])


INF = float('inf')
# 회원 수
members = int(sys.stdin.readline())
friends = [[INF] * members for _ in range(members)]

while 1:
    a, b = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1:
        break

    friends[a - 1][b - 1] = 1       # 양방향 그래프
    friends[b - 1][a - 1] = 1

floyd_warshall()

min_val = INF           # 가장 작은 점수
candidates = []         # 회장 후보 리스트
for i in range(members):
    if max(friends[i]) < min_val:       # 가장 작은 점수가 갱신되었을 떄
        candidates = [i + 1]
        min_val = max(friends[i])
    elif max(friends[i]) == min_val:    # 가장 작은 점수로 동일할 때
        candidates.append(i + 1)

print(min_val, len(candidates))
print(*candidates)
