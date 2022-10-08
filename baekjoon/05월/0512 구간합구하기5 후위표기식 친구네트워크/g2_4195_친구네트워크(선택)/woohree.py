import sys
sys.stdin = open('L.txt')


def find_set(a):                                # 대표값 찾기
    if a != rep[a]:
        rep[a] = find_set(rep[a])
    return rep[a]


def union(a, b):
    find_f1, find_f2 = find_set(a), find_set(b)
    if find_f1 != find_f2:
        rep[find_f2] = find_f1                  # 대표값 합치기
        network[find_f1] += network[find_f2]    # f1으로 합쳤으니, f1에다가 f2 친구 수 더해주기


T = int(input())
for tc in range(T):
    F = int(input())
    rep = {}
    network = {}
    for _ in range(F):
        f1, f2 = sys.stdin.readline().split()
        rep.setdefault(f1, f1)                  # 대표값(rep)에 키, 벨류 생성
        network.setdefault(f1, 1)               # 친구 수(network)에 키, 벨류 생성
        rep.setdefault(f2, f2)
        network.setdefault(f2, 1)

        union(f1, f2)                           # 대표값 합치기
        print(network[find_set(f1)])

