import sys
sys.stdin = open('M.txt')

N, M = map(int, sys.stdin.readline().split())

people = {}
never_heard_seen = []

for _ in range(N):      # 듣도 못한 사람 N명
    name = sys.stdin.readline().rstrip()
    people.setdefault(name, 1)

for _ in range(M):      # 보도 못한 사람 M명
    name = sys.stdin.readline().rstrip()
    if people.get(name):    # 듣도 보도 못한 사람일 때
        never_heard_seen.append(name)

never_heard_seen.sort()
print(len(never_heard_seen))
for name in never_heard_seen:
    print(name)
