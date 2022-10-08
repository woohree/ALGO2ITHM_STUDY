import sys

sys.stdin = open('G.txt')


def find_set(x):
    if x == networks[x]:
        return x
    else:
        return find_set(networks[x])


def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if a != b:
        networks[b] = a


T = int(sys.stdin.readline())

for tc in range(T):
    F = int(sys.stdin.readline())
    networks = dict()
    for i in range(1, F + 1):
        friend1, friend2 = sys.stdin.readline().rstrip().split()

        networks.setdefault(friend1, friend1)
        networks.setdefault(friend2, friend2)
        union(friend1, friend2)
        if i == 1:
            print(2)
        else:
            parent = find_set(friend1)
            cnt = 0
            for j in networks.values():
                if j == parent:
                    cnt += 1
                elif parent == find_set(j):
                    cnt += 1
            print(cnt)
