import sys
sys.stdin = open('M.txt')


def find_set(name):
    if name != friends[name]:
        friends[name] = find_set(friends[name])
    return friends[name]


def union(a, b):
    a_rep, b_rep = find_set(a), find_set(b)

    if b_rep != a_rep:
        friends[b_rep] = a_rep
        counts[a_rep] += counts[b_rep]

    return counts[a_rep]


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())

    friends = dict()        # 친구 해싱
    counts = dict()         # 친구 수 해싱
    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())

        if not friends.get(a):
            friends[a] = a
            counts[a] = 1
        if not friends.get(b):
            friends[b] = b
            counts[b] = 1

        print(union(a, b))


"""
# 메모리 초과
T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    friends = dict()
    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())
        friends.setdefault(a, set()).add(b)
        friends.setdefault(b, set()).add(a)
        friends[a] |= friends[b]
        friends[b] |= friends[a]
        print(len(friends[b]))
"""
