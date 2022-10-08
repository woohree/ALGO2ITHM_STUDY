import sys, heapq
sys.stdin = open('B.txt')

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    visited = {}  # 방문 체크 dict
    min_h, max_h = [], []
    for _ in range(k):
        oper, num = sys.stdin.readline().rstrip().split()
        if oper == 'I':
            heapq.heappush(min_h, int(num))
            heapq.heappush(max_h, -int(num))

            # 중복된 수가 있으면 +1 해주고, 처음 보는 숫자면 value 에 1을 넣어 준다.
            if int(num) in visited:
                visited[int(num)] += 1
            else:
                visited[int(num)] = 1

        elif oper == 'D':
            if num == '-1':
                # 해당 최소 힙 숫자의 value 가 1 이상인 것만 보고, 0이라면 min_h가 빌 때까지 while 문 돌린다.
                # 이유는 최대 힙 하면서 value 가 0으로 바뀐 수들은 pass 하기 위함
                while min_h:
                    temp = heapq.heappop(min_h)
                    if visited[temp] >= 1:
                        visited[temp] -= 1
                        break

            elif num == '1':
                while max_h:
                    temp = -heapq.heappop(max_h)
                    if visited[temp] >= 1:
                        visited[temp] -= 1
                        break

    # for 문 돌면서 최대 힙의 value 값이 1 이상 이면 출력
    for _ in range(len(max_h)):
        temp = -heapq.heappop(max_h)
        if visited[temp] >= 1:
            print(temp, end=' ')
            break

    # for 문 돌면서 최소 힙의 value 값이 1 이상 이면 출력
    for _ in range(len(min_h)):
        temp = heapq.heappop(min_h)
        if visited[temp] >= 1:
            print(temp)
            break

    else:
        print('EMPTY')
