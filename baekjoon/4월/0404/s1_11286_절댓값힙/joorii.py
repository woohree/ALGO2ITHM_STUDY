import heapq
import sys
sys.stdin = open('M.txt')


# heapq 사용 x
def insert(n):
    arr.append(n)           # 일단 가장 마지막 요소에 추가
    c = len(arr) - 1        # 가장 마지막 요소를 가리킴
    p = c // 2              # c노드의 부모노드

    while 1:
        # 부모노드의 절댓값이 더 크거나, 부모노드와 자식노드의 절댓값은 같으나 값이 더 클 때, 교환
        if (abs(arr[p]) > abs(arr[c])) or (abs(arr[p]) == abs(arr[c]) and arr[p] > arr[c]):
            arr[c], arr[p] = arr[p], arr[c]
            c = p
            p = c // 2
        else:
            break


def delete():
    print(arr[1])                   # 가장 첫번째 노드 일단 출력
    last = arr.pop()                # 마지막 노드를 last 변수에 저장
    if len(arr) > 1:                # 힙에 남아있는 수가 있다면
        arr[1] = last               # 맨 마지막 요소를 루트 노드로 옮김

        p = temp = 1                # 루트노드부터 탐색
        c1, c2 = p * 2, p * 2 + 1   # c1은 왼쪽 자식 노드, c2는 오른쪽 자식 노드

        while 1:
            # 부모노드보다 왼쪽 자식노드의 절댓값이 더 작을 때
            if c1 < len(arr) and abs(arr[c1]) < abs(arr[temp]):
                temp = c1
            # 부모노드와 왼쪽 자식노드의 절댓값은 같지만, 왼쪽자식노드의 값이 더 작을 때
            elif c1 < len(arr) and abs(arr[c1]) == abs(arr[temp]) and arr[c1] < arr[temp]:
                temp = c1

            # 부모노드보다 오른쪽 자식노드의 절댓값이 더 작을 때
            # 혹은 왼쪽 형제노드보다 오른쪽 자식노드의 절댓값이 더 작을 때
            if c2 < len(arr) and abs(arr[c2]) < abs(arr[temp]):
                temp = c2
            # 부모노드 혹은 왼쪽 형제노드와 절댓값은 같지만, 오른쪽 자식 노드의 값이 더 작을 때
            elif c2 < len(arr) and abs(arr[c2]) == abs(arr[temp]) and arr[c2] < arr[temp]:
                temp = c2

            # 부모노드보다 더 작은 값을 발견했다면, 교환
            if temp != p:
                arr[temp], arr[p] = arr[p], arr[temp]
                p = temp
                c1, c2 = p * 2, p * 2 + 1
            else:
                break


def abs_heap(n):
    if len(arr) == 1 and n == 0:
        print('0')
    elif len(arr) > 1 and n == 0:
        delete()
    else:
        insert(n)


N = int(sys.stdin.readline())
arr = [0]
for i in range(N):
    num = int(sys.stdin.readline())
    abs_heap(num)


# heapq 사용
"""
def abs_heapq(n):
    if not arr and n == 0:
        print('0')
    elif n == 0:
        print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(n), n))


N = int(input())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    abs_heapq(num)
"""