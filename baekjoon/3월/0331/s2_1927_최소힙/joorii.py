import heapq
import sys
sys.stdin = open('M.txt')

# heapq 사용
def min_heap(n):
    if not arr and n == 0:
        print('0')
    elif n == 0:
        print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, n)


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    min_heap(num)

# heapq 미사용
"""
def min_heap(n):
    if len(arr) == 1 and n == 0:
        print('0')
    elif len(arr) > 1 and n == 0:
        delete()
    else:
        insert(n)


def insert(n):
    arr.append(n)
    c = len(arr) - 1
    p = c // 2

    while arr[c] < arr[p]:
        arr[c], arr[p] = arr[p], arr[c]
        c = p
        p = c // 2


def delete():
    print(arr[1])
    last = arr.pop()
    if len(arr) > 1:
        arr[1] = last

    p = temp = 1
    c1, c2 = p * 2, p * 2 + 1

    while 1:
        if c1 < len(arr) and arr[c1] < arr[temp]:
            temp = c1
        if c2 < len(arr) and arr[c2] < arr[temp]:
            temp = c2
        if temp != p:
            arr[temp], arr[p] = arr[p], arr[temp]
            p = temp
            c1, c2 = p * 2, p * 2 + 1
        else:
            break


N = int(sys.stdin.readline())
arr = [0]
for i in range(N):
    num = int(sys.stdin.readline())
    min_heap(num)
"""


# 최대힙 (heapq 사용)
"""
def max_heap(n):
    if not arr and n == 0:
        print('0')
    elif n == 0:
        print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -n)


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    max_heap(num)
"""