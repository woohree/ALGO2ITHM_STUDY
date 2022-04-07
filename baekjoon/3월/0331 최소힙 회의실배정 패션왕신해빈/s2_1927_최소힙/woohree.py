import sys
sys.stdin = open('L.txt')


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
        if c+1 <= last and tree[c] > tree[c+1]:     # 오른쪽 자식이 존재하고, 더 작으면,
            c += 1                                  # 오른쪽 자식 선택

        if tree[p] > tree[c]:                       # 부모값보다 자식값이 작으면,
            tree[p], tree[c] = tree[c], tree[p]     # 자리 바꾸고,
            p = c                                   # 노드도 바꾸기
            c = p * 2
        else:                                       # 최소힙이면 탈출!
            break

    return temp


def heap_push(n):                                   # 최소 힙에 추가
    global last

    last += 1                                       # 트리 길이 +1
    tree[last] = n                                  # 마지막 리프에 n 저장
    c = last                                        # 자식 노드
    p = c // 2                                      # 부모 노드
    while p > 0 and tree[p] > tree[c]:              # 부모노드가 루트가 아니고, 자식값이 부모값보다 작으면,
        tree[p], tree[c] = tree[c], tree[p]         # 자리 바꾸고,
        c = p                                       # 노드도 바꾸기
        p = c // 2


N = int(sys.stdin.readline().rstrip())
tree = [0] * (N+1)
last = 0
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if not n:
        print(heap_del())
    else:
        heap_push(n)
print(tree)
