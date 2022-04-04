import sys, heapq
sys.stdin = open('B.txt')

# 입력값 input 쓰면 시간초과;;
N = int(sys.stdin.readline().rstrip())

# 배열 선언
abs_heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if abs_heap:
            answer = heapq.heappop(abs_heap)
            if answer[1] == 0:
                print(-answer[0])
            else:
                print(answer[0])
        else:
            print(0)
    else:
        # x가 음수일 경우 입력에 -1를 곱해줘서 양수로 입력해야 하므로 얘가 원래 음수인지 체크해줘야 한다.
        # 따라서 list 형식으로 heappush해주었고 음수인 수는 0을, 양수면 1을 두번 째 인자로 넣어주어
        # 절대값이 같을 경우에 원래 음수인 x가 먼저 출력되도록 설정했다.
        if x < 0:
            heapq.heappush(abs_heap, [-x, 0])
        elif x > 0:
            heapq.heappush(abs_heap, [x, 1])
