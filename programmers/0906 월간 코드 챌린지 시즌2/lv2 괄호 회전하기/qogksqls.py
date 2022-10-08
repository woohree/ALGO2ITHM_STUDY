'''
1. deque 사용해서 해결. queue 는 인풋으로 들어온 괄호들이 순환해야 했으므로 사용했다.
2. 열린 괄호가 들어오면 stack에 저장. 닫힌 괄호가 들어왔을 때 stack 마지막 값이 알맞은 열린
괄호인지 검사하고 알맞지 않다면 break.
'''
from collections import deque


def solution(s):
    answer = 0
    q = deque(list(s))
    for _ in range(len(q)):
        stack = []
        flag = 1
        for i in range(len(q)):
            if q[i] in ('[', '{', '('):  # 열린 괄호 검사
                stack.append(q[i])
            else:
                if q[i] == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif q[i] == '}' and stack and stack[-1] == '{':
                    stack.pop()
                elif q[i] == ')' and stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 0
                    break
        if not stack and flag:
            answer += 1
        q.append(q.popleft())  # 순환
    return answer
