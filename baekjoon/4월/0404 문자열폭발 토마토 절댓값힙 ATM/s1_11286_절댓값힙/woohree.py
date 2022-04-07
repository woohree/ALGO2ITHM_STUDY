import sys, heapq
sys.stdin = open('L.txt')


# N = int(sys.stdin.readline())
# tree = []
# for _ in range(N):
#     n = int(sys.stdin.readline())
#     if not n:
#         if tree:
#             print(heapq.heappop(tree)[1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(tree, (abs(n), n))  # 리스트, 튜플 둘다 가능한데, 튜플이 속도가 좀더 빨랐음 + 메모리도 덜 먹음


def heap_del():                                     # 루트 값 출력하고, 제거
    global last

    if not last:                                    # 마지막 리프가 루트면 0반환
        return 0

    temp = tree[1]                                  # 반환할 루트 값 temp에 저장
    tree[1] = tree[last]                            # 마지막 리프 값을 루트로 갱신
    last -= 1                                       # 트리 길이 하나 줄이고
    p = 1                                           # 부모 노드는 루트
    c = p * 2                                       # 자식 노드
    while c <= last:                                # 자식 노드가 트리 길이 벗어나지 않는 범위에서,
                                                    # 오른쪽 자식이 존재하고, 더 작으면,
        if c+1 <= last and (abs(tree[c]) > abs(tree[c+1]) or (abs(tree[c]) == abs(tree[c+1]) and tree[c] > tree[c+1])):
            c += 1                                  # 오른쪽 자식 선택

        if abs(tree[p]) >= abs(tree[c]):            # 부모값보다 자식값이 작으면,
            if abs(tree[p]) == abs(tree[c]) and tree[p] <= tree[c]:
                break
            tree[p], tree[c] = tree[c], tree[p]     # 자리 바꾸고,
            p = c                                   # 노드도 바꾸기
            c = p * 2
        else:                                       # 최소 힙이면 탈출!
            break

    return temp


def heap_push(n):                                   # 최소 힙에 추가
    global last

    last += 1                                       # 트리 길이 +1
    tree[last] = n                                  # 마지막 리프에 n 저장
    c = last                                        # 자식 노드
    p = c // 2                                      # 부모 노드
    while p > 0 and abs(tree[p]) >= abs(tree[c]):   # 부모노드가 루트가 아니고, 자식값이 부모값보다 작으면,
        if abs(tree[p]) == abs(tree[c]) and tree[p] <= tree[c]:
            break
        tree[p], tree[c] = tree[c], tree[p]         # 자리 바꾸고,
        c = p                                       # 노드도 바꾸기
        p = c // 2


N = int(sys.stdin.readline())
tree = [0] * (N+1)
last = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    if not n:
        print(heap_del())
    else:
        heap_push(n)
# print(tree)
