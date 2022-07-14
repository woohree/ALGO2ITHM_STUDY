import sys
sys.stdin = open('W.txt')
sys.setrecursionlimit(10**6)


def find_set(a):
    if a != rep[a]:
        rep[a] = find_set(rep[a])
    return rep[a]


def union(a, b):
    find_f1, find_f2 = find_set(a), find_set(b)
    if find_f1 != find_f2:
        rep[find_f2] = find_f1
        return 0
    else:
        return 1


n, m = map(int, input().split())
rep = {}                            # 대푯값 딕셔너리
for cnt in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    rep.setdefault(a, a)            # 대푯값 추가
    rep.setdefault(b, b)
    flag = union(a, b)              # 대푯값 합치기, 이미 같으면 1, 아니라면 0 반환
    if flag:                        # 이미 같다면,
        print(cnt+1)                # 사이클이 돌았다는 뜻이므로, 값을 출력하고 종료
        break
else:                               # 끝까지 for문이 돌면,
    print(0)                        # 아직 안돌았다는 뜻이므로, 0 출력
