import sys
sys.stdin = open('B.txt')


def solution(number):
    n = 0
    for j in range(K):
        n += lan[j] // number
        if n > N:
            return 0
    if n == N:
        return 1
    else:
        return 2


def binary_search(start, end):
    possible = [0]
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == 0:
            mid = 1
        if check == mid:
            break
        check = mid
        k = solution(mid)
        if k == 1:
            possible.append(mid)
            start = mid + 1
        elif k == 0:
            possible.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    return max(possible)


K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
lan.sort()
print(binary_search(lan[-1] // N, sum(lan) // N))
