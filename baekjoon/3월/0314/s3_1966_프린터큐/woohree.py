from collections import deque
import sys
sys.stdin = open('L.txt')


def get_print_number_of_document(M):
    cnt = 0

    while matrix:
        if len(matrix) == 1:                        # 문서가 1장 남았으면 프린트하고 순서를 출력
            matrix.popleft()
            cnt += 1
            return cnt

        for j in range(1, len(matrix)):
            if matrix[0][1] < matrix[j][1]:         # 가장 앞의 문서와 남은 문서들의 우선순위를 비교해,
                matrix.append(matrix.popleft())     # 더 큰게 있다면 맨 뒤로 보냄
                break
        else:                                       # 더 큰게 없다면
            prt = matrix.popleft()                  # 프린트
            cnt += 1
            if prt[0] == M:                         # 프린트할 게 M이라면, 프린트 순서를 출력
                return cnt


T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    matrix = deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))
    ans = get_print_number_of_document(M)
    print(ans)
