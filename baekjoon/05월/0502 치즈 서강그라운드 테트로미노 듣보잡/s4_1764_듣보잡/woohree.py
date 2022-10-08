import sys
sys.stdin = open('L.txt')


# 120ms
N, M = map(int, sys.stdin.readline().split())
not_seen = {}
for _ in range(N):
    not_seen[sys.stdin.readline().rstrip()] = 1     # 보도 못한 사람 딕셔너리에 체크

ans = []
for _ in range(M):
    not_heard = sys.stdin.readline().rstrip()       # 보도 못한 사람에 듣도 못한 사람이 있는지 체크
    if not_seen.get(not_heard):
        ans.append(not_heard)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])

# 132ms
# N, M = map(int, sys.stdin.readline().split())
# not_seen, not_heard = set(), set()
# for _ in range(N):
#     not_seen.add(sys.stdin.readline().rstrip())
# for _ in range(M):
#     not_heard.add(sys.stdin.readline().rstrip())
#
# ans = list(not_seen & not_heard)
# ans.sort()
# print(len(ans))
# for i in range(len(ans)):
#     print(ans[i])