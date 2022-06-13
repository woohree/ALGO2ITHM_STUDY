import sys
sys.stdin = open('M.txt')

N = int(sys.stdin.readline())
stack = [0]
answer = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if stack:   # stack이 비어있지 않을 떄
        if stack[-1] < y:       # 스카이라인이 더 높을 때
            stack.append(y)
        else:
            while stack and stack[-1] > y:      # 스카이라인이 더 낮을 때
                stack.pop()
                answer += 1
            if stack[-1] != y:                  # 스카이라인이 같지 않을 때
                stack.append(y)
    else:
        stack.append(y)

answer += len(stack) - 1    # 0 제외
print(answer)
