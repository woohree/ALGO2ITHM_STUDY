import sys
sys.stdin = open('B.txt')

'''
1. stack 사용. 0을 넣고 시작
2. 가 현재 이전 빌딩 높이y 값보다 작거나 같을 때까지 pop 계속 해줌
3. 2번 과정 끝나고 y값이 이전 빌딩 높이보다 크다면 append
'''

n = int(sys.stdin.readline().rstrip())
stack = [0]
answer = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    while stack[-1] > y:
        stack.pop()
        answer += 1
    if stack[-1] < y:
        stack.append(y)
print(answer + len(stack) - 1)
